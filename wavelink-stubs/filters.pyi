import abc
from typing import Any
from typing_extensions import Self

__all__ = (
    "BaseFilter",
    "Equalizer",
    "Karaoke",
    "Timescale",
    "Tremolo",
    "Vibrato",
    "Rotation",
    "Distortion",
    "ChannelMix",
    "LowPass",
    "Filter",
)

class BaseFilter(abc.ABC):
    name: str
    def __init__(self, name: str | None = None) -> None: ...
    def __repr__(self) -> str: ...
    @property
    @abc.abstractmethod
    def _payload(self) -> Any: ...

class Equalizer(BaseFilter):
    bands: list[dict[str, float]]
    def __init__(self, name: str = ..., *, bands: list[tuple[int, float]]) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def _payload(self) -> list[dict[str, float]]: ...
    @classmethod
    def flat(cls) -> Self: ...
    @classmethod
    def boost(cls) -> Self: ...
    @classmethod
    def metal(cls) -> Self: ...
    @classmethod
    def piano(cls) -> Self: ...

class Karaoke(BaseFilter):
    """
    A Karaoke filter.

    The default values provided for all the parameters will play the track normally.

    Parameters
    ----------
    level: float
        How much of an effect this filter should have.
    mono_level: float
        How much of an effect this filter should have on mono tracks.
    filter_band: float
        The band this filter should target.
    filter_width: float
        The width of the band this filter should target.
    """

    level: float
    mono_level: float
    filter_band: float
    filter_width: float

    def __init__(
        self,
        *,
        level: float = ...,
        mono_level: float = ...,
        filter_band: float = ...,
        filter_width: float = ...,
    ) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def _payload(self) -> dict[str, float]: ...

class Timescale(BaseFilter):
    speed: float
    pitch: float
    rate: float

    def __init__(self, *, speed: float = ..., pitch: float = ..., rate: float = ...) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def _payload(self) -> dict[str, float]: ...

class Tremolo(BaseFilter):
    frequency: float
    depth: float
    def __init__(self, *, frequency: float = ..., depth: float = ...) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def _payload(self) -> dict[str, float]: ...

class Vibrato(BaseFilter):
    frequency: float
    depth: float

    def __init__(self, *, frequency: float = ..., depth: float = ...) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def _payload(self) -> dict[str, float]: ...

class Rotation(BaseFilter):
    speed: float

    def __init__(self, speed: float = 5) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def _payload(self) -> dict[str, float]: ...

class Distortion(BaseFilter):
    sin_offset: float
    sin_scale: float
    cos_offset: float
    cos_scale: float
    tan_offset: float
    tan_scale: float
    offset: float
    scale: float

    def __init__(
        self,
        *,
        sin_offset: float = ...,
        sin_scale: float = ...,
        cos_offset: float = ...,
        cos_scale: float = ...,
        tan_offset: float = ...,
        tan_scale: float = ...,
        offset: float = ...,
        scale: float = ...,
    ) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def _payload(self) -> dict[str, float]: ...

class ChannelMix(BaseFilter):
    """A channel mix filter.

    Allows you to control what channel audio from the track is actually played on.

    Setting `left_to_left` and `right_to_right` to 1.0 will result in no change.
    Setting all channels to 0.5 will result in all channels receiving the same audio.

    The default values provided for all the parameters will play the track normally.

    Parameters
    ----------
    left_to_left: float
        The "percentage" of audio from the left channel that should actually get played on the left channel.
    left_to_right: float
        The "percentage" of audio from the left channel that should play on the right channel.
    right_to_left: float
        The "percentage" of audio from the right channel that should actually get played on the right channel.
    right_to_right: float
        The "percentage" of audio from the right channel that should play on the left channel.
    """

    left_to_left: float
    right_to_right: float
    left_to_right: float
    right_to_left: float

    def __init__(
        self,
        *,
        left_to_left: float = ...,
        left_to_right: float = ...,
        right_to_left: float = ...,
        right_to_right: float = ...,
    ) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def _payload(self) -> dict[str, float]: ...
    @classmethod
    def mono(cls) -> Self: ...
    @classmethod
    def only_left(cls) -> Self: ...
    @classmethod
    def full_left(cls) -> Self: ...
    @classmethod
    def only_right(cls) -> Self: ...
    @classmethod
    def full_right(cls) -> Self: ...
    @classmethod
    def switch(cls) -> Self: ...

class LowPass(BaseFilter):
    smoothing: float

    def __init__(self, *, smoothing: float = ...) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def _payload(self) -> dict[str, float]: ...

class Filter:
    filter: Filter | None
    equalizer: Equalizer | None
    karaoke: Karaoke | None
    timescale: Timescale | None
    tremolo: Tremolo | None
    vibrato: Vibrato | None
    rotation: Rotation | None
    distortion: Distortion | None
    channel_mix: ChannelMix | None
    low_pass: LowPass | None

    def __init__(
        self,
        _filter: Filter | None = ...,
        /,
        *,
        equalizer: Equalizer | None = ...,
        karaoke: Karaoke | None = ...,
        timescale: Timescale | None = ...,
        tremolo: Tremolo | None = ...,
        vibrato: Vibrato | None = ...,
        rotation: Rotation | None = ...,
        distortion: Distortion | None = ...,
        channel_mix: ChannelMix | None = ...,
        low_pass: LowPass | None = ...,
    ) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def _payload(self) -> dict[str, Any]: ...
