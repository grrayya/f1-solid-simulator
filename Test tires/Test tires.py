import pytest

from tires import SoftTire, HardTire, IntermediateTire, WetTire


def test_hard_tire_wears_slower_than_soft():
    soft, hard = SoftTire(), HardTire()
    assert soft.calculate_wear(10) > hard.calculate_wear(10)


def test_soft_tire_penalty_stays_linear_before_cliff():
    soft = SoftTire()
    # below 70% wear there's no cliff term yet
    assert soft.lap_time_penalty(50) == pytest.approx(50 * 0.035)


def test_soft_tire_penalty_jumps_past_cliff():
    soft = SoftTire()
    penalty_at_69 = soft.lap_time_penalty(69)
    penalty_at_71 = soft.lap_time_penalty(71)
    # crossing 70% should cost noticeably more than 2 wear-points' worth
    # of the base rate would suggest
    normal_gap = 2 * 0.035
    assert (penalty_at_71 - penalty_at_69) > normal_gap


def test_intermediate_and_wet_wear_between_soft_and_hard():
    soft, hard = SoftTire(), HardTire()
    inter, wet = IntermediateTire(), WetTire()
    laps = 20
    assert hard.calculate_wear(laps) < wet.calculate_wear(laps) < inter.calculate_wear(laps) < soft.calculate_wear(laps)


def test_zero_laps_means_zero_wear():
    for compound in (SoftTire(), HardTire(), IntermediateTire(), WetTire()):
        assert compound.calculate_wear(0) == 0
