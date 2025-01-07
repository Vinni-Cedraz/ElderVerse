from fastapi import APIRouter, HTTPException, Header
from apps.nats_transporter import NatsService

router = APIRouter()

@router.get("/elders/gift_cards")
async def get_all_gift_cards(authorization: str = Header(...)):
    try:
        response = await NatsService.request("ELDERS.giftCards.getAll", {}, headers={"Authorization": authorization})
        return {"data": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch gift cards: {str(e)}")
