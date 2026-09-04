"""Natural Language Generation Service."""

import logging
from typing import Optional

logger = logging.getLogger(__name__)


class NLGService:
    """Service for generating natural language voice output."""

    def __init__(self, language: str = "de-DE"):
        """
        Initialize NLG Service.

        Args:
            language: Language code (default: German)
        """
        self.language = language
        logger.info(f"NLGService initialized (language={language})")

    def generate_vehicle_scan_message(
        self,
        manufacturer: str,
        model: str,
        catalyst_count: int,
        min_price: float,
        max_price: float,
    ) -> str:
        """
        Generate voice message for vehicle scan result.

        Args:
            manufacturer: Vehicle manufacturer
            model: Vehicle model
            catalyst_count: Number of catalysts found
            min_price: Minimum price in EUR
            max_price: Maximum price in EUR

        Returns:
            Natural language message in German
        """
        if catalyst_count == 0:
            return f"{manufacturer} {model} erkannt. Es wurden keine Unterboden-Katalysatoren über 250 Euro gefunden."
        elif catalyst_count == 1:
            return f"{manufacturer} {model} erkannt. 1 passender Unterboden-Katalysator gefunden. Der Ankaufswert liegt bei etwa {max_price:.0f} Euro."
        else:
            return f"{manufacturer} {model} erkannt. {catalyst_count} verschiedene Unterboden-Katalysatoren verbaut. Alle {catalyst_count} liegen in einer Range von {min_price:.0f} bis {max_price:.0f} Euro."

    def generate_ocr_message(
        self,
        part_number: str,
        price: Optional[float],
        vehicle_match: Optional[str],
    ) -> str:
        """
        Generate voice message for OCR scan result.

        Args:
            part_number: Recognized part number
            price: Price in EUR or None
            vehicle_match: Matched vehicle or None

        Returns:
            Natural language message in German
        """
        if price is None:
            return f"Teilenummer {part_number} erkannt. Leider konnte kein Preis ermittelt werden."
        elif vehicle_match:
            return f"Teilenummer {part_number} erkannt. Passt für {vehicle_match}. Ankaufswert: etwa {price:.0f} Euro."
        else:
            return f"Teilenummer {part_number} erkannt. Ankaufswert: etwa {price:.0f} Euro."

    def generate_voice_query_message(
        self,
        recognized_query: str,
        catalyst_count: int,
        min_price: Optional[float],
        max_price: Optional[float],
    ) -> str:
        """
        Generate voice message for voice query result.

        Args:
            recognized_query: Recognized text from voice input
            catalyst_count: Number of catalysts found
            min_price: Minimum price or None
            max_price: Maximum price or None

        Returns:
            Natural language message in German
        """
        if catalyst_count == 0:
            return f"Anfrage nach '{recognized_query}' verarbeitet. Es wurden keine passenden Katalysatoren gefunden."
        elif min_price and max_price:
            return f"Anfrage nach '{recognized_query}' verarbeitet. {catalyst_count} Katalysatoren gefunden. Preisspanne: {min_price:.0f} bis {max_price:.0f} Euro."
        else:
            return f"Anfrage nach '{recognized_query}' verarbeitet. {catalyst_count} Katalysator(en) gefunden."
