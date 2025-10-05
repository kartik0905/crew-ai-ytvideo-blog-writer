from crewai import Agent
from tools import yt_transcript_tool
from dotenv import load_dotenv
import os

load_dotenv()


os.environ["OPENAI_MODEL_NAME"] = "gpt-4-turbo"


blog_researcher = Agent(
    role='YouTube Content Researcher',
    goal='Find a video on the topic "{topic}" from the YouTube channel "{channel_url}" and extract its full transcript.',
    verbose=True,
    memory=True,
    backstory=(
        "You are an expert in navigating YouTube channels to find the most relevant content "
        "and possess the ability to meticulously extract video transcripts for further analysis."
    ),
    tools=[yt_transcript_tool],
    allow_delegation=False
)


blog_writer = Agent(
    role='Tech Content Strategist',
    goal='Craft a compelling and insightful blog post from a video transcript on the topic "{topic}".',
    verbose=True,
    memory=True,
    backstory=(
        "You are a renowned Tech Content Strategist, known for your ability to transform "
        "technical transcripts into engaging and easy-to-understand blog posts. You have a knack "
        "for storytelling and making complex topics accessible."
    ),
    tools=[],  
    allow_delegation=False
)
