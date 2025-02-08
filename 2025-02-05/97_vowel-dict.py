def solution(word):
    # Define the vowels in order
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    # Precompute the positional weight values
    weights = [781, 156, 31, 6, 1]  # Derived from geometric series
    
    rank = 0  # Initialize the rank
    
    for i, char in enumerate(word):
        # Get the index of the current vowel (A=0, E=1, I=2, etc.)
        index = vowels.index(char)
        
        # Calculate contribution of this character at position i
        rank += index * weights[i] + 1  # +1 to account for 1-based indexing
    
    return rank

# Example test cases
print(solution("AAAAE"))  # Output: 6
print(solution("AAAE"))   # Output: 10
print(solution("I"))      # Output: 1563
print(solution("EIO"))    # Output: 1189
