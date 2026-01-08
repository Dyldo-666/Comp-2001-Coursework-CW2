import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from .models import ProfileCreate, ProfileUpdate
from . import crud
from .auth_client import get_auth_user

load_dotenv()

app = FastAPI(
    title="COMP2001 ProfileService (CW2)",
    description="ProfileService microservice for the Trail Application (COMP2001).",
    version="1.0.0",
)

# Basic OWASP-friendly defaults
allowed_origins = os.getenv("CORS_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in allowed_origins],
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/profiles")
def get_profiles(limit: int = 50):
    if limit < 1 or limit > 200:
        raise HTTPException(status_code=400, detail="limit must be 1..200")
    return crud.list_profiles(limit=limit)

@app.get("/profiles/{username}")
def get_profile(username: str):
    profile = crud.read_profile_summary(username)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@app.post("/profiles", status_code=201)
def post_profile(payload: ProfileCreate):
    # You can optionally enforce "must exist in authenticator" here,
    # but some students prefer to just demonstrate integration via /auth route.
    result = crud.create_profile(payload.model_dump())
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("message", "Create failed"))
    return result

@app.put("/profiles/{username}")
def put_profile(username: str, payload: ProfileUpdate):
    result = crud.update_profile(username, payload.model_dump())
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("message", "Update failed"))
    return result

@app.delete("/profiles/{username}")
def delete_profile(username: str):
    result = crud.delete_profile(username)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("message", "Delete failed"))
    return result

@app.get("/profiles/{username}/auth")
async def get_profile_auth(username: str):
    """
    Evidence endpoint: show user info coming from the Authenticator API.
    """
    user = await get_auth_user(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found in Authenticator API")
    return user
