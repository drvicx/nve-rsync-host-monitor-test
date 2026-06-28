from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import platform
import subprocess
from app.database import SessionLocal
from app.models import Message

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_os_info():
    """Retrieves OS Info (OS type and kernel version)"""
    try:
        # Retrieves OS version
        os_version = subprocess.check_output(
            ['lsb_release', '-ds'], 
            universal_newlines=True
        ).strip()
    except:
        os_version = "Ubuntu 24.04 LTS"  # fallback
    
    try:
        # Retrieves OS kernel version
        os_kernel = platform.uname().release
    except:
        os_kernel = "6.8.0-124-generic"  # fallback
    
    return os_version, os_kernel

@router.get("/api/data")
async def get_data(db: Session = Depends(get_db)):
    """Main Endpoint with database data"""
    
    # Retrieves 1st message from database record or create default message
    message = db.query(Message).first()
    
    if not message:
        # If no database records - creates new default message
        default_message = Message(text="Hello from RSync Monitoring")
        db.add(default_message)
        db.commit()
        db.refresh(default_message)
        message = default_message
    
    # Retrieves OS Info
    os_version, os_kernel = get_os_info()
    
    # Retrieves current Date and Time in ISO format
    current_time = datetime.now().isoformat()
    
    # Returns Python dictionary (same as JSON) as a result
    return {
        "message": message.text,
        "serverInfo": {
            "currentTS": current_time,
            "osVersion": os_version,
            "osKernel": os_kernel
        }
    }
