from car import F1Car, SafetyCar
from tires import SoftTire, HardTire
from telemetry import TelemetryLogger
from personnel import Mechanic, ChiefEngineer
from engine import HondaEngine, MercedesEngine

def main():
    # 1. Initialize our Telemetry Logger (SRP)
    logger = TelemetryLogger()
    
    # 2. Setup Team Personnel (ISP)
    mechanic = Mechanic()
    engineer = ChiefEngineer("GP")
    
    # 3. Setup Power Units (DIP)
    honda_pu = HondaEngine()
    merc_pu = MercedesEngine()
    
    # 4. Build the Grid 
    # Injecting the tires (OCP) and engines (DIP) into the cars
    car1 = F1Car("Verstappen", SoftTire(), honda_pu)
    car2 = F1Car("Hamilton", HardTire(), merc_pu)
    safety_car = SafetyCar("Mayländer")
    
    # --- RACE START ---
    print("\n🚥 --- LIGHTS OUT AND AWAY WE GO --- 🚥\n")
    
    # Stint 1
    print(engineer.give_radio_comms("Push push, let's open a gap."))
    logger.log_data(car1.drive_stint(10))
    logger.log_data(car2.drive_stint(10))
    
    # --- PIT WINDOW ---
    print("\n🔧 --- PIT WINDOW OPEN --- 🔧")
    print(engineer.give_radio_comms("Box, box. We are fitting hards."))
    
    # Mechanic performs the stop
    print(mechanic.change_tires(car1))
    
    # Swap out the tires
    car1.tire = HardTire() 
    
    # Stint 2
    print(engineer.give_radio_comms("Good stop. Manage these tires to the end."))
    logger.log_data(car1.drive_stint(20))
    
    # --- TRACK STATUS SUMMARY ---
    print("\n🏁 --- FINAL TRACK STATUS --- 🏁")
    
    # Loop through our Vehicle base classes (LSP)
    # The program treats F1Cars and the SafetyCar exactly the same way here!
    track_vehicles = [car1, car2, safety_car]
    
    for vehicle in track_vehicles:
        print(vehicle.get_status())

if __name__ == "__main__":
    main()
