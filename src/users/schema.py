from pydantic import BaseModel
from typing import List

class Supplier(BaseModel):
	country: str
	contactTitle: str
	address: str
	supplierID: str
	phone: str
	city: str
	contactName: str
	companyName: str
	postalCode: str
	region: str = ""
	fax: str = ""
	homePage: str = ""

class Suppliers(BaseModel):
	suppliers: List[Supplier] = []