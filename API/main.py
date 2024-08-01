from fastapi import FastAPI
from uvicorn import run
app = FastAPI()


@app.get("/ping")
async def ping():
    return "yah , I am alive"



if __name__ == "__main__":
    run(app, host="localhost", port=8000)