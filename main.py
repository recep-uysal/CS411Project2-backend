from fastapi import FastAPI
import uvicorn
from project.login import login_router

app = FastAPI()
app.include_router(login_router)

@app.post("/test")
async def read_root():
    return {"hello world!"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=9000,
        reload=False,
        workers=1,
    )