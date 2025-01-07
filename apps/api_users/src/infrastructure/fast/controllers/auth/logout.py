from fastapi import APIRouter, Header, HTTPException
from apps.nats_transporter import NatsService

router = APIRouter()

@router.post("/auth/logout")
async def logout_user(authorization: str = Header(...)):
    try:
        await NatsService.emit("USERS.logout", {"token": authorization}) #@TODO: DBService
        return {"message": "Logout successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Logout failed: {str(e)}")
