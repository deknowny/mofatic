import abc
import dataclasses
import typing


FilterParameter = typing.TypeVar("FilterParameter")


@dataclasses.dataclass
class BaseFieldRule(typing.Generic[FilterParameter], abc.ABC):
    name: str
    value: FilterParameter

    @abc.abstractmethod
    def represent(self) -> typing.Any:
        pass

