from fastapi import APIRouter

router = APIRouter()

@router.get("/api/status")
async def get_status():
    """Service status check endpoint"""
    return {
        "status": "OK",
        "code": 200
    }
