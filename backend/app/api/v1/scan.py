"""Vehicle and OCR Scan Endpoints."""

from fastapi import APIRouter, File, UploadFile, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/scan", tags=["scan"])


class ScanResponse(BaseModel):
    """Scan Response Schema."""

    vehicle_manufacturer: str
    vehicle_model: str
    vehicle_generation: str
    catalyst_count: int
    min_price_eur: float
    max_price_eur: float
    voice_message: str
    message: Optional[str] = None


class OCRResponse(BaseModel):
    """OCR Scan Response."""

    part_number: str
    recognized_text: str
    confidence: float
    price_eur: Optional[float]
    vehicle_match: Optional[str]


@router.post("/vehicle", response_model=ScanResponse)
async def scan_vehicle(file: UploadFile = File(...)) -> ScanResponse:
    """
    Fahrzeug-Scan via Kamerabild.

    - Empfängt Fahrzeug-Foto
    - Erkennt Hersteller, Modell, Baureihe via GPT-4o Vision
    - Ruft Katalysator-Daten ab
    - Wendet Business-Filter an
    - Generiert Sprachausgabe-Text

    Returns: Fahrzeugdaten, Katalysator-Range, Sprachtext
    """
    try:
        # Placeholder für Vision AI Integration
        raise HTTPException(
            status_code=501,
            detail="Vision AI Integration (Phase 3) noch nicht implementiert",
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/ocr", response_model=OCRResponse)
async def scan_ocr(file: UploadFile = File(...)) -> OCRResponse:
    """
    OCR-Scan für Katalysator-Teilenummern.

    - Empfängt Foto der Teilenummer
    - Erkennt Text via Google ML Kit (lokal auf Client)
    - Sucht Teilenummer in Datenbank
    - Gibt aktuellen Ankaufswert zurück

    Returns: Erkannte Teilenummer, Preis, Fahrzeug-Match
    """
    try:
        raise HTTPException(
            status_code=501,
            detail="OCR Integration (Phase 4) noch nicht implementiert",
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
