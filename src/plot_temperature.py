import argparse
import pathlib
import os
import logging

# /sys/bus/w1/devices/10-000803cd476f

def search_data_file(root_dir: pathlib.Path, filename: str):
    return list(root_dir.rglob(filename))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Polling data from the charger and write to database"
    )
    parser.add_argument("--todo", default="localhost", help="URL with of the database")
    args = parser.parse_args()

    root_dir = pathlib.Path("./test_device")
    filename = "w1_slave"
    print(f"File is {search_data_file(root_dir, filename)[0]}")


