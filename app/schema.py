from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class InvoiceCreate(BaseModel):
    customer_name: str
    amount: float
    date: datetime
    status: str = "pending" 

class InvoiceUpdate(BaseModel):
    customer_name: Optional[str] = None
    amount: Optional[float] = None
    date: Optional[datetime] = None
    status: Optional[str] = None

class InvoiceResponse(BaseModel):
    id: int
    customer_name: str
    amount: float
    date: datetime
    status: str

    class Config:
        orm_mode = True  # Enable ORM mode to read data from SQLAlchemy models
