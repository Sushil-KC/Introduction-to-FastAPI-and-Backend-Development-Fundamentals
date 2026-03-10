from pydantic import BaseModel, Field
from random import randint

def random_destination():
    return randint(11000, 12000)

class Shipment(BaseModel):
    content: str = Field(max_length=20, )
    weight: float = Field(lt=25, description="Weight of the shipment in KG")  # Less than equal = le, Grater than equal = ge,
    status: str | None = Field(default='Placed')

    # destination: int | None = Field(default=random_destination())
    # destination: int | None = Field(default=randint(11000, 12000))