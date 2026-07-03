from car import F1Car, SafetyCar
from tires import SoftTire, HardTire
from telemetry import TelemetryLogger
from personnel import Mechanic, ChiefEngineer

def main():
    logger = TelemetryLogger()
    
    # 1. Setup Track Session
    car1 = F1Car("Verstappen", SoftTire())
    mechanic = Mechanic()
    engineer = ChiefEngineer("GP")
    
    # 2. First Stint
    print(engineer.give_radio_comms("Push push, let's open a gap."))
    stint_data = car1.drive_stint(5)
    logger.log_data(stint_data)
    
    # 3. Pit Stop Phase
    print("\n--- PIT WINDOW OPEN ---")
    print(engineer.give_radio_comms("Box, box. We are fitting hards."))
    
    # The mechanic handles the physical stop
    pit_action = mechanic.change_tires(car1)
    print(pit_action)
    
    # Fit the new tires
    car1.tire = HardTire() 
    
    # 4. Second Stint
    print(engineer.give_radio_comms("Good stop. Manage these tires to the end."))
    stint2_data = car1.drive_stint(20)
    logger.log_data(stint2_data)

if __name__ == "__main__":
    main()
