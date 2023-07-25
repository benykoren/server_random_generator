from typing import ClassVar as _ClassVar, Optional as _Optional

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class RandomRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RandomReply(_message.Message):
    __slots__ = ["random_number"]
    RANDOM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    random_number: int
    def __init__(self, random_number: _Optional[int] = ...) -> None: ...
