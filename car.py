from abc import ABC, abstractmethod
from tires import TireCompound

class Vehicle(ABC):
    """Abstract base class for anything on the track."""
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_status(self) -> str:
        pass


class F1Car(Vehicle):
    """An active race car. Fully substitutable as a Vehicle."""
    def __init__(self, driver_name: str, tire: TireCompound):
        super().__init__(driver_name)  # Pass driver_name to the Vehicle base class
        self.tire = tire
        self.total_wear = 0.0

    def drive_stint(self, laps: int) -> str:
        wear = self.tire.calculate_wear(laps)
        self.total_wear += wear
        return f"{self.name} drove {laps} laps. Tire wear increased by {wear}%. Total wear: {self.total_wear}%"

    def get_status(self) -> str:
        return f"Race Car ({self.name}) | Tire Wear: {self.total_wear}%"


class SafetyCar(Vehicle):
    """The safety car. Fully substitutable as a Vehicle, even without tires to wear down."""
    def get_status(self) -> str:
        return f"Safety Car ({self.name}) | Deployed on track controlling the race pace."
