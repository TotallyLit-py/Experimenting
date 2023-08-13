# TODO: move this stuff because lit.memory is its own thing!

from totallylit.api.memory import MemoryStoreBase as __MemoryStoreBase

from .MemoryServiceRegistry import memory_service_registry as __memory_service_registry


def register_memory_service(store: __MemoryStoreBase, name: str = "default") -> None:
    __memory_service_registry.register(name, store)


# TODO figure this out ... rename, etc ... this is a hack to test
class GetDefaultMemoryService:
    from totallylit.api.memory import MemoryStoreBase as __MemoryStoreBase

    @property
    def memory(self) -> __MemoryStoreBase:
        from .MemoryServiceRegistry import (
            memory_service_registry as __memory_service_registry,
        )

        return __memory_service_registry.get_default()


get_default_memory_service_instance = GetDefaultMemoryService()
