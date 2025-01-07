from fastapi import APIRouter, HTTPException, Header
from apps.nats_transporter import NatsService

router = APIRouter()

@router.get("/elders/gift_cards/{gift_card_id}")
async def get_gift_card(gift_card_id: str, authorization: str = Header(...)):
    try:
        response = await NatsService.request(f"ELDERS.giftCards.get.{gift_card_id}", {}, headers={"Authorization": authorization})
        return {"data": response}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Gift card not found: {str(e)}")
