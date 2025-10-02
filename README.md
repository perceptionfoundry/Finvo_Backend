# Finvo_Backend
# uv commands:

# To create a project (microservice) with uv
uv init test_service

# Now install packages or modules:
uv add fastapi uvicorn

# Check install packages:
uv pip list

# To run fastapi
uv run -- uvicorn app.main:app --reload


users-service/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── routes/
│   │   │   │   └── users.py            # v1 HTTP endpoints
│   │   │   └── schemas/
│   │   │       └── user.py             # v1 request/response schemas
│   │   └── v2/
│   │       ├── routes/
│   │       │   └── profile.py          # v2 HTTP endpoints
│   │       └── schemas/
│   │           └── profile.py          # v2 schemas (could differ from v1)
│   ├── dependencies/
│   │   └── auth.py                     # Shared dependencies (auth, DB sessions, etc.)
│   ├── services/
│   │   └── user_service.py             # Business logic (shared by all versions)
│   ├── core/
│   │   ├── config.py                   # Configurations, env vars
│   │   └── auth.py                     # Clerk token verification, JWT helpers
│   │   ├── settings.py
│   ├── models/                         # DB models (SQLAlchemy, etc.)
│   ├── utils/                          # Helpers/utilities (non-DI helpers)
│   └── main.py                        # FastAPI app entrypoint, include routers here
├── tests/                             # Unit & integration tests
│   └── unit/
│   |   └── test_user_service.py
│   └── integration/
│   |   └── test_users_endpoint.py
├── .env                              # Environment variables
├── .env.example
├── Dockerfile                        # Docker config for containerization
├── pyproject.toml                    # Python dependencies
├── .python-version
├── uv.lock
└── README.md                        # Documentation
