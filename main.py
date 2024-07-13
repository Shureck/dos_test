import uvicorn
from fastapi import FastAPI, File, UploadFile, status, Header, Request, Depends
from fastapi.staticfiles import StaticFiles
from prometheus_client import make_asgi_app, Counter
import schema
app = FastAPI()

index_counter = Counter('index_counter', 'Description of counter')

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

@app.get("/")
async def getR():
    return "lol"

@app.get("/add")
async def addUser():
    index_counter.inc()
    schema.add_new_user("shureck", "keklol","fuck_lol")
    return "lol"

@app.get("/get")
async def getUser():
    t = schema.get_user("shureck")
    return t