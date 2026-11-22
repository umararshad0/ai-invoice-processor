from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field


class InvoiceCorrection(BaseModel):
    invoice_number: str | None = Field(default=None, max_length=100)
    supplier_name: str | None = Field(default=None, max_length=255)
    invoice_date: date | None = None
    due_date: date | None = None
    subtotal: Decimal | None = Field(default=None, ge=0, max_digits=12, decimal_places=2)
    tax_amount: Decimal | None = Field(default=None, ge=0, max_digits=12, decimal_places=2)
    total_amount: Decimal | None = Field(default=None, ge=0, max_digits=12, decimal_places=2)
    currency: str | None = Field(default=None, min_length=3, max_length=3)
