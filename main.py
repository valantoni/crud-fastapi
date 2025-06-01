from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from app.schema import InvoiceCreate, InvoiceUpdate, InvoiceResponse
from app import crud

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API de Facturación"}

@app.post("/invoices/", response_model=InvoiceResponse)
def create_invoice(invoice_data: InvoiceCreate, db: Session = Depends(get_db)):
    return crud.create_invoice(db, invoice_data)

@app.get("/invoices/{invoice_id}", response_model=InvoiceResponse)
def read_invoice(invoice_id: int, db: Session = Depends(get_db)):
    invoice = crud.get_invoice(db, invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return invoice

@app.get("/invoices/", response_model=list[InvoiceResponse])
def read_invoices(db: Session = Depends(get_db)):
    return crud.get_invoices(db)

@app.put("/invoices/{invoice_id}", response_model=InvoiceResponse)
def update_invoice(invoice_id: int, invoice_data: InvoiceUpdate, db: Session = Depends(get_db)):
    invoice = crud.update_invoice(db, invoice_id, invoice_data)
    if not invoice:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return invoice

@app.delete("/invoices/{invoice_id}", response_model=InvoiceResponse)
def delete_invoice(invoice_id: int, db: Session = Depends(get_db)):
    invoice = crud.delete_invoice(db, invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return invoice
