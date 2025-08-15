import argparse
import pathlib
import time
import threading
import sys

from src import logging_conf
from src import utils
from src import exceptions
from src import api_calls
from src.dto.temperature_dto import TemperatureDto


logger = logging_conf.config("plot_temperature")


def temp_loop(
    file_path: pathlib.Path,
    interval: int,
    url: str,
    name: str,
    stop_event: threading.Event,
):
    while not stop_event.is_set():
        try:
            temp = utils.parse_temp_in_cesius(file_path)
            logger.debug(f"{temp:.3f} °C")
            data = TemperatureDto(device=name, value=temp, timestamp=utils.timestamp())
            api_calls.send_temperature(data=data, url=url)

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
    parser.add_argument(
        "--url",
        default="http://localhost:8080/temp",
        help="URL for api call",
    )
    parser.add_argument(
        "--name",
        default="device_1",
        help="Name of the device -> as tag for the data",
    )
    args = parser.parse_args()

    root_dir: pathlib.Path = pathlib.Path(args.root_dir)
    filename: str = args.sensor_filename
    interval: int = int(args.interval)
    url: str = args.url
    device_name: str = args.name

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
        target=temp_loop,
        args=(sensor_file_path, interval, url, device_name, stop_event),
        daemon=True,
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
