import serial

# Replace /dev/ttyUSB0 with your actual device name if different
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

while True:
  if ser.in_waiting > 0:
    line = ser.readline().decode('utf-8').rstrip()
    print(f'Received: {line}')
