def solution(weights):
    weight_freq = {}  # Dictionary to store frequency of each weight
    answer = 0

    # Iterate through weights and populate the frequency dictionary
    for w in weights:
        if w in weight_freq:
            weight_freq[w] += 1
        else:
            weight_freq[w] = 1

    # Iterate through unique weights and count valid pairs
    for w in weight_freq:
        # Case 1: Identical weights (W_A = W_B)
        if weight_freq[w] > 1:
            answer += (weight_freq[w] * (weight_freq[w] - 1)) // 2  # nC2 = n(n-1)/2

        # Case 2: Different weight pairs based on valid ratios
        for ratio in [3/2, 2/1, 4/3]:  # Possible ratios
            target = w * ratio
            if target in weight_freq:
                answer += weight_freq[w] * weight_freq[target]  # Multiply occurrences

    return answer

# Example test case
weights = [100, 180, 360, 100, 270]
print(solution(weights))  # Output: 4
