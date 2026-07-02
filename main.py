from car import F1Car
from tires import SoftTire, HardTire
from telemetry import TelemetryLogger

def main():
    # Initialize our logger
    logger = TelemetryLogger()
    
    # 1. Start on softs for a quick stint
    quali_tire = SoftTire()
    my_car = F1Car("Verstappen", quali_tire)
    
    # Drive a stint and log the data
    stint_data = my_car.drive_stint(5)
    logger.log_data(stint_data)
    
    # 2. Pit stop for hards
    print("\n--- BOX BOX. Fitting Hard Tires. ---\n")
    race_tire = HardTire()
    my_car.tire = race_tire 
    
    # Drive the second stint and log the data
    stint2_data = my_car.drive_stint(20)
    logger.log_data(stint2_data)

if __name__ == "__main__":
    main()
