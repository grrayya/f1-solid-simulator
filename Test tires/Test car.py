from car import F1Car, SafetyCar, BASE_LAP_TIME
from tires import HardTire
from engine import HondaEngine


def make_car():
    return F1Car("Perez", HardTire(), HondaEngine())


def test_drive_stint_accumulates_wear_and_time():
    car = make_car()
    car.drive_stint(10)
    expected_wear = HardTire().calculate_wear(10)
    assert car.total_wear == expected_wear
    assert car.total_race_time > 0


def test_two_stints_stack_on_top_of_each_other():
    car = make_car()
    car.drive_stint(10)
    wear_after_first = car.total_wear
    car.drive_stint(10)
    assert car.total_wear > wear_after_first


def test_caution_reduces_wear_compared_to_green_flag():
    green_car = make_car()
    green_car.drive_stint(10)

    caution_car = make_car()
    caution_car.drive_stint(10, caution=True)

    assert caution_car.total_wear < green_car.total_wear


def test_caution_slows_the_car_down():
    # lap time multiplier (1.3x) should outweigh the
    # reduced tire penalty
    fresh_tire_penalty = HardTire().lap_time_penalty(0)
    caution_lap_time = (BASE_LAP_TIME + fresh_tire_penalty) * 1.3
    assert caution_lap_time > BASE_LAP_TIME


def test_status_string_mentions_the_driver_name():
    car = make_car()
    assert "Perez" in car.get_status()


def test_safety_car_status_does_not_track_wear():
    safety_car = SafetyCar("Maylander")
    status = safety_car.get_status()
    assert "Maylander" in status
    assert "%" not in status
