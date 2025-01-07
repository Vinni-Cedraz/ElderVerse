from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel
from apps.nats_transporter import NatsService

router = APIRouter()

class GenerateGiftCardRequest(BaseModel):
    occasion: str
    recipient_name: str
    message: str

@router.post("/elders/gift_cards/generate")
async def generate_gift_card(request: GenerateGiftCardRequest, authorization: str = Header(...)):
    payload = request.dict()
    try:
        response = await NatsService.request("ELDERS.giftCards.generate", payload, headers={"Authorization": authorization})
        return {"message": "Gift card generation request sent", "data": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate gift card: {str(e)}")
