import argparse
import pathlib
from src import logging_conf
from src import utils

logger = logging_conf.config("plot_temperature")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Polling data from the charger and write to database"
    )
    parser.add_argument(
        "--root-dir",
        default="/sys/devices",
        help="Dir where to search for sensor",
    )
    parser.add_argument(
        "--sensor-filename",
        default="w1_slave",
        help="Name of the sensor file to search for",
    )
    parser.add_argument(
        "--period",
        default=60,
        help="Period for polling in seconds",
    )
    args = parser.parse_args()

    root_dir = pathlib.Path(args.root_dir)
    filename = args.sensor_filename
    period = args.period

    logger.info(f"root-dir: {root_dir}, filename: {filename}, period: {period}")

    logger.info(f"Searching for {filename} in {root_dir}")
    sensor_file_path = utils.search_file(root_dir, filename)[0]
    logger.info(f"sensor file path is: {sensor_file_path}")
