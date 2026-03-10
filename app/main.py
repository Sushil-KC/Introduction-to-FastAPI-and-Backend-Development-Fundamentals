
from fastapi import FastAPI, status, HTTPException
from scalar_fastapi import get_scalar_api_reference
app = FastAPI()

# Sample shipment database with 20 diverse records
shipments = {
    # ID: {weight, content, status}
    10001: {"weight": 5, "content": "Electronics", "status": "Delivered"},
    10002: {"weight": 12, "content": "Furniture", "status": "In transit"},
    10003: {"weight": 3, "content": "Books", "status": "Placed"},
    10004: {"weight": 8, "content": "Clothing", "status": "Processing"},
    10005: {"weight": 15, "content": "Machinery", "status": "In transit"},
    10006: {"weight": 2, "content": "Documents", "status": "Delivered"},
    10007: {"weight": 25, "content": "Auto parts", "status": "Placed"},
    10008: {"weight": 7, "content": "Medical supplies", "status": "Processing"},
    10009: {"weight": 4, "content": "Perishables", "status": "In transit"},
    10010: {"weight": 18, "content": "Building materials", "status": "Placed"},
    10011: {"weight": 9, "content": "Chemicals", "status": "Processing"},
    10012: {"weight": 11, "content": "Textiles", "status": "Delivered"},
    10013: {"weight": 6, "content": "Glassware", "status": "Placed"},
    10014: {"weight": 22, "content": "Heavy equipment", "status": "In transit"},
    10015: {"weight": 3, "content": "Pharmaceuticals", "status": "Processing"},
    10016: {"weight": 14, "content": "Food products", "status": "Delivered"},
    10017: {"weight": 8, "content": "Cosmetics", "status": "Placed"},
    10018: {"weight": 19, "content": "Metal parts", "status": "In transit"},
    10019: {"weight": 5, "content": "Software", "status": "Delivered"},
    10020: {"weight": 16, "content": "Sporting goods", "status": "Processing"}
}

@app.get("/")
def get_shipment():
    return {
        "content": "Sushil KC",
        "status": "In transit"
    }

@app.get("/shipments/latest")
def get_shipment_with_params() -> dict[str, str | int]:
    id = max(shipments.keys())
    return shipments[id]

@app.get("/shipments/{id}")
def get_shipment_with_params(id: int) -> dict[str, str | int]:
    if id not in shipments:
        return {"details": "Id doesnot exists"}
    return shipments[id]

# # ✅ CORRECT: Static routes first
# @app.get("/shipments/latest")      # Static - checked first
# @app.get("/shipments/stats")        # Static - checked first  
# @app.get("/shipments/{id}")         # Dynamic - checked after
# @app.get("/shipments/{id}/items")   # Dynamic - more specific


# ❌ AVOID: This creates ambiguity
# @app.get("/items/{id}")
# @app.get("/items/latest")  # "latest" could be an ID

# # ✅ BETTER: Use distinct paths
# @app.get("/items/latest")
# @app.get("/items/{item_id}")

# Query Parameters
@app.get('/shipments', )
def get_query_params(id: int) -> dict[str, str | int]:
    print("Sushil")
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id doesnot exists"
        )
    return shipments[id]


















@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )
# pip install scalar_fastapi
# http://127.0.0.1:8000/docs  API Documentation 

