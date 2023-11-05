from discord.types.voice import GuildVoiceState, VoiceServerUpdate
from typing import TypedDict
from typing_extensions import NotRequired

class VoiceState(TypedDict):
    token: str
    endpoint: str
    sessionId: str
    connected: NotRequired[bool]
    ping: NotRequired[int]

class DiscordVoiceState(GuildVoiceState, VoiceServerUpdate): ...
