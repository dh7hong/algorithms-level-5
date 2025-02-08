def time_to_minutes(time_str):
    """
    Convert time string 'HH:MM' to total minutes since 00:00.

    Args:
    time_str (str): A time string in the format 'HH:MM'.

    Returns:
    int: Total minutes since 00:00.
    """
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes  # Convert to total minutes

def calculate_fee(total_time, fees):
    """
    Calculate the parking fee based on the total parking time.

    Args:
    total_time (int): The total minutes a vehicle was parked.
    fees (list): List containing [base_time, base_fee, unit_time, unit_fee].

    Returns:
    int: The total parking fee for the vehicle.
    """
    base_time, base_fee, unit_time, unit_fee = fees

    if total_time <= base_time:
        return base_fee  # If parking time is within base time, return base fee

    # Calculate additional fees (manual ceiling without math.ceil)
    extra_time = total_time - base_time
    extra_units = extra_time // unit_time  # Full unit count
    if extra_time % unit_time > 0:  # If there's any remainder, add one extra unit
        extra_units += 1

    return base_fee + extra_units * unit_fee

def solution(fees, records):
    """
    Compute parking fees for each vehicle based on their entry and exit times.

    Args:
    fees (list): Parking fees [base_time, base_fee, unit_time, unit_fee].
    records (list): List of entry/exit records in the format "HH:MM CAR_ID IN/OUT".

    Returns:
    list: Parking fees sorted by vehicle number.
    """
    parking_times = {}  # Dictionary to store total parking time per vehicle
    active_entries = {}  # Dictionary to store currently parked vehicles

    for record in records:
        time, car_number, action = record.split()
        minutes = time_to_minutes(time)  # Convert time to minutes

        if action == "IN":
            active_entries[car_number] = minutes  # Store entry time
        elif action == "OUT":
            if car_number in active_entries:
                entry_time = active_entries.pop(car_number)  # Get entry time
                if car_number in parking_times:
                    parking_times[car_number] += (minutes - entry_time)  
                    # Add to existing time
                else:
                    parking_times[car_number] = (minutes - entry_time)  
                    # Initialize total time

    # Handle cars still parked at 23:59
    closing_time = time_to_minutes("23:59")
    for car_number, entry_time in active_entries.items():
        if car_number in parking_times:
            parking_times[car_number] += (closing_time - entry_time)
        else:
            parking_times[car_number] = (closing_time - entry_time)

    # Calculate fees for each vehicle
    fees_per_vehicle = {}
    for car_number, total_time in parking_times.items():
        fees_per_vehicle[car_number] = calculate_fee(total_time, fees)

    # Return fees sorted by vehicle number
    return [fees_per_vehicle[car] for car in sorted(fees_per_vehicle.keys())]

# Example Test Cases
print(solution([180, 5000, 10, 600], 
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", 
                "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", 
                "23:00 5961 OUT"]))  # Expected Output: [14600, 34400, 5000]

print(solution([120, 0, 60, 591], 
               ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT",
                "23:58 3961 IN"]))  # Expected Output: [0, 591]

print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))  # Expected Output: [14841]
