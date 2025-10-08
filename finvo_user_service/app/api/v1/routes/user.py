# app/api/v1/routes/user.py

from fastapi import APIRouter, Depends
from app.core.security import get_current_user

router = APIRouter()

@router.get("/me")
async def get_me(user: dict = Depends(get_current_user)):
    return {
        "clerk_user_id": user.get("sub"),
        "email": user.get("email"),
        "first_name": user.get("first_name"),
        "last_name": user.get("last_name")
    }
