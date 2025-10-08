# app/core/security.py

import httpx
from jose import jwt
from fastapi import Request, HTTPException, Depends, status
from app.core.config import settings

async def get_current_user(request: Request):
    auth_header = request.headers.get("authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing token")

    token = auth_header.split(" ")[1]

    async with httpx.AsyncClient() as client:
        jwks = (await client.get(settings.CLERK_JWKS_URL)).json()

    try:
        # Validate token with jose
        payload = jwt.decode(
            token,
            jwks,
            algorithms=["RS256"],
            audience=settings.CLERK_AUDIENCE,
            issuer=settings.CLERK_ISSUER
        )
        return payload
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")
