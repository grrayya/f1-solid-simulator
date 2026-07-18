from abc import ABC, abstractmethod
from tires import TireCompound
from engine import IEngine

BASE_LAP_TIME = 90.0  # seconds, rough dry-race baseline lap


class Vehicle(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_status(self) -> str:
        pass


class F1Car(Vehicle):
    def __init__(self, driver_name: str, tire: TireCompound, engine: IEngine):
        super().__init__(driver_name)
        self.tire = tire
        self.engine = engine
        self.total_wear = 0.0
        self.total_race_time = 0.0

    def drive_stint(self, laps: int, caution: bool = False) -> str:
        """Drive a stint, accumulating wear and lap time.

        Under caution (VSC/SC) the field runs at a controlled pace, so both
        wear and the lap-time penalty get dialed back rather than zeroed out.
        """
        wear_multiplier = 0.4 if caution else 1.0
        wear = self.tire.calculate_wear(laps) * wear_multiplier
        self.total_wear += wear

        penalty_per_lap = self.tire.lap_time_penalty(self.total_wear)
        lap_time = BASE_LAP_TIME + penalty_per_lap
        if caution:
            lap_time *= 1.3
        stint_time = lap_time * laps
        self.total_race_time += stint_time

        flag = " [under caution]" if caution else ""
        return (
            f"{self.name} drove {laps} laps on {self.tire.name} tires using "
            f"{self.engine.get_power_output()}{flag}. "
            f"Stint time: {stint_time:.1f}s | Total wear: {self.total_wear:.1f}% | "
            f"Total race time: {self.total_race_time:.1f}s"
        )

    def get_status(self) -> str:
        return (
            f"Race Car ({self.name}) | Tire Wear: {self.total_wear:.1f}% | "
            f"Total Time: {self.total_race_time:.1f}s"
        )


class SafetyCar(Vehicle):
    def get_status(self) -> str:
        return f"Safety Car ({self.name}) | Deployed on track."
