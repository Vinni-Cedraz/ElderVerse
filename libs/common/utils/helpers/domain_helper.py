from typing import Optional, TypeVar, Generic
from uuid import uuid5

T = TypeVar("T")


class Domain(Generic[T]):
    def __init__(self, id: Optional[T] = None):
        self.id = id


class Entity:

    @staticmethod
    def generate_uuid(base_id: str) -> str:
        return str(uuid5("namespace", base_id))
