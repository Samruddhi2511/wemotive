from fastapi import FastAPI
import asyncpg

app = FastAPI()

@app.on_event("startup")
async def connect_db():
    app.state.db = await asyncpg.connect(
        user="postgres",
        password="postgres",
        database="metricsdb",
        host="localhost"
    )

@app.get("/weather")
async def get_weather():
    rows = await app.state.db.fetch(
        "SELECT * FROM weather ORDER BY time DESC LIMIT 10"
    )
    return [dict(r) for r in rows]
