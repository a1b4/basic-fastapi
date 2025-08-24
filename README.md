# Basic FastAPI Project

A clean and modular FastAPI base project with essential configurations and utilities for rapid API development.

## 🚀 Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **Modular Structure**: Clean separation of concerns with organized code structure
- **Logging System**: Configurable logging with different levels and formats
- **Python 3.12+**: Latest Python features and performance improvements
- **UV Package Manager**: Fast Python package management and virtual environments

## 📁 Project Structure

```
basic-fasapi/
├── src/
│   ├── main.py          # FastAPI application entry point
│   └── logging.py       # Logging configuration utilities
├── main.py              # Project entry point
├── pyproject.toml       # Project configuration and dependencies
├── uv.lock              # Locked dependencies
└── README.md           # This file
```

## 🛠️ Setup

### Prerequisites

- Python 3.12 or higher
- UV package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd basic-fasapi
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Run the application**
   ```bash
   uv run uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## 🚀 Usage

### Starting the Development Server

```bash
# Using UV (recommended)
uv uvicorn main:app --reload
```

### API Endpoints

- **GET /** - Returns a simple "Hello World" message


## 🔧 Development

### Adding New Dependencies

```bash
# Add a new dependency
uv add fastapi uvicorn

# Add development dependencies
uv add --dev pytest flake8
```

### Code Formatting

```bash
# Format code with black
uv run black src/

# Check code style with flake8
uv run flake8 src/
```

## 📝 API Documentation

Once the server is running, you can access:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🏗️ Project Architecture

### Core Components

1. **FastAPI Application** (`main.py`)
   - Main application instance
   - Route definitions
   - API endpoints

2. **Logging System** (`src/logging.py`)
   - Configurable log levels
   - Custom log formats
   - Debug-friendly output

3. **Project Configuration** (`pyproject.toml`)
   - Dependencies management
   - Python version requirements
   - Project metadata

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).


**Happy coding! 🚀**
