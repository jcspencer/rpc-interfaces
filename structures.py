from enum import Enum

from typing import List, NamedTuple, Optional

class RpcService:
    id: str
    path: List[str]
    name: str
    description: str

    def __init__(
        self,
        id: str,
        path: List[str],
        name: str,
        description: str
    ):
        self.id = id
        self.path = path
        self.name = name
        self.description = description

class RpcUuid:
    uuid: str
    name: Optional[str] = None
    undocumented: bool = False

    def __init__(
        self,
        uuid: str,
        name: Optional[str] = None,
        undocumented: bool = False
    ):
        self.uuid = uuid
        self.name = name
        self.undocumented = undocumented

class RpcNamedPipe:
    path: str
    description: Optional[str] = None
    undocumented: bool = False

    def __init__(
        self,
        path: str,
        description: Optional[str] = None,
        undocumented: bool = False
    ):
        self.path = path
        self.description = description
        self.undocumented = undocumented

class RpcProfileType(str, Enum):
    CORE = 'core'
    REMOTE_MANAGEMENT = 'remote_management'
    HYBRID = 'hybrid'

class RpcInterfaceProfile:
    service_id: str
    type: RpcProfileType

    def __init__(
        self,
        service: RpcService,
        type: RpcProfileType
    ):
        self.service_id = service.id
        self.type = type

class RpcInterfaceMetadata:
    name: str
    description: str
    url: str
    security_notes: List[str] = []

    def __init__(
        self,
        name: str,
        description: str,
        url: str = None,
        security_notes: List[str] = []
    ):
        self.name = name
        self.description = description
        self.url = url
        self.security_notes = security_notes

class RpcInterfaceDefinition:
    id: str
    metadata: RpcInterfaceMetadata
    profiles: List[RpcInterfaceProfile]
    uuids: List[RpcUuid]
    named_pipes: List[RpcNamedPipe]

    def __init__(
        self,
        id: str,
        metadata: RpcInterfaceMetadata,
        profiles: List[RpcInterfaceProfile] = [],
        uuids: List[RpcUuid] = [],
        named_pipes: List[RpcNamedPipe] = [],
    ):
        self.id = id
        self.metadata = metadata
        self.profiles = profiles
        self.uuids = uuids
        self.named_pipes = named_pipes