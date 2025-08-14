import pathlib
from src import exceptions


def search_file(root_dir: pathlib.Path, filename: str):
    return list(root_dir.rglob(filename))


def parse_temp_in_cesius(file: pathlib.Path):
    with file.open() as f:
        lines = f.readlines()

    if lines[0].strip().endswith("YES"):
        temp_str = lines[1].split("t=")[-1].strip()
        temperature_c = int(temp_str) / 1000.0
        return temperature_c
    else:
        raise exceptions.CRCError("CRC check failed for 1-Wire sensor data.")
