class TemperatureDto:
    def __init__(self, device: str, value: float):
        self.device = device
        self.value = value

    # Convert to dict for JSON serialization
    def to_dict(self):
        return {"device": self.device, "value": self.value}
