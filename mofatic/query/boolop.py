import dataclasses
import enum
import typing

from mofatic.query.base import BaseFieldRule


class LogicalType(str, enum.Enum):
    AND = "$and"
    OR = "$or"


@dataclasses.dataclass
class BinaryFieldRule(
    BaseFieldRule[
        typing.List[BaseFieldRule]
    ]
):
    filter_name: LogicalType

    def represent(self) -> typing.Any:
        return {self.name: {self.filter_name.value: [rule.represent() for rule in self.value]}}


class NotFieldRule(BaseFieldRule[BaseFieldRule]):
    def represent(self) -> typing.Any:
        return {self.name: {"$not": self.value.represent()}}