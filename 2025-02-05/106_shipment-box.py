def solution(order):
    belt = list(range(1, len(order) + 1))  # Original conveyor belt (1 to N)
    waiting = []  # Temporary hold; waiting
    count = 0  # Number of boxes successfully loaded
    index = 0  # Pointer for the belt
    
    for box in order:
        # Move boxes from the belt to the waiting 
        # until we find the required one
        while index < len(belt) and (not waiting or waiting[-1] != box):
            waiting.append(belt[index])
            index += 1  # Move to the next box in the belt
        
        # If the top of the waiting matches the required box, 
        # load it onto the truck
        if waiting and waiting[-1] == box:
            waiting.pop()  # Remove from waiting
            count += 1  # Successfully loaded box
        else:
            break  # If we can't load the required box, stop
    
    return count

# Example tests
print(solution([4, 3, 1, 2, 5]))  # Output: 2
print(solution([5, 4, 3, 2, 1]))  # Output: 5
