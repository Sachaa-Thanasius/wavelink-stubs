from collections.abc import Callable

class Backoff:
    _base: int
    _maximum_time: float
    _maximum_tries: int | None
    _retries: int
    _rand: Callable[[float, float], float]
    _last_wait: float

    def __init__(self, *, base: int = 1, maximum_time: float = 30.0, maximum_tries: int | None = 5) -> None: ...
    def calculate(self) -> float: ...
