import json
import random
import sys

from car import F1Car, SafetyCar
from tires import SoftTire, HardTire, IntermediateTire, WetTire
from telemetry import TelemetryLogger
from personnel import Mechanic, ChiefEngineer
from engine import HondaEngine, MercedesEngine

TIRE_MAP = {
    "Soft": SoftTire,
    "Hard": HardTire,
    "Intermediate": IntermediateTire,
    "Wet": WetTire,
}

ENGINE_MAP = {
    "Honda": HondaEngine,
    "Mercedes": MercedesEngine,
}

CAUTION_CHANCE = 0.20  # chance a given stint gets interrupted by a VSC/SC


def load_strategies(path: str = "strategies.json") -> dict:
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Can't find {path} - pass a different strategies file as an argument?")
        sys.exit(1)


def build_car(driver_cfg: dict) -> F1Car:
    first_tire = TIRE_MAP[driver_cfg["stints"][0]["tire"]]()
    engine = ENGINE_MAP[driver_cfg["engine"]]()
    return F1Car(driver_cfg["name"], first_tire, engine)


def run_driver_strategy(car: F1Car, driver_cfg: dict, mechanic: Mechanic,
                         engineer: ChiefEngineer, logger: TelemetryLogger,
                         rng: random.Random) -> None:
    stints = driver_cfg["stints"]
    print(f"\n--- {car.name} ({driver_cfg['strategy_label']} strategy) ---")

    for i, stint in enumerate(stints):
        laps = stint["laps"]
        caution = rng.random() < CAUTION_CHANCE
        if caution:
            print(f"WARNING: Caution flag deployed during {car.name}'s stint {i + 1}!")

        logger.log_data(car.drive_stint(laps, caution=caution))

        if i < len(stints) - 1:
            next_tire = TIRE_MAP[stints[i + 1]["tire"]]()
            print(mechanic.change_tires(car))
            print(engineer.give_radio_comms(
                f"Box, box. Fitting {stints[i + 1]['tire']} tires."))
            car.tire = next_tire


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else None
    rng = random.Random(seed)

    config = load_strategies()
    logger = TelemetryLogger()
    mechanic = Mechanic()
    engineer = ChiefEngineer("GP")
    safety_car = SafetyCar("Maylander")

    print("\n--- LIGHTS OUT AND AWAY WE GO ---")

    cars = []
    for driver_cfg in config["drivers"]:
        car = build_car(driver_cfg)
        run_driver_strategy(car, driver_cfg, mechanic, engineer, logger, rng)
        cars.append((car, driver_cfg["strategy_label"]))

    print("\n--- FINAL TRACK STATUS ---")
    for vehicle in [car for car, _ in cars] + [safety_car]:
        print(vehicle.get_status())

    print("\n--- STRATEGY COMPARISON ---")
    ranked = sorted(cars, key=lambda pair: pair[0].total_race_time)
    winner, winner_strategy = ranked[0]
    for car, strategy in ranked:
        gap = car.total_race_time - winner.total_race_time
        gap_str = "leader" if gap == 0 else f"+{gap:.1f}s"
        print(f"{car.name:12s} | {strategy:6s} | "
              f"{car.total_race_time:8.1f}s total | {gap_str}")

    print(f"\n{winner.name}'s {winner_strategy} strategy wins this run "
          f"(re-run with a different seed to see it play out differently).")


if __name__ == "__main__":
    main()
