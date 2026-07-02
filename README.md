# F1 Race Strategy Simulator

A terminal-based Formula 1 race strategy simulator built in Python.
      specifically focusing on implementing the **S.O.L.I.D. design principles**.


Currently implemented SOLID principles:
- **Single Responsibility Principle (SRP):** Separated the `F1Car` (driving logic) from the `TelemetryLogger` (data logging logic).
- **Open/Closed Principle (OCP):** Implemented an abstract `TireCompound` system. New tire types (e.g., Wet, Intermediate) can be added without modifying the core car logic.


## File Structure
- `main.py` - The main simulation loop.
- `car.py` - Manages the vehicle state and stint data.
- `tires.py` - Abstract tire logic and specific compound wear rates.
- `telemetry.py` - Handles writing race data to external logs.

