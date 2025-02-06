def is_prime(num):
    """
    Function to check if a number is prime without using the math module.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if num is a prime number, False otherwise.
    """
    if num < 2:
        return False  # Prime numbers are greater than 1

    # Check for factors up to the integer square root (without using math.sqrt)
    i = 2
    while i * i <= num:  # Equivalent to checking up to sqrt(num)
        if num % i == 0:
            return False  # Not a prime if divisible
        i += 1  # Increment the divisor
    return True  # Prime number

def convert_to_base(n, k):
    """
    Function to convert a decimal number `n` to base `k` without using math module.

    Args:
    n (int): The decimal number.
    k (int): The base to convert to.

    Returns:
    str: The number represented in base `k` as a string.
    """
    if n == 0:
        return "0"  # Edge case

    result = ""
    while n > 0:
        result = str(n % k) + result  # Get remainder and prepend to result
        n //= k  # Reduce n by dividing it by k
    return result

def solution(n, k):
    """
    Function to count prime numbers found in the `k`-base representation of `n`.
    
    Args:
    n (int): The number to convert.
    k (int): The base to convert to.

    Returns:
    int: The count of prime numbers found in the base `k` representation of `n`.
    """
    base_k_number = convert_to_base(n, k)  # Convert number to base k
    print(f"Base {k} representation of {n}: {base_k_number}")  # Debugging output

    split_numbers = base_k_number.split("0")  # Split by "0" to extract potential primes
    print(f"Extracted numbers: {split_numbers}")  # Debugging output

    prime_count = 0  # Initialize count of prime numbers

    for num_str in split_numbers:
        if num_str == "":  # Ignore empty strings (caused by consecutive zeros)
            continue
        
        num = int(num_str)  # Convert string to integer
        
        if is_prime(num):  # Check if the number is prime
            print(f"{num} is prime.")  # Debugging output
            prime_count += 1  # Increment count

    return prime_count  # Return the total count of prime numbers found

# Example Test Cases
print("Output:", solution(437674, 3))  # Expected Output: 3
print("Output:", solution(110011, 10))  # Expected Output: 2
