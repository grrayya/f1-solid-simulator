class TelemetryLogger:
    def log_data(self, entry, filename="telemetry.txt"):
        try:
            with open(filename, "a") as file:
                file.write(entry + "\n")
        except OSError as exc:
            print(f"[SYSTEM] Couldn't write to {filename}: {exc}")
            return
        print(f"[SYSTEM] Logged to {filename}: {entry}")
