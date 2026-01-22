import asyncpg
import asyncio
import random
from datetime import datetime

async def send_weather_data():
    conn = await asyncpg.connect(
        user="postgres",
        password="postgres",
        database="metricsdb",
        host="localhost"
    )

    temperature = random.uniform(20, 35)

    await conn.execute(
        "INSERT INTO weather VALUES ($1, $2)",
        datetime.utcnow(),
        temperature
    )

    print("Saved temperature:", temperature)

    await conn.close()

asyncio.run(send_weather_data())
