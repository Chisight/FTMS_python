import sys
import json
import asyncio
import time
from bleak import BleakClient
from lib import const as c
from lib.extract_treadmill_data import extract_treadmill_data

def get_current_timestamp():
    """Return the current timestamp formatted as a string."""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def notification_handler(characteristic_uuid, value):
    """Handle notifications from the BLE device."""
    timestamp = get_current_timestamp()
    # Handle treadmill data extraction
    if str(characteristic_uuid).startswith(c.TreadmillData):
        result = extract_treadmill_data(value, units='english')
        print(result)

async def read_and_subscribe(address):
    while True:  # Keep trying to connect indefinitely
        try:
            async with BleakClient(address) as client:
                print(f"Connected to {address}")

                # Add a short delay to allow the device to stabilize
                await asyncio.sleep(2)

                await client.start_notify(c.TreadmillData, notification_handler)

                while True:
                    await asyncio.sleep(1)  # Sleep to keep the loop alive

        except Exception as e:
            print(f"Connection failed: {e}. Retrying in 5 seconds...")
            await asyncio.sleep(5)  # Wait before retrying

def main():
    # Check the number of arguments
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help']:
        print("Usage: python bluetooth_read_treadmill.py <bluetooth MACaddress>")
        print("Returns Json data")
        return

    param = sys.argv[1]
    asyncio.run(read_and_subscribe(param))

if __name__ == '__main__':
    main()
