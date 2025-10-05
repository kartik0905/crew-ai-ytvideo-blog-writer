from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task
from dotenv import load_dotenv

load_dotenv()


crew = Crew(
  agents=[blog_researcher, blog_writer],
  tasks=[research_task, write_task],
  process=Process.sequential,  
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)


crew_inputs = {
    'topic': 'Agentic RAG',
    'channel_url': 'https://youtube.com/@krishnaik06'
}


print("Crew kicking off!")
result = crew.kickoff(inputs=crew_inputs)


print("Crew execution finished!")


print("Final Result:")
print(result)
print("\n\nBlog post saved to blog_post.md")
