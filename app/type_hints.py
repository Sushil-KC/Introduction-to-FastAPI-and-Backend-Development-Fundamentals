from typing import Any
text: str = "Value"

pert: float = 10.2
temp: float = 37.5
file:bytes

number: int | float = 10
value:str = "Sushil KC"
value.capitalize()


digits: list[int] = [1, 2, 3, 4]
tuples: tuple[int, ...] = (10, 20, 30)

city_temp: tuple[str, float] = ("City", 10.5)

shipment: dict[str, Any] = {
    "id": 12701,
    "weight": 12.2,
    "content": "Wooden table",
    "status": "In Transit"
}
def root(num: int | float) ->int:
    return pow(num, 0.5)

root(10)