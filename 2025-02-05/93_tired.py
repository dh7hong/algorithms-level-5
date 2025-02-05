def solution(k, dungeons):
    max_dungeons = 0  
    # Track the maximum dungeons explored
    visited = [False] * len(dungeons) 
    print(visited) 
    # Track visited dungeons

    def explore_dungeons(current_fatigue, count):
        nonlocal max_dungeons
        max_dungeons = max(max_dungeons, count)  
        # Update max count

        for i in range(len(dungeons)):
            min_required, consumption = dungeons[i]
          
            # If we haven't visited this dungeon and have enough fatigue
            if not visited[i] and current_fatigue >= min_required:
                visited[i] = True  
                # Mark dungeon as visited
                explore_dungeons(current_fatigue - consumption, count + 1)  
                # Explore next dungeon
                visited[i] = False  
                # Backtrack to explore other possibilities

    explore_dungeons(k, 0)  
    # Start exploration with initial fatigue `k` and 0 dungeons explored
    return max_dungeons
  
# Example Test Cases
print(solution(80, [[80, 20], [50, 40], [30, 10]]))  # Output: 3