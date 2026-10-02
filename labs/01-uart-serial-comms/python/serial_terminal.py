"""
Python Serial Port Monitor & Loopback Tester
Requires: pyserial (pip install pyserial)
"""
import sys

def list_serial_ports():
    try:
        import serial.tools.list_ports
        ports = serial.tools.list_ports.comports()
        print("=== Available Serial Ports ===")
        if not ports:
            print("No serial ports detected.")
        for p in ports:
            print(f"- {p.device}: {p.description}")
        print("==============================")
    except ImportError:
        print("[!] 'pyserial' not installed. Install with: pip install pyserial")

def run_loopback_test(port: str, baudrate: int = 115200):
    try:
        import serial
        print(f"Opening port {port} at {baudrate} baud...")
        with serial.Serial(port, baudrate, timeout=1) as ser:
            test_msg = b"Hello Embedded World!\n"
            print(f"Sending: {test_msg}")
            ser.write(test_msg)
            
            response = ser.readline()
            print(f"Received: {response}")
    except Exception as e:
        print(f"Error opening port: {e}")

if __name__ == "__main__":
    list_serial_ports()
    if len(sys.argv) > 1:
        run_loopback_test(sys.argv[1])
