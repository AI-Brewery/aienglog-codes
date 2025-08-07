# AI Engineering Blog - Code Repository

Code examples and implementations from my AI Engineering blog posts. Each module is self-contained with its own environment for easy experimentation.

## 📁 Repository Structure

```
aienglog-codes/
├── module-1/           # Prompt Engineering Collection
│   ├── post1.py        # Prompt Engineering 101
│   ├── main.py         # Advanced examples
│   └── README.md       # Module documentation
├── module-2/           # (Future modules)
└── README.md          # This file
```

## 🚀 Quick Start

1. **Install UV package manager**:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone and setup**:
   ```bash
   git clone https://github.com/himanshuraimau/aienglog-codes.git
   cd aienglog-codes/module-1
   uv sync
   cp .env.example .env
   # Add your API keys to .env
   uv run python post1.py
   ```

## 📚 Modules

### Module 1: Prompt Engineering Collection
Complete guide to writing prompts that actually work.

- **Post 1**: Prompt Engineering 101 - Fundamentals & Gemini API setup
- **Post 2**: Better Prompts - Templates, roles, and examples  
- **Post 3**: Advanced Techniques - Few-shot, zero-shot, Chain of Thought
- **Post 4**: Real-World Applications - Task-specific prompting

**Tech**: Google Gemini API (free tier), Python, UV

## 🛠️ Working with UV

UV is a fast Python package manager that handles virtual environments automatically.

```bash
# Navigate to any module and run:
uv sync          # Install dependencies
uv run python script.py    # Run with project environment
uv add package-name        # Add new dependency
```

## 🔗 Links

- **Blog**: [aiengineeringlog.vercel.app](https://aiengineeringlog.vercel.app)
- **GitHub**: [@himanshuraimau](https://github.com/himanshuraimau)
- **UV Docs**: [docs.astral.sh/uv](https://docs.astral.sh/uv/)

---

Each module contains detailed setup instructions and examples. Happy coding! 🚀
