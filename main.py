from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def index():
    return {"message": "hello, world"}

if __name__ == "__main__":
    # Dev only: run "python main.py" and open http://localhost:8080
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)

