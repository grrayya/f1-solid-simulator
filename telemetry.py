class TelemetryLogger:
    """Handles only the storage and logging of race data."""
    def log_data(self, data, filename="telemetry.txt"):
        with open(filename, "a") as file:
            file.write(data + "\n")
        print(f"[SYSTEM] Logged to {filename}: {data}")
