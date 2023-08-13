from totallylit.api.memory import MemoryStoreBase
from totallylit.api.services import ServiceRegistry

memory_service_registry = ServiceRegistry[MemoryStoreBase]()
