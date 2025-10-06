from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from backend.fetch import fetch_events

events_cache = []

app = FastAPI()


async def update_events():
    #fetch new updates and put in cache
    global events_cache
    data = await fetch_events(limit = 50)
    events_cache = data.get("arcs",[])

@app.on_event("startup")
async def on_startup():
    #fetch once at startup
    await update_events()


    #schedule periodic updates
    scheduler = AsyncIOScheduler()
    scheduler.add_job(update_events,'interval',minutes = 1)
    scheduler.start()


@app.get("/events")
async def get_events():
    #put cache in frontend
    return {"arcs" : events_cache}



