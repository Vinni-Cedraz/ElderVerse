from fastapi import APIRouter, HTTPException, Header
from apps.nats_transporter import NatsService

router = APIRouter()

@router.delete("/elders/gift_cards/{gift_card_id}")
async def delete_gift_card(gift_card_id: str, authorization: str = Header(...)):
    try:
        await NatsService.emit(f"ELDERS.giftCards.delete.{gift_card_id}", {}, headers={"Authorization": authorization})
        return {"message": "Gift card deletion request sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete gift card: {str(e)}")