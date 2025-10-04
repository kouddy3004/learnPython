import uvicorn
from fastapi import FastAPI

from ezGameMultiAgent.src.backend.api import api_router

# Initialize the FastAPI application [1]
app = FastAPI(
    title="Multi-Agent Game Tester POC",
    description="Backend for coordinating LangChain-based agents for game testing."
)

# Include the API routes for planning, execution, and reports
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def read_root():
    """Simple health check endpoint."""
    return {"message": "Multi-Agent POC Backend is running."}


if __name__ == "__main__":
    # Command to run the server locally: uvicorn main:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)
