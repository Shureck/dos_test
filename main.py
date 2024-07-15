import uvicorn
from fastapi import FastAPI, File, UploadFile, status, Header, Request, Depends, Response
from fastapi.staticfiles import StaticFiles
from prometheus_client import make_asgi_app, Counter, Gauge
from prometheus_fastapi_instrumentator import Instrumentator

import schema
import psutil
import time
import threading
import random
import asyncio
app = FastAPI()

index_counter = Counter('index_counter', 'Description of counter')
cpu_usage = Gauge('cpu_usage', 'CPU usage percentage')
memory_usage = Gauge('memory_usage', 'Memory usage percentage')

def collect_metrics():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_percent = psutil.virtual_memory().percent
        cpu_usage.set(cpu_percent)
        memory_usage.set(memory_percent)
        time.sleep(0.5)

# Запускаем сбор метрик в отдельном потоке
threading.Thread(target=collect_metrics, daemon=True).start()

Instrumentator().instrument(app).expose(app)

@app.get("/")
async def getR():
    index_counter.inc()
    await asyncio.sleep(random.randrange(0, 10)/1000)
    return {"first_root": "one"}
    # return "lol"

@app.get("/add")    
async def addUser():
    index_counter.inc()
    await asyncio.sleep(random.randrange(0, 10)/1000)
    return {"first_root": "add"}
    # # schema.add_new_user("shureck", "keklol","fuck_lol")
    # return "lol"

@app.get("/get")
async def getUser():
    index_counter.inc()
    await asyncio.sleep(random.randrange(0, 10)/1000)
    return {"first_root": "get"}
    # t = schema.get_user("shureck")
    # return "t"