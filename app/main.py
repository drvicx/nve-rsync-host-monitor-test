from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
import sys
from pathlib import Path

# Adds app root directory to PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database import engine, Base
from app.routers import status, data

# Creates DB tables
Base.metadata.create_all(bind=engine)

# Inits FastAPI
app = FastAPI(
    title="RSync Monitoring Service",
    description="REST API for rsync monitoring",
    version="1.0.0"
)

# Configures CORS rules
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connects routers
app.include_router(status.router)
app.include_router(data.router)

# Implemets root endpoint
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "service": "RSync Monitoring",
        "version": "1.0.0",
        "endpoints": {
            "/api/status": "Checks service status",
            "/api/data": "Retrieves monitoring data from DB"
        }
    }

# Creates app as Web Service and binds to 8000 TCP port
if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="info"
    )
