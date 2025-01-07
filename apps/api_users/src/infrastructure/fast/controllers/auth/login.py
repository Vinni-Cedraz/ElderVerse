from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from apps.nats_transporter import NatsService

router = APIRouter()

#@TODO: move to Domain
class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/users/login")
async def login_user(request: LoginRequest):
    payload = request.dict()
    try:
        response = await NatsService.request("USERS.login", payload)
        return {"message": "Login successful", "data": response}
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Login failed: {str(e)}")
