from abc import ABC, abstractmethod


class TireCompound(ABC):
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
        return laps * 3.5

    def lap_time_penalty(self, current_wear: float) -> float:
        # drops off hard past ~70% wear
        if current_wear > 70:
            return current_wear * 0.035 + (current_wear - 70) * 0.05
        return current_wear * 0.035


class HardTire(TireCompound):
    name = "Hard"

    def calculate_wear(self, laps: int) -> float:
        return laps * 1.2

    def lap_time_penalty(self, current_wear: float) -> float:
        return current_wear * 0.015


class IntermediateTire(TireCompound):
    name = "Intermediate"

    def calculate_wear(self, laps: int) -> float:
        return laps * 2.0

    def lap_time_penalty(self, current_wear: float) -> float:
        return current_wear * 0.025


class WetTire(TireCompound):
    name = "Wet"

    def calculate_wear(self, laps: int) -> float:
        return laps * 1.5

    def lap_time_penalty(self, current_wear: float) -> float:
        return current_wear * 0.02
