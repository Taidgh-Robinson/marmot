# Movie Association Random Memorable One-liner Tracker

Marmot is a date-aware movie quote application. It finds a film quote related to today's date, or to a date supplied in the URL, and presents it with the corresponding movie poster when available.

The application searches QuoDB, validates and crops quotes with an LLM, enriches movie information through OMDb, and caches results in PostgreSQL.

## Stack

- Frontend: React, TypeScript, Vite, Mantine, and SWR
- Backend: FastAPI, Python 3.12+, and Uvicorn
- Data: PostgreSQL with Liquibase migrations
- Integrations: QuoDB, LiteLLM-compatible model provider, and OMDb API

## Prerequisites

- Node.js and npm
- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- Docker and Docker Compose, for PostgreSQL
- An OMDb API key
- Access to the LLM configured by `LLM_MODEL` and, when applicable, `LLM_LOCAL_BASE`

## Local Setup

1. Start PostgreSQL:

   ```bash
   docker compose up -d db
   ```

2. Create `backend/.env`:

   ```dotenv
   LLM_MODEL=your-model-name
   LLM_LOCAL_BASE=

   PG_HOST=localhost
   PG_USER=user
   PG_PASSWORD=password
   PG_DB=marmot

   OMDBAPI_API_KEY=your-omdb-api-key
   ```

3. Install backend dependencies and start the API:

   ```bash
   cd backend
   uv sync
   uv run uvicorn src.api.app:app --reload
   ```

   The API runs at <http://localhost:8000>. Database migrations run automatically during application startup.

4. Create `frontend/.env`:

   ```dotenv
   VITE_API_BASE_URL=http://localhost:8000
   ```

5. Install frontend dependencies and start the development server:

   ```bash
   cd frontend
   npm install
   npm run dev
   ```

   Open the URL printed by Vite, normally <http://localhost:5173>.

## Usage

- Visit `/` for the current day's quote.
- Visit `/:month/:day/:year` for a specific date, such as `/07/04/2026`.

The backend caches quotes by month and day, so subsequent requests for the same calendar date reuse the stored quote.

## API

| Endpoint | Description |
| --- | --- |
| `GET /quote_of_the_day` | Returns a quote for the current date. |
| `GET /get_quote?date=MM/DD/YYYY` | Returns a quote for the supplied date. |

Both endpoints return:

```json
{
  "quote": "...",
  "movie": "...",
  "poster_url": "..."
}
```

When no matching quote is available, each field is `null`.

## Development Commands

From `frontend`:

```bash
npm run dev
npm run build
npm run lint
```

From `backend`:

```bash
uv run uvicorn src.api.app:app --reload
```

## Project Layout

```text
.
├── backend/
│   ├── changelogs/       # Liquibase schema migrations
│   └── src/
│       ├── api/          # FastAPI application and routes
│       ├── clients/      # External service and database clients
│       ├── models/       # Application and database models
│       └── utils/        # Date and quote processing pipeline
├── frontend/
│   └── src/              # React application
└── compose.yaml          # Local PostgreSQL service
```

## Configuration Notes

- Do not commit `.env` files or API keys.
- `compose.yaml` provides local PostgreSQL credentials that match the example backend configuration.
- The FastAPI CORS configuration permits the Vite development server at `http://localhost:5173`.
