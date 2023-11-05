import abc
from typing import Any, ClassVar, Final, TypeVar
from typing_extensions import Self

from discord.ext import commands

from .enums import TrackSource
from .node import Node
from .types.track import Track as TrackPayload

__all__ = (
    "Playable",
    "Playlist",
    "YouTubeTrack",
    "GenericTrack",
    "YouTubeMusicTrack",
    "SoundCloudTrack",
    "YouTubePlaylist",
    "SoundCloudPlaylist",
)

_BotT_co = TypeVar("_BotT_co", bound=commands.Bot | commands.AutoShardedBot, covariant=True)

_source_mapping: Final[dict[str, TrackSource]]

class Playlist(abc.ABC):
    data: dict[str, Any]
    def __init__(self, data: dict[str, Any]) -> None: ...

class Playable(abc.ABC):
    PREFIX: ClassVar[str] = ""
    data: TrackPayload
    encoded: str
    is_seekable: bool
    is_stream: bool
    length: int
    duration: int
    position: int
    title: str
    source: TrackSource
    uri: str | None
    author: str | None
    identifier: str | None

    def __init__(self, data: TrackPayload) -> None: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    @classmethod
    async def search(
        cls,
        query: str,
        /,
        *,
        node: Node | None = None,
    ) -> YouTubePlaylist | SoundCloudPlaylist | list[Self]: ...
    @classmethod
    async def convert(
        cls,
        ctx: commands.Context[_BotT_co],
        argument: str,
    ) -> YouTubePlaylist | SoundCloudPlaylist | Self: ...

class GenericTrack(Playable): ...

class YouTubeTrack(Playable):
    PREFIX: ClassVar[str] = "ytsearch:"
    _thumb: str

    @property
    def thumbnail(self) -> str: ...
    @property
    def thumb(self) -> str: ...
    async def fetch_thumbnail(self, *, node: Node | None = None) -> str: ...

class YouTubeMusicTrack(YouTubeTrack):
    PREFIX: ClassVar[str] = "ytmsearch:"

class SoundCloudTrack(Playable):
    PREFIX: ClassVar[str] = "scsearch:"

class YouTubePlaylist(Playable, Playlist):
    PREFIX: ClassVar[str] = "ytpl:"
    data: dict[str, Any]  # type: ignore # Override Playable's data attribute.
    tracks: list[YouTubeTrack]
    name: str
    selected_track: int | None
    source: TrackSource

    def __init__(self, data: dict[str, Any]) -> None: ...
    def __str__(self) -> str: ...

class SoundCloudPlaylist(Playable, Playlist):
    data: dict[str, Any]  # type: ignore # Override Playable's data attribute.
    tracks: list[YouTubeTrack]
    name: str
    selected_track: int | None
    source: TrackSource

    def __init__(self, data: dict[str, Any]) -> None: ...
    def __str__(self) -> str: ...
