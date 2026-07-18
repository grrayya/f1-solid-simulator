from engine import HondaEngine, MercedesEngine


def test_engines_report_distinct_power_units():
    assert HondaEngine().get_power_output() != MercedesEngine().get_power_output()
