import abc as __abc


class MemoryStoreBase(__abc.ABC):
    import abc as __abc

    @__abc.abstractmethod
    def get(self, key) -> any:
        pass

    @__abc.abstractmethod
    def set(self, key, value) -> None:
        pass

    @__abc.abstractmethod
    def delete(self, key) -> None:
        pass

    @__abc.abstractmethod
    def clear(self) -> None:
        pass

    @__abc.abstractmethod
    def __contains__(self, key) -> bool:
        pass

    @__abc.abstractmethod
    def __getitem__(self, key) -> any:
        pass

    @__abc.abstractmethod
    def __setitem__(self, key, value) -> None:
        pass
