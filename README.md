# AI-Powered YouTube to Blog Post Generator using CrewAI

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![CrewAI](https://img.shields.io/badge/CrewAI-AI%20Agents-orange)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

## Project Summary

This project is a Python-based application that automates the process of creating a blog post from a YouTube video. It uses the **CrewAI framework** to build a team of autonomous AI agents that collaborate on the task. The user provides a specific YouTube channel URL and a topic of interest. The AI crew then finds a relevant video on that channel, extracts its full transcript, and writes a comprehensive, well-structured blog post based on the video's content. The final output is saved as a Markdown file, ready for publication.

---

## Key Features

- **Autonomous Agent System**: Utilizes CrewAI to create specialized agents (a Researcher and a Writer) that work together.  
- **Targeted Content Sourcing**: Searches for videos within a specific YouTube channel, ensuring the content comes from a trusted source.  
- **Automated Transcription**: Automatically fetches the full text transcript of the selected video.  
- **AI-Powered Content Generation**: Employs a large language model (like OpenAI's GPT-4) to analyze the transcript and write an engaging and informative blog post.  
- **Structured Workflow**: The process is sequential, ensuring the research is complete before the writing begins.  
- **File Output**: Saves the final blog post as a `.md` (Markdown) file.

---

## Technology Stack

- **Core Framework**: CrewAI  
- **Language**: Python  
- **LLM Integration**: OpenAI (via `langchain-openai`)  
- **YouTube Interaction**: `pytube` (for channel/video searching) and `youtube-transcript-api` (for fetching transcripts)  
- **Configuration**: `python-dotenv` for managing API keys

---

## How It Works (The Process Flow)

1. **Initialization**: `main.py` starts the process with inputs: `topic` and `channel_url`.  
2. **Research Task**: `blog_researcher` is assigned the `research_task`.  
3. **Custom Tool Execution**: The researcher uses `YouTubeSearchAndTranscriptTool` to find a video whose title contains the topic and extract its transcript.  
4. **Context Passing**: The output of the `research_task` is passed as context to the writing task.  
5. **Writing Task**: `blog_writer` uses the transcript to generate a compelling blog post.  
6. **Final Output**: The blog post is saved as `blog_post.md`.

---

## Project File Structure

```
.
├── .env.example
├── .gitignore
├── README.md
├── agents.py
├── blog_post.md
├── crew.py
├── pyproject.toml
├── requirements.txt
├── tasks.py
├── tools.py
└── uv.lock
```

---

## Setup and Installation

1. Ensure **Python 3.8+** is installed.  
2. Clone or download the project.  
3. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```  
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```  
5. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY="sk-..."
   ```

---

## How to Run

1. Navigate to the project root:
   ```bash
   cd project-directory
   ```  
2. Activate the virtual environment.  
3. Run the main script:
   ```bash
   python crew.py
   ```  
4. To change the topic or target channel, modify the `crew_inputs` dictionary in `crew.py`.  
5. After completion, the blog post will be saved as `blog_post.md`.

---

## License

This project is licensed under the **MIT License**.  
---
