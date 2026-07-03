from car import F1Car, SafetyCar
from tires import SoftTire, HardTire
from telemetry import TelemetryLogger

def main():
    logger = TelemetryLogger()
    
    # Setup our track session objects
    quali_tire = SoftTire()
    car1 = F1Car("Verstappen", quali_tire)
    car2 = F1Car("Leclerc", HardTire())
    safety_car = SafetyCar("Mayländer")
    
    # Run a quick simulation action
    stint_data = car1.drive_stint(5)
    logger.log_data(stint_data)
    
    print("\n--- Track Status Update ---")
    # LSP IN ACTION: We treat F1Cars and SafetyCars exactly the same way 
    # via the Vehicle base class interface. The program never crashes.
    track_vehicles = [car1, car2, safety_car]
    
    for vehicle in track_vehicles:
        print(vehicle.get_status())

if __name__ == "__main__":
    main()
