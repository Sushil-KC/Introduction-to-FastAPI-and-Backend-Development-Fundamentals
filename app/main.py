
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_shipment():
    return {
        "content": "Sushil KC",
        "status": "In transit"
    }

# Run User: fastapi dev