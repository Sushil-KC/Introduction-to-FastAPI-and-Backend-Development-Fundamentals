
from fastapi import FastAPI, status, HTTPException
from scalar_fastapi import get_scalar_api_reference
from typing import Any
from schemas import Shipment, ShipmentStatus, ShipmentRead, ShipmentCreate, ShipmentUpdate


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
@app.get('/shipments', response_model=ShipmentRead)
def get_query_params(id: int) -> dict[str, str | int]:
    print("Sushil")
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id doesnot exists"
        )
    return shipments[id]

# POST Method
# @app.post('/shipment')
# def submit_shipment(content: str, weight: float) ->dict[str, Any]:
#     if weight > 25:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Weight is less than 25")
#     new_id = max(shipments.keys()) +1
#     shipments[new_id]={
#         "content": content,
#         "weight": weight,
#         "status": "Placed"
#     }
#     return {"id": new_id}

# Request Body
@app.post('/shipment')
def submit_shipment(shipment: ShipmentCreate) ->dict[str, Any]:
    new_id = max(shipments.keys()) +1
    shipments[new_id]={
        "content": shipment.content,
        "weight": shipment.weight,
        "status": shipment.status
    }
    return {"id": new_id}

# Path & Query Parameters
@app.get('/shipment/{field}')
def get_shipment_field(field: str, id:int)->dict[str, Any]:
    return {
        field: shipments[id][field]
    }

# Update
@app.put("/shipment-update/{id}")
def shipment_update(id: int, content: str, weight: float, status: str)->dict[str, Any]:
    shipments[id]={
        "content": content,
        "weight": weight,
        "status": status
    }
    return shipments[id]


# @app.patch('/shipment')
# def patch_shipment(id: int, content: str | None=None, weight: float | None=None, status: str | None=None):
#     shipment = shipments[id]
#     # update the provide Fields
#     if content:
#         shipment["content"] = content
#     if weight:
#         shipment["weight"] = weight
#     if status:
#         shipment["status"] = status
    
#     shipments[id] = shipment
#     return shipment


@app.patch('/shipment', response_model=ShipmentRead)
def patch_shipment(id: int, body: ShipmentUpdate):
    # update the provide Fields
    shipments[id].update(body)
    return shipments[id]

@app.delete("/shipment")
def delete_shipment(id: int) ->dict[str, Any]:
    shipments.pop(id)
    return {"detail": f"Shipment with id {id} is deleted"}

@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )
# pip install scalar_fastapi
# http://127.0.0.1:8000/docs  API Documentation 

