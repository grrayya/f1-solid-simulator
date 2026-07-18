from abc import ABC, abstractmethod


class IEngine(ABC):
    @abstractmethod
    def get_power_output(self) -> str:
        pass


class HondaEngine(IEngine):
    def get_power_output(self) -> str:
        return "Honda RBPT (1000 HP)"


class MercedesEngine(IEngine):
    def get_power_output(self) -> str:
        return "Mercedes-AMG Power Unit (1010 HP)"
