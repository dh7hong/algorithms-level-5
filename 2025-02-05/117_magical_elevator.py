def solution(storey):
    cnt = 0
    while storey > 0:
        r = storey % 10  # Get the last digit
        
        if r > 5:  
            # If rounding up is cheaper, do so
            cnt += (10 - r)
            storey += (10 - r)
        elif r < 5:
            # If rounding down is better, do so
            cnt += r
        else:
            # If r == 5, check the next digit
            if (storey // 10) % 10 >= 5:
                storey += (10 - r)  # Round up
            cnt += r  # Otherwise, round down
        
        storey //= 10  # Move to the next digit
        
    return cnt