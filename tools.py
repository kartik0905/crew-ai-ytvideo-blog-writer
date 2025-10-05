import os
from crewai.tools import BaseTool 
from pytube import Channel
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled

class YouTubeSearchAndTranscriptTool(BaseTool):
    name: str = "YouTube Video Search and Transcript Tool"
    description: str = (
        "This tool finds a video on a specified YouTube channel based on a topic "
        "and fetches its full transcript. Input should be a dictionary with 'youtube_channel_url' and 'topic'."
    )

    def _run(self, **kwargs) -> str:
        youtube_channel_url = kwargs.get('youtube_channel_url')
        topic = kwargs.get('topic')

        if not youtube_channel_url or not topic:
            return "Error: Both 'youtube_channel_url' and 'topic' must be provided."

        try:
            c = Channel(youtube_channel_url)
            print(f"Searching for videos in channel: {c.channel_name}")


            video_to_transcribe = None
            for video in c.videos:
                if topic.lower() in video.title.lower():
                    video_to_transcribe = video
                    print(f"Found relevant video: '{video.title}'")
                    break
            
            if not video_to_transcribe:
                return f"Error: No video found on the topic '{topic}' in the channel."

            video_id = video_to_transcribe.video_id
            

            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            transcript_text = " ".join([d['text'] for d in transcript_list])
            
            return transcript_text

        except (NoTranscriptFound, TranscriptsDisabled):
            return f"Error: Transcripts are disabled or not available for the video '{video_to_transcribe.title}'."
        except Exception as e:
            return f"An unexpected error occurred: {e}"


yt_transcript_tool = YouTubeSearchAndTranscriptTool()

