"""Voice Query Endpoints."""

from fastapi import APIRouter, File, UploadFile, HTTPException, Query
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/voice", tags=["voice"])


class VoiceQueryRequest(BaseModel):
    """Voice Query Request Schema."""

    query_text: str
    language: str = "de-DE"


class VoiceQueryResponse(BaseModel):
    """Voice Query Response Schema."""

    recognized_query: str
    vehicle_manufacturer: Optional[str]
    vehicle_model: Optional[str]
    catalyst_count: Optional[int]
    min_price_eur: Optional[float]
    max_price_eur: Optional[float]
    voice_message: str
    confidence: float


@router.post("/query", response_model=VoiceQueryResponse)
async def voice_query(
    text: str = Query(..., description="Sprachtext aus Whisper-Transkription"),
) -> VoiceQueryResponse:
    """
    Sprachbasierte Abfrage von Katalysator-Werten.

    Beispiel:
    - Input: "Was bringt der Kat vom BMW E46 328i?"
    - Output: Erkanntes Fahrzeugmodell, Katalysator-Range, Sprachausgabe-Text

    Unterstützt:
    - Natürlichsprachige Anfragen (z.B. "Preis für Volkswagen Polo 6N?")
    - Direkter Teilenummern-Abfrage (z.B. "GM28")
    """
    try:
        raise HTTPException(
            status_code=501,
            detail="Voice Query Engine (Phase 5) noch nicht implementiert",
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
