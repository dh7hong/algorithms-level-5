def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length  
    # The bridge starts empty
    time = 0  
    # Keep track of time
    current_weight = 0  
    # Track the total weight on the bridge

    while truck_weights or current_weight > 0:  
        # Keep running until all trucks cross
        time += 1  
        # Each loop represents 1 second

        # Step 1: Remove the first truck from the bridge (if any)
        leaving_truck = bridge.pop(0)  
        # A truck moves off the bridge
        current_weight -= leaving_truck  
        # Reduce weight on the bridge

        # Step 2: Check if we can add a new truck to the bridge
        if truck_weights:
            # Only add the next truck if it does 
            # not exceed the bridge weight limit
            if current_weight + truck_weights[0] <= weight:
                next_truck = truck_weights.pop(0)  
                # Get the next truck
                bridge.append(next_truck)  
                # Add the truck to the bridge
                current_weight += next_truck  
                # Update the total weight
            else:
                bridge.append(0)  
                # No truck added, just move time forward

    return time  
    # Return the total time needed for all trucks to cross

# Example test cases
print(solution(2, 10, [7,4,5,6]))  # Output: 8
print(solution(100, 100, [10]))    # Output: 101
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))  # Output: 110
