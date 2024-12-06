from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

# CORS middleware configuration
origins = [
    "http://localhost:3000",  # Replace with your React app's URL during development
    "https://your-frontend-domain.com",  # Add your deployed React app's URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)

# Include routers
app.include_router(login_router, prefix="/login")
app.include_router(register_router, prefix="/register")
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
