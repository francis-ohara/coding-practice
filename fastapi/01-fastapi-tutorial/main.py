from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def simple_route():
    return {"status": "success", "data": "67 is greater than 42."}
