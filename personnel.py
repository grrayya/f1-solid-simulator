from abc import ABC, abstractmethod

# --- Segregated Interfaces ---
class IPitCrew(ABC):
    """Interface strictly for physical car maintenance."""
    @abstractmethod
    def change_tires(self, car) -> str:
        pass

class IRaceEngineer(ABC):
    """Interface strictly for driver communication and strategy."""
    @abstractmethod
    def give_radio_comms(self, message: str) -> str:
        pass

# --- Concrete Classes ---
class Mechanic(IPitCrew):
    def change_tires(self, car) -> str:
        # The mechanic doesn't have to implement a useless radio method
        return f"Mechanic completed a 2.1s pit stop for {car.name}."

class ChiefEngineer(IRaceEngineer):
    def __init__(self, name: str):
        self.name = name

    def give_radio_comms(self, message: str) -> str:
        # The engineer doesn't have to implement a useless tire-changing method
        return f"Radio ({self.name}): '{message}'"
