from fastapi import APIRouter, HTTPException, Header, Body
from pydantic import BaseModel
from apps.nats_transporter import NatsService
from http_endpoints import HTTP_ENDPOINTS

router = APIRouter()

class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str

@router.put(HTTP_ENDPOINTS["USERS"]["PROFILE"]["CHANGE_PASSWORD"])
async def change_password(
    id: str,
    request: ChangePasswordRequest = Body(...),
    authorization: str = Header(...)
):
    """
    Endpoint to change the password of a user.
    This sends a request to NATS for handling the password change.
    """
    payload = {
        "user_id": id,
        "old_password": request.old_password,
        "new_password": request.new_password
    }
    
    try:
        # Send the request to NATS and await response
        response = await NatsService.request(
            subject="USERS.changePassword",
            payload=payload,
            headers={"Authorization": authorization}
        )
        return {"message": "Password changed successfully", "data": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to change password: {str(e)}")
