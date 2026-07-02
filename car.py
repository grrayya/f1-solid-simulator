from tires import TireCompound

class F1Car:
    """Handles only the car's state and track behavior."""
    def __init__(self, driver_name: str, tire: TireCompound):
        self.driver_name = driver_name
        self.tire = tire
        self.total_wear = 0.0

    def drive_stint(self, laps: int) -> str:
        # The car trusts the tire to calculate its own wear
        wear = self.tire.calculate_wear(laps)
        self.total_wear += wear
        return f"{self.driver_name} drove {laps} laps. Tire wear increased by {wear}%. Total wear: {self.total_wear}%"
