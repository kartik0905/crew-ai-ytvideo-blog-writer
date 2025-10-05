from crewai import Task
from agents import blog_researcher, blog_writer


research_task = Task(
  description=(
    'Find a video on the YouTube channel with the URL {channel_url} that is about the topic {topic}. '
    'Then, extract the full text transcript from that video. Your final output must be only the transcript text.'
  ),
  expected_output='The complete text transcript of the found YouTube video.',
  agent=blog_researcher,
)


write_task = Task(
  description=(
    'Using the provided transcript, write a comprehensive and engaging blog post about {topic}. '
    'The post should have a catchy title, an introduction, several body paragraphs discussing key points from the video, and a concluding summary.'
    'Ensure the tone is informative and accessible to a tech-savvy audience.'
  ),
  expected_output='A well-written blog post in markdown format, ready for publication.',
  agent=blog_writer,
  context=[research_task],  
  output_file='blog_post.md'
)
