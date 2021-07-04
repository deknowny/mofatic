import dataclasses
import enum
import typing

from mofatic.query.base import BaseFieldRule


class ComparisonType(str, enum.Enum):
    EQ = "$eq"
    GT = "$gt"
    GTE = "$gte"
    IN = "$in"
    LT = "$lt"
    LTE = "$lte"
    NE = "$ne"
    NIN = "$nin"


@dataclasses.dataclass
class BaseComparisonFieldRule(BaseFieldRule[int]):
    filter_name: ComparisonType

    def represent(self) -> typing.Any:
        return {self.name: {self.filter_name.value: self.value}}
