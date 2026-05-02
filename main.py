from fastapi import FastAPI

app = FastAPI()

@app.get("/") ## Decorador 
async def root ():
    return {"mesagge": "Hello World"}

