
from fastapi import APIRouter
from starlette.responses import JSONResponse

from db import run_get_query
from users.schema import Suppliers

users_route = APIRouter()


@users_route.get(
	'/get_all_suppliers',
	response_model=Suppliers,
	status_code=200,
	tags=['Suppliers'],
	summary="Get info about all suppliers",
	description="Get all information such as company, fax, homepage, etc., of all suppliers registered in system."
	)
def get_all_suppliers():
	result = run_get_query("""MATCH (n:Supplier) RETURN n""")

	suppliers = [dict(i['n']) for i in result]
	return JSONResponse(content={'suppliers': suppliers})