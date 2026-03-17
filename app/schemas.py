from pydantic import BaseModel, Field
from random import randint
from enum import Enum

def random_destination():
    return randint(11000, 12000)

class Shipment(BaseModel):
    content: str = Field(max_length=20, )
    weight: float = Field(lt=25, description="Weight of the shipment in KG")  # Less than equal = le, Grater than equal = ge,
    status: str | None = Field(default='Placed')

    # destination: int | None = Field(default=random_destination())
    # destination: int | None = Field(default=randint(11000, 12000))

class BaseShipment(BaseModel):
    content: str = Field(max_length=20, )
    weight: float = Field(lt=25, description="Weight of the shipment in KG")
    
class ShipmentStatus(str, Enum):
    placed="placed"
    in_transit="in_transit"
    out_for_delivery = "out_for_delivery"
    delivery = "delivery"

class ShipmentRead(BaseShipment):
    status: str | None = Field(default='Placed')

class ShipmentCreate(BaseShipment):
    status: str | None = Field(default='Placed')

class ShipmentUpdate(BaseModel):
    status: ShipmentStatus