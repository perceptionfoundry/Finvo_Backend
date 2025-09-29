# Finvo_Backend

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
│   ├── models/                         # DB models (SQLAlchemy, etc.)
│   ├── utils/                          # Helpers/utilities (non-DI helpers)
│   └── main.py                        # FastAPI app entrypoint, include routers here
├── tests/                             # Unit & integration tests
│   └── test_users.py
├── .env                              # Environment variables
├── Dockerfile                        # Docker config for containerization
├── requirements.txt                  # Python dependencies
└── README.md                        # Documentation
