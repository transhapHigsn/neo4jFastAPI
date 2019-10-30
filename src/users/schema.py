import re

from pydantic import BaseModel, validator
from typing_extensions import Literal
from typing import List, Optional

# FastAPI does not support latest pydantic version.
# As of now, FastAPI has following requirements pydantic<=0.32.2,>=0.32.2 
# this is probably added in later versions.
# from pydantic import HttpUrl


class Supplier(BaseModel):
	country: Literal['IN']
	contactTitle: Literal['Mr.', 'Ms.', 'Mrs.']
	address: str
	supplierID: str
	phone: str
	city: str
	contactName: str
	companyName: str
	postalCode: str
	region: Optional[str] = ""
	fax: Optional[str] = ""
	homePage: Optional[str] = ""


	@validator('supplierID')
	def check_supplier_id(cls, v):
		if not v.isdigit():
			raise ValueError('SupplierID can only be made up of digits.')
		return v

	@validator('postalCode')
	def check_postal_code(cls, v):
		if not v.isdigit():
			raise ValueError('Postal code can only be made up of digits.')
		
		if len(v) != 6:
			raise ValueError('Postal code can only be made up of six characters.')

		return v

	@validator('homePage')
	def validate_homepage(cls, v):
		if v == '':
			return v
		
		# Logic taken from following link.
		# https://stackoverflow.com/questions/7160737/python-how-to-validate-a-url-in-python-malformed-or-not
		regex = re.compile(
			r'^(?:http)s?://' # http:// or https://
			r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
			r'localhost|' #localhost...
			r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
			r'(?::\d+)?' # optional port
			r'(?:/?|[/?]\S+)$', re.IGNORECASE
		)

		if not re.match(regex, v):
			raise ValueError('Invalid home page url')

		return v


class Suppliers(BaseModel):
	suppliers: List[Supplier] = []