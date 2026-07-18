import json

import pytest

from main import load_strategies, build_car
from tires import HardTire
from engine import MercedesEngine


def test_load_strategies_reads_json(tmp_path):
    strategies_file = tmp_path / "strategies.json"
    strategies_file.write_text(json.dumps({"race_laps": 50, "drivers": []}))
    config = load_strategies(str(strategies_file))
    assert config["race_laps"] == 50


def test_load_strategies_exits_on_missing_file(capsys):
    with pytest.raises(SystemExit):
        load_strategies("this_file_does_not_exist.json")
    assert "Can't find" in capsys.readouterr().out


def test_build_car_picks_the_right_tire_and_engine():
    driver_cfg = {
        "name": "Hamilton",
        "engine": "Mercedes",
        "stints": [{"tire": "Hard", "laps": 30}],
    }
    car = build_car(driver_cfg)
    assert car.name == "Hamilton"
    assert isinstance(car.tire, HardTire)
    assert isinstance(car.engine, MercedesEngine)
