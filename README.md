# AI Engineering Blog - Code Repository

This repository contains code examples and implementations from my AI Engineering blog posts. Each module corresponds to different blog topics and maintains its own isolated environment for better dependency management and experimentation.

## 📁 Repository Structure

```
aienglog-codes/
├── module-1/           # Gemini API integration examples
│   ├── main.py
│   ├── post1.py
│   ├── pyproject.toml
│   ├── README.md
│   └── uv.lock
├── module-2/           # (Future modules)
├── module-3/           # (Future modules)
└── README.md          # This file
```

## 🛠️ Technology Stack

- **Python**: Primary programming language
- **UV**: Fast Python package manager and project manager
- **Virtual Environments**: Each module has its own isolated environment
- **Environment Variables**: Using `.env` files for API keys and configuration

## 🚀 Getting Started

### Prerequisites

1. **Python 3.12+** installed on your system
2. **UV package manager** - Install it using:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

### Quick Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/himanshuraimau/aienglog-codes.git
   cd aienglog-codes
   ```

2. **Navigate to any module**:
   ```bash
   cd module-1
   ```

3. **Install dependencies using UV**:
   ```bash
   uv sync
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env file with your API keys
   ```

5. **Run the code**:
   ```bash
   uv run python post1.py
   ```

## 📚 Module Guide

### Module 1: Gemini API Integration
- **Topic**: Getting started with Google's Gemini API
- **Dependencies**: `google-genai`, `python-dotenv`
- **Files**:
  - `post1.py`: Basic Gemini API usage example
  - `main.py`: Main application entry point

**Setup for Module 1**:
```bash
cd module-1
uv sync
# Add your GEMINI_API_KEY to .env file
uv run python post1.py
```

## 🔧 Working with UV Package Manager

### Why UV?
- **Fast**: Written in Rust, significantly faster than pip
- **Reliable**: Consistent dependency resolution
- **Modern**: Built-in virtual environment management
- **Compatible**: Works with existing Python ecosystem

### Common UV Commands

```bash
# Create a new project
uv init my-project

# Install dependencies
uv sync

# Add a new dependency
uv add package-name

# Add a development dependency
uv add --dev package-name

# Run Python with project environment
uv run python script.py

# Activate virtual environment
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# Update dependencies
uv lock --upgrade

# Remove a dependency
uv remove package-name
```

## 🔐 Environment Variables

Each module may require different API keys and configuration. Create a `.env` file in each module directory:

```env
# Example .env file
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_key_here
# Add other environment variables as needed
```

**Security Note**: Never commit `.env` files to version control. They are included in `.gitignore`.

## 📝 Module Development Workflow

When creating a new module:

1. **Create module directory**:
   ```bash
   mkdir module-n
   cd module-n
   ```

2. **Initialize UV project**:
   ```bash
   uv init
   ```

3. **Add dependencies**:
   ```bash
   uv add package1 package2
   uv add --dev pytest black flake8  # Development dependencies
   ```

4. **Create environment file**:
   ```bash
   touch .env
   # Add necessary environment variables
   ```

5. **Write your code and README**:
   ```bash
   # Create your Python files
   # Update module-specific README.md
   ```

## 🤝 Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Follow the existing module structure
4. Ensure your code includes proper documentation
5. Test your code thoroughly
6. Submit a pull request

## 📋 Best Practices

### Code Organization
- Keep each module focused on a specific topic
- Use descriptive file names (`post1.py`, `advanced_example.py`)
- Include docstrings and comments
- Follow PEP 8 style guidelines

### Dependency Management
- Use `uv.lock` to lock dependency versions
- Keep `pyproject.toml` updated with proper metadata
- Separate development and production dependencies
- Document any system-level dependencies

### Environment Management
- Always use virtual environments (UV handles this automatically)
- Keep `.env.example` files for required environment variables
- Document all required API keys and their sources

## 🔗 Related Links

- [Blog Website](https://your-blog-url.com)
- [UV Documentation](https://docs.astral.sh/uv/)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

- **Author**: Himanshu Rai
- **GitHub**: [@himanshuraimau](https://github.com/himanshuraimau)
- **Blog**: [Your Blog URL]


---

**Happy Coding! 🚀**

> This repository is part of my AI Engineering blog series. Each module represents practical implementations of concepts discussed in the blog posts.
