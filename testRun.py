import serial
import time


ser = serial.Serial('COM6', baudrate=9600, timeout=1)


# Send a command to the NPK sensor to request data
ser.write(b'ReadData\r\n')

# Wait a moment to give the sensor time to respond
time.sleep(0.1)

# Read the response from the sensor
# response = ser.readline().decode().strip()
response = ser.readline().decode('ascii', errors='ignore').strip()



# Process the response if necessary
# (The format of the response will depend on the sensor's protocol)

# Example: If the sensor returns comma-separated values for N, P, and K:
# Assuming the response is in the format "N,P,K\r\n"
while response:
    print(response)
    # nitrogen, phosphorus, potassium = map(float, response.split(','))
    # print(f"N: {nitrogen}, P: {phosphorus}, K: {potassium}")
else:
    print("No response from the sensor.")

# Close the serial connection when you're done reading data
ser.close()
