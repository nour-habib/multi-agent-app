# MultiAgentApp

## Project Structure

```
MultiAgentApp/
├── agent_backend/   # Python FastAPI service (AI agents)
├── backend/         # NestJS backend (REST API + PostgreSQL)
└── ui/              # Next.js frontend
```

---

## Prerequisites

- Node.js (v18+)
- Python (3.10+)
- PostgreSQL

---

## 1. Agent Backend (Python / FastAPI)

```bash
cd agent_backend

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
```

---

## 2. NestJS Backend

```bash
cd backend/multi-agent-app

# Install dependencies
npm install

# Run in development mode
npm run start:dev
```

Configure your PostgreSQL connection in the `TypeOrmModule` inside `app.module.ts`:

```ts
TypeOrmModule.forRoot({
  type: 'postgres',
  host: 'localhost',
  port: 5432,
  username: 'your_user',
  password: 'your_password',
  database: 'your_db',
  entities: [],
  synchronize: true,
})
```

---

## 3. UI (Next.js)

```bash
cd ui/multi-agent-app

# Install dependencies
npm install

# Run in development mode
npm run dev
```
