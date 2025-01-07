from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from apps.nats_transporter import NatsService

router = APIRouter()

class RegistrationRequest(BaseModel):
    username: str
    email: str
    password: str

@router.post("/users/register")
async def register_user(request: RegistrationRequest):
    payload = request.dict()
    try:
        response = await NatsService.request("USERS.registration", payload) #@TODO: no ms_users, so use DBService to write directly to DB from API, for now...
        return {"message": "User registered successfully", "data": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Registration failed: {str(e)}")
