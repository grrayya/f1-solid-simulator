from abc import ABC, abstractmethod

# --- The Abstraction ---
class IEngine(ABC):
    """Abstract interface that both the F1Car and the concrete engines depend on."""
    @abstractmethod
    def get_power_output(self) -> str:
        pass

# --- Low-Level Concrete Modules ---
class HondaEngine(IEngine):
    def get_power_output(self) -> str:
        return "Honda RBPT (1000 HP)"

class MercedesEngine(IEngine):
    def get_power_output(self) -> str:
        return "Mercedes-AMG Power Unit (1010 HP)"
