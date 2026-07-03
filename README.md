# F1 Race Strategy Simulator

A terminal-based Formula 1 race strategy simulator built in Python.
      specifically focusing on implementing the **S.O.L.I.D. design principles**.


Currently implemented SOLID principles:
- **Single Responsibility Principle (SRP):** Separated the `F1Car` (driving logic) from the `TelemetryLogger` (data logging logic).
- **Open/Closed Principle (OCP):** Implemented an abstract `TireCompound` system. New tire types (e.g., Wet, Intermediate) can be added without modifying the core car logic.
- **Liskov Substitution Principle (LSP):** Created a unified `Vehicle` base class. The main simulation loop can process different track vehicles (e.g., `F1Car`, `SafetyCar`) interchangeably without breaking.
- **Interface Segregation Principle (ISP):** Split team personnel roles into narrow, specific interfaces (`IPitCrew` and `IRaceEngineer`) so mechanics and engineers are not forced to inherit methods they don't use.
- **Dependency Inversion Principle (DIP):** The `F1Car` class depends on an abstract `IEngine` interface rather than a concrete engine. Specific power units (Honda, Mercedes) are injected into the car at runtime.

## File Structure
- `main.py` - The main simulation loop.
- `engine.py` - Abstract powertrain interfaces and concrete engine modules.
- `car.py` - Manages the vehicle state and stint data.
- `tires.py` - Abstract tire logic and specific compound wear rates.
- `telemetry.py` - Handles writing race data to external logs.
- `personnel.py` - Segregated interfaces for pit crew and race engineers

