from telemetry import TelemetryLogger


def test_log_data_appends_to_file(tmp_path):
    log_file = tmp_path / "race.txt"
    TelemetryLogger().log_data("lap 1 complete", filename=str(log_file))
    assert log_file.read_text() == "lap 1 complete\n"


def test_log_data_appends_multiple_lines(tmp_path):
    log_file = tmp_path / "race.txt"
    logger = TelemetryLogger()
    logger.log_data("lap 1", filename=str(log_file))
    logger.log_data("lap 2", filename=str(log_file))
    assert log_file.read_text() == "lap 1\nlap 2\n"


def test_log_data_handles_unwritable_path(tmp_path, capsys):
    # pointing at a directory instead of a file guarantees an OSError on write
    bad_path = tmp_path  # a directory, not a file
    TelemetryLogger().log_data("this shouldn't crash", filename=str(bad_path))
    captured = capsys.readouterr()
    assert "Couldn't write" in captured.out
