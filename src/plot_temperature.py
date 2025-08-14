import argparse
import pathlib
import time
import threading
import sys

from src import logging_conf
from src import utils
from src import exceptions


logger = logging_conf.config("plot_temperature")


def temp_loop(file_path: pathlib.Path, interval: int, stop_event: threading.Event):
    while not stop_event.is_set():
        try:
            temp = utils.parse_temp_in_cesius(file_path)
            logger.info(f"{temp:.3f} °C")
        except exceptions.CRCError as e:
            logger.error("Error reading temperature:", e)
        stop_event.wait(interval)


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
        "--interval",
        default=60,
        help="Interval for polling in seconds",
    )
    args = parser.parse_args()

    root_dir: pathlib.Path = pathlib.Path(args.root_dir)
    filename: str = args.sensor_filename
    interval: int = int(args.interval)

    logger.info(f"root-dir: {root_dir}, filename: {filename}, interval: {interval}")

    try:
        sensor_file_path = utils.search_file(root_dir, filename)[0]
        logger.info(f"sensor file path is: {sensor_file_path}")
    except IndexError:
        logger.error(
            f"No sensor found in {root_dir} with filename {filename} -> terminating"
        )
        sys.exit(1)

    stop_event = threading.Event()
    thread = threading.Thread(
        target=temp_loop, args=(sensor_file_path, interval, stop_event), daemon=True
    )
    thread.start()

    try:
        # Main thread can do other things here, or just sleep
        while thread.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("\nStopping temperature monitor...")
        stop_event.set()  # signal the thread to exit
        thread.join()  # wait for thread to finish
    logger.info("Exited gracefully.")
