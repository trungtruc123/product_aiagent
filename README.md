# ProductAI-agent
Production-ready AI framework built with FastAPI, supporting AI agents and multi-agent workflows using LangGraph. Includes observability with Langfuse and built-in support for RAG systems to deliver accurate, context-aware responses.
# <img src="https://github.com/trungtruc123/product_aiagent/blob/develop/assets/images/ai_architecture_diagram.svg"/>
## 💬 Where to ask questions
Please use our dedicated channels for questions and discussion. Help is much more valuable if it's shared publicly so that more people can benefit from it.

| Type                            | Platforms      |
| ------------------------------- |----------------|
| 🚨 **Bug Reports**              | [GitHub Issue] |
| 🎁 **Feature Requests & Ideas** | [GitHub Issue] |
| 🗯 **General Discussion**       | [Linkedin] or [Gitter Room] |

[GitHub issue]: https://github.com/trungtruc123/product_aiagent/issues
[github discussions]: https://github.com/trungtruc123/product_aiagent/issues
[gitter room]: https://www.facebook.com/profile.php?id=100038801181933
[linkedin]: https://www.linkedin.com/in/truc-tran-trung-380533149/


## 🔗 Links and Resources
| Type                                  | Links                                                                                            |
|---------------------------------------|--------------------------------------------------------------------------------------------------|
| 💼 **FastAPI**                        | [ReadTheDocs](https://fastapi.tiangolo.com/tutorial/)                                            
| 💾 **LangGraph**                      | [LangGraph](https://github.com/langchain-ai/langgraph)                                           |
| 👩‍💻 **PostgresSQL & pgvector**      | [pgvector](https://github.com/pgvector/pgvector)                                                 |
| 💾 **Langfuse**                       | [Langfuse](https://github.com/langfuse/langfuse)                                                 |
| 👩‍💻 **Learn AI-agent for beginner** | [Learn ai-agent](https://github.com/microsoft/ai-agents-for-beginners)                           |
| 📌 **Road Map**                       | [Main Development Plans](https://github.com/trungtruc123/product_aiagent/blob/develop/README.md) 

## 🌟 Features

- **Production-Ready Architecture**

  - Build high-performance asynchronous APIs using FastAPI, optimized with uvloop for better performance 2x-4x times in linux ( others asyncio in window)
  - Create AI-agent and Multi-agent workflows with LangGraph, including support for persistent state.
  - Monitor and debug LLM interactions using Langfuse.
  - Use structured logging to track requests with clear formatting across different environments.
  - Apply flexible rate limiting rules to control API usage per endpoint.
  - Store application data and embeddings with PostgreSQL and pgvector (or pipecone).
  - Deploy easily with Docker and Docker Compose.
  - Monitor system performance using Prometheus and visualize metrics through Grafana.

- **AI & LLM Features**
  - Integrates MCP and A2A for secure and efficient access to external tools.
  - Uses Hybrid RAG (keyword + vector search) to improve retrieval accuracy.
  - Supports advanced memory (short-term, long-term, Redis, entity memory) with automatic conversation summarization to reduce cost.
  - Reliable LLM service with auto-retry using Tenacity.
  - Supports multiple models such as GPT-4o, GPT-4o mini, and GPT-5 series.
  - Real-time chat via streaming responses.
  - Built-in tool calling and function execution.

- **Security**

  - JWT-based authentication
  - Session management
  - Input sanitization ( help prevent XSS and other injection attacks)
  - CORS configuration
  - Rate limiting protection

- **Developer Experience**

  - Environment-specific configuration with automatic .env file loading
  - Comprehensive logging system with context binding
  - Clear project structure following best practices
  - Type hints throughout for better IDE support
  - Easy local development setup with Makefile commands
  - Automatic retry logic with exponential backoff for resilience

- **Evaluation**
  - Automated metric-based evaluation of model outputs
  - Integration with Langfuse for trace analysis
  - Detailed JSON reports with success/failure metrics
  - Interactive command-line interface
  - Customizable evaluation metrics

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- PostgreSQL ([see Database setup](#database-setup))
- Docker and Docker Compose (optional)

### Environment Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd <project-directory>
```

2. Create and activate a virtual environment:
First install uv (uv == setup.py + requirement.txt)```pip install uv ```
```bash
uv sync
```

3. Copy the example environment file:

```bash
cp .env.example .env.[development|staging|production] # e.g. .env.development
```

4. Update the `.env` file with your configuration (see `.env.example` for reference)

### Database setup

1. Create a PostgreSQL database (e.g Supabase or local PostgreSQL)
2. Update the database connection settings in your `.env` file:

```bash
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=mydb
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

### Running the Application

#### Local Development

1. Install dependencies:

```bash
uv sync
```

2. Run the application:
- window:
```bash
uv run uvicorn app.main:app --reload --port 8000 --loop asyncio
```
- linux or mac:
```bash
uv run uvicorn app.main:app --reload --port 8000 --loop uvloop
```
1. Go to Swagger UI:

```bash
http://localhost:8000/docs
```

#### Using Docker

1. Build and run with Docker Compose:

```bash
make docker-build-env ENV=[development|staging|production] # e.g. make docker-build-env ENV=development
make docker-run-env ENV=[development|staging|production] # e.g. make docker-run-env ENV=development
```

2. Access the monitoring stack:

```bash
# Prometheus metrics
http://localhost:9090

# Grafana dashboards
http://localhost:3000
Default credentials:
- Username: admin
- Password: admin
```

The Docker setup includes:

- FastAPI application
- PostgreSQL database
- Prometheus for metrics collection
- Grafana for metrics visualization
- Pre-configured dashboards for:
  - API performance metrics
  - Rate limiting statistics
  - Database performance
  - System resource usage

## 📊 Model Evaluation

The project includes a robust evaluation framework for measuring and tracking model performance over time. The evaluator automatically fetches traces from Langfuse, applies evaluation metrics, and generates detailed reports.

### Running Evaluations

You can run evaluations with different options using the provided Makefile commands:

```bash
# Interactive mode with step-by-step prompts
make eval [ENV=development|staging|production]

# Quick mode with default settings (no prompts)
make eval-quick [ENV=development|staging|production]

# Evaluation without report generation
make eval-no-report [ENV=development|staging|production]
```

### Evaluation Features

- **Interactive CLI**: User-friendly interface with colored output and progress bars
- **Flexible Configuration**: Set default values or customize at runtime
- **Detailed Reports**: JSON reports with comprehensive metrics including:
  - Overall success rate
  - Metric-specific performance
  - Duration and timing information
  - Trace-level success/failure details

### Customizing Metrics

Evaluation metrics are defined in `evals/metrics/prompts/` as markdown files:

1. Create a new markdown file (e.g., `my_metric.md`) in the prompts directory
2. Define the evaluation criteria and scoring logic
3. The evaluator will automatically discover and apply your new metric

### Viewing Reports

Reports are automatically generated in the `evals/reports/` directory with timestamps in the filename:

```
evals/reports/evaluation_report_YYYYMMDD_HHMMSS.json
```

Each report includes:

- High-level statistics (total trace count, success rate, etc.)
- Per-metric performance metrics
- Detailed trace-level information for debugging

## 🔧 Configuration

The application uses a flexible configuration system with environment-specific settings:

- `.env.development` - Local development settings
- `.env.staging` - Staging environment settings
- `.env.production` - Production environment settings

### Environment Variables

Key configuration variables include:

```bash
# Application
APP_ENV=development
PROJECT_NAME="Product AI Agent"
DEBUG=true

# Database
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=mydb
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

# LLM Configuration
OPENAI_API_KEY=your_openai_api_key
DEFAULT_LLM_MODEL=gpt-4o
DEFAULT_LLM_TEMPERATURE=0.7
MAX_TOKENS=4096

# Long-Term Memory
LONG_TERM_MEMORY_COLLECTION_NAME=agent_memories
LONG_TERM_MEMORY_MODEL=gpt-4o-mini
LONG_TERM_MEMORY_EMBEDDER_MODEL=text-embedding-3-small

# Observability
LANGFUSE_PUBLIC_KEY=your_public_key
LANGFUSE_SECRET_KEY=your_secret_key
LANGFUSE_HOST=https://cloud.langfuse.com

# Security
SECRET_KEY=your_secret_key_here
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Rate Limiting
RATE_LIMIT_ENABLED=true
```

## 🧠 Long-Term Memory

The application includes a sophisticated long-term memory system powered by mem0ai and pgvector:

### Features

- **Semantic Memory Storage**: Stores and retrieves memories based on semantic similarity
- **User-Specific Memories**: Each user has their own isolated memory space
- **Automatic Memory Management**: Memories are automatically extracted, stored, and retrieved
- **Vector Search**: Uses pgvector for efficient similarity search
- **Configurable Models**: Separate models for memory processing and embeddings

### How It Works

1. **Memory Addition**: During conversations, important information is automatically extracted and stored
2. **Memory Retrieval**: Relevant memories are retrieved based on conversation context
3. **Memory Search**: Semantic search finds related memories across conversations
4. **Memory Updates**: Existing memories can be updated as new information becomes available

## 🤖 LLM Service

The LLM service provides robust, production-ready language model interactions with automatic retry logic and multiple model support.

### Features

- **Multiple Model Support**: Pre-configured support for GPT-4o, GPT-4o-mini, GPT-5, and GPT-5 variants
- **Automatic Retries**: Uses tenacity for exponential backoff retry logic
- **Reasoning Configuration**: GPT-5 models support configurable reasoning effort levels
- **Environment-Specific Tuning**: Different parameters for development vs production
- **Fallback Mechanisms**: Graceful degradation when primary models fail

### Supported Models

| Model       | Use Case                | Reasoning Effort |
| ----------- | ----------------------- | ---------------- |
| gpt-5       | Complex reasoning tasks | Medium           |
| gpt-5-mini  | Balanced performance    | Low              |
| gpt-5-nano  | Fast responses          | Minimal          |
| gpt-4o      | Production workloads    | N/A              |
| gpt-4o-mini | Cost-effective tasks    | N/A              |

### Retry Configuration

- Automatically retries on API timeouts, rate limits, and temporary errors
- **Max Attempts**: 3
- **Wait Strategy**: Exponential backoff (1s, 2s, 4s)
- **Logging**: All retry attempts are logged with context

## 📝 Advanced Logging

The application uses structlog for structured, contextual logging with automatic request tracking.

### Features

- **Structured Logging**: All logs are structured with consistent fields
- **Request Context**: Automatic binding of request_id, session_id, and user_id
- **Environment-Specific Formatting**: JSON in production, colored console in development
- **Performance Tracking**: Automatic logging of request duration and status
- **Exception Tracking**: Full stack traces with context preservation

### Logging Context Middleware

Every request automatically gets:
- Unique request ID
- Session ID (if authenticated)
- User ID (if authenticated)
- Request path and method
- Response status and duration

### Log Format Standards

- **Event Names**: lowercase_with_underscores
- **No F-Strings**: Pass variables as kwargs for proper filtering
- **Context Binding**: Always include relevant IDs and context
- **Appropriate Levels**: debug, info, warning, error, exception

## ⚡ Performance Optimizations

### uvloop Integration

The application uses uvloop for enhanced async performance (automatically enabled via Makefile):

**Performance Improvements**:
- 2-4x faster asyncio operations
- Lower latency for I/O-bound tasks
- Better connection pool management
- Reduced CPU usage for concurrent requests

### Connection Pooling
Helps improve performance, increase stability, prevent database overload, and use system resources more efficiently.
Avoids creating a new database connection for every request, which is time-consuming.Example: If an API receives 1,000 requests per second, it could create 1,000 database connections, which significantly slows down the system.
- **Database**: Async connection pooling with configurable pool size
- **LangGraph Checkpointing**: Shared connection pool for state persistence
- **Redis** (optional): Connection pool for caching

### Caching Strategy

- Only successful responses are cached
- Configurable TTL based on data volatility
- Cache invalidation on updates
- Supports Redis or in-memory caching

## 🔌 API Reference

### Authentication Endpoints

- `POST /api/v1/auth/register` - Register a new user
- `POST /api/v1/auth/login` - Authenticate and receive JWT token
- `POST /api/v1/auth/logout` - Logout and invalidate session

### Chat Endpoints

- `POST /api/v1/chatbot/chat` - Send message and receive response
- `POST /api/v1/chatbot/chat/stream` - Send message with streaming response
- `GET /api/v1/chatbot/history` - Get conversation history
- `DELETE /api/v1/chatbot/history` - Clear chat history

### Health & Monitoring

- `GET /health` - Health check with database status
- `GET /metrics` - Prometheus metrics endpoint

For detailed API documentation, visit `/docs` (Swagger UI) or `/redoc` (ReDoc) when running the application.


## 📞 Support some issue

### Pgvector not install
pgvector is an extension for PostgreSQL that enables storing and searching vector embeddings directly within the database.

1.**Setup**
 - Linux/Mac:
```bash
cd /tmp
git clone --branch v0.8.2 https://github.com/pgvector/pgvector.git
cd pgvector
make
make install # may need sudo
```
 - Window:

  Ensure C++ support in Visual Studio is installed and run x64 Native Tools Command Prompt for VS [version] as administrator. Then use nmake to build:
```bash
set "PGROOT=C:\Program Files\PostgreSQL\18"
cd %TEMP%
git clone --branch v0.8.2 https://github.com/pgvector/pgvector.git
cd pgvector
nmake /F Makefile.win
nmake /F Makefile.win install
```
2.**Test**

Open PGadmin4 -> Tool -> PSQL tool -> enter
```bash
CREATE EXTENSION vector;
CREATE TABLE items (id bigserial PRIMARY KEY, embedding vector(3));
INSERT INTO items (embedding) VALUES ('[1,2,3]'), ('[4,5,6]');
SELECT * FROM items ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
```
