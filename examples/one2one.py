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
    leaves: Leaf = pydantic.Field(reference=True)  # Stored as ObjectID
