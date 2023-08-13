import typing as __typing

__T = __typing.TypeVar("__T")


class ServiceRegistry(__typing.Generic[__T]):
    import typing as __typing

    __T = __typing.TypeVar("__T")

    default_service_name: str = None
    services: dict[str, __T] = {}

    def register(self, name: str, service: __T) -> None:
        if name in self.services:
            raise ValueError(
                f"Service {name} already registered. Attempted to register {service}"
            )
        if not self.default_service_name:
            self.default_service_name = name
        self.services[name] = service

    def unregister(self, name: str) -> None:
        if self.default_service_name == name:
            self.default_service_name = None
        del self.services[name]

    def get(self, name: str) -> __T:
        return self.services.get(name)

    def get_default(self) -> __T:
        return self.get(self.default_service_name)

    @property
    def default(self) -> __T:
        return self.get_default()

    def __getitem__(self, name: str) -> __T:
        return self.get(name)

    def __setitem__(self, name: str, service: __T) -> None:
        self.register(name, service)

    def __contains__(self, name: str) -> bool:
        return name in self.services

    def __iter__(self) -> __typing.Iterator[str]:
        return iter(self.services)

    def __len__(self) -> int:
        return len(self.services)

    def __repr__(self) -> str:
        return f"<ServiceRegistry {self.services}>"

    def __str__(self) -> str:
        return repr(self)
