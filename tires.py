from abc import ABC, abstractmethod

class TireCompound(ABC):
    """Abstract base class. Open for extension, closed for modification."""
    @abstractmethod
    def calculate_wear(self, laps: int) -> float:
        pass

class SoftTire(TireCompound):
    def calculate_wear(self, laps: int) -> float:
        return laps * 3.5  # Degrades very quickly

class HardTire(TireCompound):
    def calculate_wear(self, laps: int) -> float:
        return laps * 1.2  # Lasts much longer
