def compute_gcd_iterative(a, b):
    """
    Compute the greatest common divisor (GCD) of two numbers iteratively 
    without using the built-in math.gcd function.
    """
    while b:
        a, b = b, a % b
    return a

def solution(W, H):
    """
    Given width (W) and height (H) of the grid, return the number of 1x1 squares 
    that can still be used after the paper is cut diagonally.
    """
    # Compute the greatest common divisor iteratively
    common_divisor = compute_gcd_iterative(W, H)

    # Avoid large multiplication
    return (W * H) - (W + H - common_divisor)

# Example usage
print(solution(8, 12))  # Output: 80
