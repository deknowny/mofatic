import datetime

import pydantic


class Leaf(pydantic.BaseModel):
    color: int
    size: float


class Tree(pydantic.BaseModel):
    trunk_radius: float
    height: int
    width: int
    planted_date: datetime.datetime
    leaves: list[Leaf] = pydantic.Field(reference=True)  # Stored as list of ObjectID
