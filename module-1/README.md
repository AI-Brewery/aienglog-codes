# Module 1: Prompt Engineering Collection

Ever asked ChatGPT or Gemini to do something and gotten a completely wrong answer? This collection teaches you how to write prompts that actually work.

## 📋 What You'll Learn

### Post 1: Prompt Engineering 101 - How to Talk So AI Understands You
- What is prompt engineering and why prompt design matters
- Good vs bad prompts (side-by-side examples)
- Use cases: text generation, coding, summarization
- Zero-shot, few-shot, and role-based prompting basics
- Setting up Google Gemini API (free)

### Post 2: Writing Better Prompts - Templates, Roles, and Real Examples
- Prompt templates ("Act as…", "Explain like I'm 5…")
- Using variables and placeholders
- Role prompting (data analyst, teacher, etc.)
- Reusability and consistency in prompt design
- Simple prompt hacks to improve LLM output

### Post 3: Thinking Like the Model - Few-Shot, Zero-Shot & Chain of Thought
- In-depth examples of zero-shot and few-shot prompting
- When to use which technique
- Chain of Thought prompting: what it is and why it works
- Real examples: reasoning, math, code explanation

### Post 4: Prompt Engineering in the Wild - Task-Specific Prompting
How to prompt for:
- **Summarization**: Extract key insights from documents
- **Question Answering**: Build reliable Q&A systems
- **Code Generation**: Get clean, working code
- **Creative Writing**: Consistent tone and storytelling
- Hands-on prompts to copy and tweak
- Tips on debugging bad prompts
- Intro to prompt optimization through iteration

## ✨ Why This Collection?

- **Hands-on**: Every post has working code examples
- **Free**: Uses Google Gemini's free tier
- **Practical**: Real prompts for real tasks
- **Tested**: Techniques that actually work consistently

## 📋 Prerequisites

- Python and UV package manager

## 🛠️ Dependencies

- `google-genai`: Official Google Generative AI SDK
- `python-dotenv`: For loading environment variables from .env files

## 🚀 Quick Start

1. **Install dependencies**:
   ```bash
   uv sync
   ```

2. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

3. **Get your Gemini API Key**:
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Create a new API key
   - Copy it to your `.env` file

4. **Run the examples**:
   ```bash
   # Run the basic example
   uv run python post1.py
   
   # Run the main application
   uv run python main.py
   ```

## 📁 Files Description

- `post1.py`: Post 1 implementation - Basic Gemini API setup and prompt engineering fundamentals
- `main.py`: Main application entry point with advanced prompt examples
- `pyproject.toml`: Project configuration and dependencies
- `.env.example`: Template for environment variables (Gemini API key)
- `uv.lock`: Locked dependency versions for reproducible installs

### Additional Files (Coming Soon)
- `post2.py`: Prompt templates and role-based prompting examples
- `post3.py`: Few-shot, zero-shot, and Chain of Thought implementations
- `post4.py`: Task-specific prompting for real-world applications

## 🔧 Code Examples

### Basic Usage (post1.py)
```python
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words"
)

print(response.text)
```

## 🔐 Environment Variables

Required environment variables:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

## 📚 Learn More

- [AI Engineering Blog](https://aiengineeringlog.vercel.app) - Complete prompt engineering tutorial series
- [Google Generative AI Documentation](https://ai.google.dev/docs) - Official Gemini API docs
- [Gemini API Reference](https://ai.google.dev/api/rest) - API reference and examples
- [Prompt Engineering Guide](https://www.promptingguide.ai/) - Comprehensive prompting techniques

## 🎯 Next Steps

After completing this module, you'll be ready for:
- Advanced prompt templates and role-based prompting
- Few-shot learning and Chain of Thought techniques  
- Task-specific prompting for real-world applications
- Building production-ready AI systems with better prompts

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your `GEMINI_API_KEY` is correctly set in the `.env` file
2. **Import Error**: Run `uv sync` to install all dependencies
3. **Permission Error**: Check that your API key has the necessary permissions

### Getting Help

If you encounter issues:
1. Check the [official documentation](https://ai.google.dev/docs)
2. Review your API key permissions
3. Ensure all dependencies are installed
