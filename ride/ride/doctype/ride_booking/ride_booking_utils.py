import frappe
from frappe.utils import flt,getdate

def calculate_total_amount(doc):
    total_amount = sum( [ flt(service.amount,3) for service in doc.services])

    doc.total_amount = (flt(doc.price_per_kilometer,3) * flt(doc.estimated_km,3)) + total_amount    
    doc.booking_date = getdate()