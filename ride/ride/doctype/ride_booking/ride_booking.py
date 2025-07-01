# Copyright (c) 2025, Sanskar Technolab and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime
from frappe.model.naming import make_autoname

from frappe.model.document import Document
from . ride_booking_utils import calculate_total_amount

class RideBooking(Document):
	def before_validate(self):
		calculate_total_amount(self)

	def autoname(self):
		if not self.vechicle:
			frappe.throw("Vehicle field is required for naming.")

		current_year = datetime.now().year
		prefix = f"{self.vechicle}-{current_year}-"
		
		self.name = make_autoname(f"{prefix}.####")

