import requests

from src.dto.temperature_dto import TemperatureDto
from src import logging_conf

logger = logging_conf.config("api_calls")


def send_temperature(data: TemperatureDto, url: str):
    logger.debug(f"Sending {data.device}:{data.value} to {url}")
    response = requests.post(url, json=data.to_dict())
    # Check if request was successful
    if response.status_code != 200:
        logger.error(f"{response.status_code}: {response.text}")
