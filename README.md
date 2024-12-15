

### Backend README.md


# Backend Application

This is the FastAPI-based backend for the project. It provides REST APIs for the frontend and handles all server-side logic.

## Prerequisites

- **Python**:
- **pip**: Python package manager.

## Getting Started

### 1. Clone the Repository

Clone the repository and navigate to the backend directory:


### 2. Run the commands 
python -m venv venv

.\venv\Scripts\activate (for Windows)
source venv/bin/activate (for MacOS and Linux)

pip install -r requirements.txt

uvicorn main:app --reload
uvicorn main:app --host 127.0.0.1 --port 9000 --reload --log-level debug (if you want to run on a specific port and see the logs for the debugging)

### 3. About testing
We do not have a separate testing file to be run. However, FastAPI provides a UI for testing the backend functions. Both from the testing UI and from our frontend, we tested our functions and they worked successfully. To test the software, you can go to: 'your-backend-url'/docs to access the testing UI.

