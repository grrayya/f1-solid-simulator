from abc import ABC, abstractmethod


class TireCompound(ABC):
    """Abstract base class. Open for extension, closed for modification.

    Any new compound only needs to implement calculate_wear() and
    lap_time_penalty() -- nothing in car.py or main.py ever needs to change.
    """

    name: str = "Unknown"

    @abstractmethod
    def calculate_wear(self, laps: int) -> float:
        """Cumulative wear (%) added after driving `laps` laps."""
        pass

    @abstractmethod
    def lap_time_penalty(self, current_wear: float) -> float:
        """Seconds lost per lap as a function of current tire wear (%)."""
        pass


class SoftTire(TireCompound):
    name = "Soft"

    def calculate_wear(self, laps: int) -> float:
        return laps * 3.5  # Degrades very quickly

    def lap_time_penalty(self, current_wear: float) -> float:
        # Soft tires have great initial grip but fall off a cliff late on
        return current_wear * 0.035


class HardTire(TireCompound):
    name = "Hard"

    def calculate_wear(self, laps: int) -> float:
        return laps * 1.2  # Lasts much longer

    def lap_time_penalty(self, current_wear: float) -> float:
        # Hards degrade slowly and predictably
        return current_wear * 0.015


class IntermediateTire(TireCompound):
    """Added purely to prove OCP: zero changes were needed elsewhere."""

    name = "Intermediate"

    def calculate_wear(self, laps: int) -> float:
        return laps * 2.0

    def lap_time_penalty(self, current_wear: float) -> float:
        return current_wear * 0.025


class WetTire(TireCompound):
    """Also added purely to prove OCP."""

    name = "Wet"

    def calculate_wear(self, laps: int) -> float:
        return laps * 1.5

    def lap_time_penalty(self, current_wear: float) -> float:
        return current_wear * 0.02
