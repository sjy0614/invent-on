import serial
import time

ser = serial.Serial('/dev/ttyS0',9600,timeout=1)
ser.flush()

print("Raspberry Pi is ready.")

while True:
    ser.write(b'A\n')
    print("Sent'A\\n' to Arduino.")
    
    if ser.in_waiting > 0:
        response = ser.readline().decode('UTF-8').rstrip()
        print(f"Response from Arduino:{response}")
        
        time.sleep(5)
        
