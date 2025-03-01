def solution(storey):
    magic_stones = 0  # Count the number of button presses
    carry = 0  # Used when rounding up affects the next digit
    
    while storey > 0 or carry > 0:
        digit = storey % 10  # Extract the last digit
        storey //= 10  # Remove the last digit from storey
        
        digit += carry  # Apply any carry from the previous step
        carry = 0  # Reset carry
        
        if digit < 5:  # If digit is 0 to 4, round down
            magic_stones += digit
        elif digit > 5:  # If digit is 6 to 9, round up
            magic_stones += (10 - digit)
            carry = 1  # This creates a carry to the next digit
        else:  # If digit is exactly 5
            if storey % 10 >= 5:  # Check the next digit
                magic_stones += (10 - digit)  # Round up
                carry = 1
            else:
                magic_stones += digit  # Round down

    return magic_stones
