"""
Script to run the FastAPI backend server
"""
import sys
import os
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import uvicorn
from backend.config import settings

if __name__ == "__main__":
    print("=" * 60)
    print("Starting Restaurant POS Backend Server")
    print("=" * 60)
    print(f"API Documentation: http://localhost:{settings.BACKEND_PORT}/docs")
    print(f"API Base URL: http://localhost:{settings.BACKEND_PORT}{settings.API_V1_PREFIX}")
    print("=" * 60)
    print("\nPress CTRL+C to stop the server\n")
    
    uvicorn.run(
        "backend.main:app",
        host=settings.BACKEND_HOST,
        port=settings.BACKEND_PORT,
        reload=True
    )