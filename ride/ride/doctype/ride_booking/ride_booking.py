# Copyright (c) 2025, Sanskar Technolab and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.utils import y
from . ride_booking_utils import calculate_total_amount

class RideBooking(Document):
	def before_validate(self):
		calculate_total_amount(self)

