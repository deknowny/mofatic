import typing

from mofatic.query.base import BaseFieldRule


class NestedFieldRule(BaseFieldRule[BaseFieldRule]):
    def represent(self) -> typing.Any:
        return {self.name: self.value.represent()}