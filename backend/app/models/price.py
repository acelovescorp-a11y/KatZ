"""Price and Metals Data Models."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class MetalsPrices(BaseModel):
    """Current Precious Metals Prices per Gram (EUR)."""

    platinum_eur_per_gram: float = Field(..., description="Platin-Preis pro Gramm (EUR)")
    palladium_eur_per_gram: float = Field(
        ..., description="Palladium-Preis pro Gramm (EUR)"
    )
    rhodium_eur_per_gram: float = Field(
        ..., description="Rhodium-Preis pro Gramm (EUR)"
    )
    timestamp: datetime = Field(..., description="Zeitstempel der Preise")
    source: str = Field(default="metals-api", description="Datenquelle")


class Price(BaseModel):
    """Single Price Entry."""

    catalyst_id: int
    price_eur: float
    timestamp: datetime


class PriceCache(BaseModel):
    """Price Cache Entry (Redis)."""

    key: str = Field(..., description="Cache-Key (z.B. 'catalyst:GM28')")
    value: dict = Field(..., description="Gecachter Preis & Daten")
    expires_at: datetime = Field(
        ..., description="Ablaufzeitpunkt (TTL 12h)"
    )


class PriceCacheResponse(BaseModel):
    """Price Cache Response Schema."""

    key: str
    value: dict
    expires_at: datetime
    is_expired: bool = Field(..., description="Ist der Cache abgelaufen?")
