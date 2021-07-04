import dataclasses
import typing

import pydantic
import motor


@dataclasses.dataclass
class Engine:
    driver: motor.MotorDatabase

    async def find_one(self, collection: pydantic.BaseModel, filter: typing.Callable[[], bool], /):
        pass