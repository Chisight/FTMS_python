import json
import time

def extract_treadmill_data(byte_array, units='metric'):
    # Unpack the flags (2 bytes)
    flags = int.from_bytes(byte_array[0:2], byteorder='little')

    # Initialize the result dictionary
    result = {
        "timeStamp": int(time.time()),  # Current Unix timestamp
    }
    
    # Initialize the current offset
    offset = 2  # Start after the flags

    # Extract Instantaneous Speed (always present)
    instantaneous_speed = int.from_bytes(byte_array[offset:offset + 2], byteorder='little')
    result["instantaneousSpeed"] = round(instantaneous_speed * 0.01, 2)  # Convert to km/h
    if units == 'english':
        result["instantaneousSpeed"] = round(instantaneous_speed / 160.934398, 1)  # Convert to mph
    offset += 2  # Move to the next field

    # Check for Average Speed (Bit 1)
    if flags & 0x0002:  # Average Speed feature
        average_speed = int.from_bytes(byte_array[offset:offset + 2], byteorder='little')
        result["averageSpeed"] = round(average_speed * 0.01, 2)  # Convert to km/h
        if units == 'english':
            result["averageSpeed"] = round(average_speed / 160.934398, 1)  # Convert to mph
        offset += 2  # Move to the next field

    # Check for Total Distance (Bit 2)
    if flags & 0x0004:  # Total Distance feature
        total_distance = int.from_bytes(byte_array[offset:offset + 3] + b'\x00', byteorder='little')  # uint24
        result["totalDistance"] = total_distance  # in meters
        if units == 'english':
            result["totalDistance"] = round(total_distance / 1609.34398, 2)  # Convert to miles
        offset += 3  # Move to the next field

    # Check for Inclination (Bit 3)
    if flags & 0x0008:  # Inclination feature
        inclination = int.from_bytes(byte_array[offset:offset + 2], byteorder='little')
        result["inclination"] = round(inclination * 0.1, 2)  # Convert to percent
        offset += 2  # Move to the next field

    # Check for Elevation Gain (Bit 4)
    if flags & 0x0010:  # Elevation Gain feature
        positive_elevation_gain = int.from_bytes(byte_array[offset:offset + 2], byteorder='little')
        negative_elevation_gain = int.from_bytes(byte_array[offset + 2:offset + 4], byteorder='little')
        result["positiveElevationGain"] = positive_elevation_gain  # in meters
        result["negativeElevationGain"] = negative_elevation_gain  # in meters
        if units == 'english':
            result["positiveElevationGain"] = round(positive_elevation_gain * 3.28084, 2)  # Convert to feet
            result["negativeElevationGain"] = round(negative_elevation_gain * 3.28084, 2)  # Convert to feet
        offset += 4  # Move to the next field

    # Check for Instantaneous Pace (Bit 5)
    if flags & 0x0020:  # Instantaneous Pace feature
        instantaneous_pace = int.from_bytes(byte_array[offset:offset + 2], byteorder='little')
        result["instantaneousPace"] = round(instantaneous_pace * 0.1, 2)  # Convert to min/km
        if units == 'english':
            result["instantaneousPace"] = round(instantaneous_pace * 0.1 * 1.609344, 2)  # Convert to min/mi
        offset += 2  # Move to the next field

    # Check for Average Pace (Bit 6)
    if flags & 0x0040:  # Average Pace feature
        average_pace = int.from_bytes(byte_array[offset:offset + 2], byteorder='little')
        result["averagePace"] = round(average_pace * 0.1, 2)  # Convert to min/km
        if units == 'english':
            result["averagePace"] = round(average_pace * 0.1 * 1.609344, 2)  # Convert to min/mi
        offset += 2  # Move to the next field

    # Check for Expended Energy (Bit 7)
    if flags & 0x0080:  # Expended Energy feature
        total_energy = int.from_bytes(byte_array[offset:offset + 2], byteorder='little')
        energy_per_hour = int.from_bytes(byte_array[offset + 2:offset + 4], byteorder='little')  # uint16
        energy_per_minute = byte_array[offset + 4]  # uint8
        result["totalEnergy"] = total_energy  # in kcal
        result["energyPerHour"] = energy_per_hour  # in kcal
        result["energyPerMinute"] = energy_per_minute  # in kcal
        offset += 5  # Move to the next field

    # Check for Heart Rate (Bit 8)
    if flags & 0x0100:  # Heart Rate feature
        heart_rate = byte_array[offset]  # uint8
        result["heartRate"] = heart_rate  # in beats/min
        offset += 1  # Move to the next field

    # Check for Metabolic Equivalent (Bit 9)
    if flags & 0x0200:  # Metabolic Equivalent feature
        metabolic_equivalent = byte_array[offset]  # uint8
        result["metabolicEquivalent"] = round(metabolic_equivalent * 0.1, 2)  # Convert to METs
        offset += 1  # Move to the next field

    # Check for Elapsed Time (Bit 10)
    if flags & 0x0400:  # Elapsed Time feature
        elapsed_time = int.from_bytes(byte_array[offset:offset + 2], byteorder='little')
        result["elapsedTime"] = elapsed_time  # in seconds
        offset += 2  # Move to the next field

    # Check for Remaining Time (Bit 11)
    if flags & 0x0800:  # Remaining Time feature
        remaining_time = int.from_bytes(byte_array[offset:offset + 2], byteorder='little')
        result["remainingTime"] = remaining_time  # in seconds
        offset += 2  # Move to the next field

    # Check for Force on Belt (Bit 12)
    if flags & 0x1000:  # Force on Belt feature
        force_on_belt = int.from_bytes(byte_array[offset:offset + 2], byteorder='little')
        result["forceOnBelt"] = force_on_belt  # in newtons
        offset += 2  # Move to the next field

    # Check for Power Output (Bit 13)
    if flags & 0x2000:  # Power Output feature
        power_output = int.from_bytes(byte_array[offset:offset + 2], byteorder='little')
        result["powerOutput"] = power_output  # in watts
        offset += 2  # Move to the next field

    # Note: Bits 14 and 15 are reserved and not used.

    return json.dumps(result)
