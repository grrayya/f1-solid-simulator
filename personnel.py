from abc import ABC, abstractmethod


class IPitCrew(ABC):
    @abstractmethod
    def change_tires(self, car) -> str:
        pass


class IRaceEngineer(ABC):
    @abstractmethod
    def give_radio_comms(self, message: str) -> str:
        pass


class Mechanic(IPitCrew):
    def change_tires(self, car) -> str:
        return f"Mechanic completed a 2.1s pit stop for {car.name}."


class ChiefEngineer(IRaceEngineer):
    def __init__(self, name: str):
        self.name = name

    def give_radio_comms(self, message: str) -> str:
        return f"Radio ({self.name}): '{message}'"
