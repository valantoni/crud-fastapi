from sqlalchemy.orm import Session
from app.models import Invoice
from app.schema import InvoiceCreate, InvoiceUpdate

# Crear una nueva factura
def create_invoice(db: Session, invoice_data: InvoiceCreate):
    new_invoice = Invoice(**invoice_data.model_dump())
    db.add(new_invoice)
    db.commit()
    db.refresh(new_invoice)
    return new_invoice

# Obtener una factura por ID
def get_invoice(db: Session, invoice_id: int):
    return db.query(Invoice).filter(Invoice.id == invoice_id).first()

# Obtener todas las facturas
def get_invoices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Invoice).offset(skip).limit(limit).all()

# Actualizar una factura por ID
def update_invoice(db: Session, invoice_id: int, invoice_data: InvoiceUpdate):
    invoice = get_invoice(db, invoice_id)
    if not invoice:
        return None
    for field, value in invoice_data.model_dump(exclude_unset=True).items():
        setattr(invoice, field, value)
    db.commit()
    db.refresh(invoice)
    return invoice

# Eliminar una factura por ID
def delete_invoice(db: Session, invoice_id: int):
    invoice = get_invoice(db, invoice_id)
    if not invoice:
        return None
    db.delete(invoice)
    db.commit()
    return invoice
