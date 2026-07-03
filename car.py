from abc import ABC, abstractmethod
from tires import TireCompound
from engine import IEngine  # Import the abstraction

class Vehicle(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_status(self) -> str:
        pass


class F1Car(Vehicle):
    # Notice we ask for an IEngine here! This is Dependency Injection.
    def __init__(self, driver_name: str, tire: TireCompound, engine: IEngine):
        super().__init__(driver_name)
        self.tire = tire
        self.engine = engine 
        self.total_wear = 0.0

    def drive_stint(self, laps: int) -> str:
        wear = self.tire.calculate_wear(laps)
        self.total_wear += wear
        # The car uses the engine without needing to know what brand it is
        return f"{self.name} drove {laps} laps using {self.engine.get_power_output()}. Total wear: {self.total_wear}%"

    def get_status(self) -> str:
        return f"Race Car ({self.name}) | Tire Wear: {self.total_wear}%"


class SafetyCar(Vehicle):
    def get_status(self) -> str:
        return f"Safety Car ({self.name}) | Deployed on track."
