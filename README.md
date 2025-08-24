# Basic FastAPI Project

A clean and modular FastAPI base project with essential configurations and utilities for rapid API development.

## 🚀 Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **Modular Structure**: Clean separation of concerns with organized code structure
- **Authentication System**: JWT-based authentication with user registration and login
- **Logging System**: Configurable logging with different levels and formats
- **Database Integration**: SQLAlchemy ORM with PostgreSQL support
- **Entity Models**: User entity with UUID primary keys and timestamps
- **Docker Support**: PostgreSQL database container with Docker Compose
- **Python 3.12+**: Latest Python features and performance improvements
- **UV Package Manager**: Fast Python package management and virtual environments

## 📁 Project Structure

```
basic-fasapi/
├── src/
│   ├── main.py          # FastAPI application entry point
│   ├── api.py           # API routes registration
│   ├── logging.py       # Logging configuration utilities
│   ├── auth/
│   │   ├── controller.py # Authentication endpoints
│   │   ├── service.py    # Authentication business logic
│   │   ├── models.py     # Authentication Pydantic models
│   │   └── __init__.py   # Auth module initialization
│   ├── database/
│   │   └── core.py      # Database configuration and session management
│   └── entities/
│   │       └── user.py      # User entity model
│   ├── main.py              # Project entry point
│   ├── api.py               # API routes
│   ├── exceptions.py        # Custom exception classes
├── docker-compose.yml   # PostgreSQL Docker configuration
├── init.sql            # Database initialization script
├── pyproject.toml       # Project configuration and dependencies
├── uv.lock              # Locked dependencies
└── README.md           # This file
```

## 🛠️ Setup

### Prerequisites

- Python 3.12 or higher
- UV package manager
- Docker and Docker Compose (for PostgreSQL)

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

3. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp env.example .env
   
   # Generate a secure SECRET_KEY
   python3 -c "import secrets; print('SECRET_KEY=' + secrets.token_urlsafe(32))"
   
   # Update your .env file with the generated SECRET_KEY
   ```

4. **Start PostgreSQL database**
   ```bash
   docker-compose up -d postgres
   ```

5. **Run the application**
   ```bash
   uv run uvicorn src.main:app --reload
   ```

## 🚀 Usage

### Starting the Development Server

```bash
# Using UV (recommended)
uv run uvicorn src.main:app --reload
```

### Database Management

```bash
# Start PostgreSQL
docker-compose up -d postgres

# Stop PostgreSQL
docker-compose down

# View database logs
docker-compose logs -f postgres

# Reset database (clean and restart)
docker-compose down -v
docker-compose up -d postgres
```

### API Endpoints

- **GET /** - Returns a simple "Hello World" message
- **POST /auth/register** - Register a new user
- **POST /auth/token** - Login and get access token
- **GET /auth/me** - Get current user information

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

1. **FastAPI Application** (`src/main.py`)
   - Main application instance
   - Route definitions
   - API endpoints

2. **Authentication System** (`src/auth/`)
   - JWT token generation and validation
   - User registration and login
   - Password hashing with bcrypt
   - Pydantic models for request/response validation

3. **Logging System** (`src/logging.py`)
   - Configurable log levels
   - Custom log formats
   - Debug-friendly output

4. **Database Configuration** (`src/database/core.py`)
   - SQLAlchemy engine setup
   - Database session management
   - Dependency injection for database sessions

5. **Entity Models** (`src/entities/user.py`)
   - User entity with UUID primary key
   - Timestamp fields for audit trails
   - PostgreSQL-specific data types

6. **Docker Configuration** (`docker-compose.yml`)
   - PostgreSQL 15 container
   - Persistent data volumes
   - Health checks
   - Database initialization scripts

7. **Project Configuration** (`pyproject.toml`)
   - Dependencies management
   - Python version requirements
   - Project metadata

## 🔐 Authentication

The project includes a complete JWT-based authentication system:

- **User Registration**: Create new user accounts with email validation
- **User Login**: Authenticate users and receive JWT tokens
- **Token Validation**: Secure endpoint access with JWT verification
- **Password Security**: Bcrypt hashing for secure password storage

### Environment Variables

Required environment variables in `.env`:

```env
DATABASE_URL=postgresql://fasapi_user:fasapi_password@localhost:5432/basic_fasapi_db
SECRET_KEY=your-super-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DEBUG=True
ENVIRONMENT=development
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).


**Happy coding! 🚀**
