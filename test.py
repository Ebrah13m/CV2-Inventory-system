import Adafruit_DHT
import csv
import time

# Sensor and GPIO pin configuration
SENSOR = Adafruit_DHT.DHT11
GPIO_PIN = 17
CSV_FILE = 'sensor_data.csv'

def read_sensor():
    # Read the temperature and humidity from the DHT11 sensor
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, GPIO_PIN)
    return temperature, humidity

def log_to_csv(file_path, temperature, humidity):
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            writer.writerow(['Timestamp', 'Temperature (C)', 'Humidity (%)'])
        # Write the sensor data
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([timestamp, temperature, humidity])

def main():
    while True:
        temperature, humidity = read_sensor()
        if temperature is not None and humidity is not None:
            print(f'Temperature: {temperature:.1f}C  Humidity: {humidity:.1f}%')
            log_to_csv(CSV_FILE, temperature, humidity)
        else:
            print('Failed to get reading. Try again.')

        # Wait time
        time.sleep(2)

if __name__ == '__main__':
    main()
