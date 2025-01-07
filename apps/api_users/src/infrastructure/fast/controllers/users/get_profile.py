from fastapi import APIRouter
from http_endpoints import HTTP_ENDPOINTS

router = APIRouter()

@router.get(HTTP_ENDPOINTS["USERS"]["PROFILE"]["GET"])
async def get_user_profile(id: str):
    return {"message": f"Fetched profile for user {id}"}
