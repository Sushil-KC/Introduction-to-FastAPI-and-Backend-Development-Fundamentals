
from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
app = FastAPI()

@app.get("/")
def get_shipment():
    return {
        "content": "Sushil KC",
        "status": "In transit"
    }


@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )
# pip install scalar_fastapi
# http://127.0.0.1:8000/docs  API Documentation 

