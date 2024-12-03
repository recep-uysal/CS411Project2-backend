from fastapi import FastAPI
import uvicorn
from fastapi import lifespan
from router.login_router import login_router
from router.register_router import register_router
from router.inpatient_router import inpatient_router
from router.admission_router import admission_router
from database_setup import initialize_database  # Import your database setup function

# Define the lifespan context manager
async def lifespan(app: FastAPI):
    # Code to execute on startup
    initialize_database()

    # Yield control to FastAPI
    yield

    # Code to execute on shutdown (if needed)
    # Add any cleanup logic here

# Create the FastAPI app with lifespan
app = FastAPI(lifespan=lifespan)

# Include routers
app.include_router(login_router, prefix="/login")
app.include_router(register_router, prefix="/register")
# Include routers
app.include_router(inpatient_router, prefix="/inpatient")
app.include_router(admission_router, prefix="/admission")

# Test route to verify the app is running
@app.post("/test")
async def read_root():
    return {"message": "Healthcare Management API is running"}

# Entry point for running the app
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=9000,
        reload=False,
        workers=1,
    )
