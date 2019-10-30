
from fastapi import APIRouter
from starlette.responses import JSONResponse

from db import run_get_query, run_post_query
from suppliers.schema import Suppliers, Supplier

supplier_route = APIRouter()


@supplier_route.get(
	'/get_all',
	response_model=Suppliers,
	status_code=200,
	summary="Get info about all suppliers",
	description="Get all information such as company, fax, homepage, etc., of all suppliers registered in system."
	)
def get_all_suppliers():
	result = run_get_query("""MATCH (n:Supplier) RETURN n""")
	suppliers = [dict(i['n']) for i in result]
	return JSONResponse(content={'suppliers': suppliers})


@supplier_route.post('/create', response_model=Supplier, status_code=201)
def create_new_supplier(supplier: Supplier):
	query = """
		CREATE (n:Supplier {
			contactName: $contactName,
			contactTitle: $contactTitle,
			country: $country,
			address: $address,
			supplierID: $supplierID,
			phone: $phone,
			city: $city,
			companyName: $companyName,
			postalCode: $postalCode,
			region: $region,
			fax: $fax,
			homePage: $homePage
		})
		RETURN n.supplierID
	"""
	run_post_query(query, dict(supplier))
	return JSONResponse(content={'supplier': dict(supplier)})
