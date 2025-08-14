FROM python:3.11-slim

ENV LOG_DIR=/var/log/pi_temperature_sensor
RUN mkdir -p $LOG_DIR &&\
  chmod 777 $LOG_DIR &&\
  mkdir -p /app &&\
  chmod 777 /app

COPY ./src/ /app/src/
#COPY requirements.txt /app

WORKDIR /app

#RUN pip install -r requirements.txt

# Set non-root user
USER nobody

ENV PYTHONUNBUFFERED=1 \
    ROOT_DIR="pi4b" \
    SENSOR_FILENAME="5432" \
    INTERVAL="1"

CMD ["sh", "-c", "python3 -m src.plot_temperature --root-dir \"$ROOT_DIR\" --sensor-filename \"$SENSOR_FILENAME\" --interval \"$INTERVAL\""]
