import datetime

class TemperatureDto:
    def __init__(self, device: str, value: float, timestamp: datetime):
        self.device = device
        self.value = value
        self.timestamp = timestamp

    # Convert to dict for JSON serialization
    def to_dict(self):
        return {"device": self.device, "value": self.value, "timestamp": self.timestamp}
