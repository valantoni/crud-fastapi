#crear modelo de la tabla de facturas con SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base


class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, index=True)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)
    status = Column(String, default='pending')  
    