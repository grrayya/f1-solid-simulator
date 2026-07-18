from personnel import Mechanic, ChiefEngineer
from car import F1Car
from tires import SoftTire
from engine import HondaEngine


def test_mechanic_mentions_the_car_by_name():
    car = F1Car("Norris", SoftTire(), HondaEngine())
    result = Mechanic().change_tires(car)
    assert "Norris" in result


def test_chief_engineer_wraps_message_with_call_sign():
    comms = ChiefEngineer("GP").give_radio_comms("Box, box.")
    assert "GP" in comms
    assert "Box, box." in comms
