# pylint: disable = invalid-name

from typing import Any, Iterator, Literal

# Referenced from https://gist.github.com/charbonnierg/b693316276e67fb02189548841830a34


class Empty:
    def __bool__(self) -> Literal[False]:
        return False

    def __str__(self) -> Literal["{}"]:
        return "{}"

    def __repr__(self) -> Literal["{}"]:
        return "{}"

    def __dict__(self) -> dict:
        return {}

    def __len__(self) -> Literal[0]:
        return 0

    def __contains__(self, _: Any) -> Literal[False]:
        return False

    def __iter__(self) -> Iterator[Any]:
        yield from ()

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if v:
            raise ValueError("Not empty")
        return cls()
