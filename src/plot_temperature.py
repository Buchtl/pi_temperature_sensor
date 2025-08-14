import argparse
import pathlib
from src import logging_conf

logger = logging_conf.config("plot_temperature")

# /sys/bus/w1/devices/10-000803cd476f


def search_data_file(root_dir: pathlib.Path, filename: str):
    return list(root_dir.rglob(filename))


# def search_data_file(root_dir: pathlib.Path, filename: str):
#    results = []
#    for dirpath, dirnames, filenames in os.walk(root_dir, followlinks=True):
#        if filename in filenames:
#            results.append(os.path.join(dirpath, filename))
#    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Polling data from the charger and write to database"
    )
    parser.add_argument(
        "--root-dir",
        default="/sys/bus/w1/devices",
        help="Dir where to search for sensor",
    )
    parser.add_argument(
        "--sensor-filename",
        default="w1_slave",
        help="Name of the sensor file to search for",
    )
    args = parser.parse_args()

    root_dir = pathlib.Path(args.root_dir)
    filename = args.sensor_filename

    logger.info(f"Searching for {filename} in {root_dir}")
    sensor_file_path = search_data_file(root_dir, filename)[0]

    logger.info(f"sensor file path is: {sensor_file_path}")
