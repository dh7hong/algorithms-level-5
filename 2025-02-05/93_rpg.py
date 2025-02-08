def solution(k, dungeons):
    max_dungeons = 0  
    dungeons_cleared = [False] * len(dungeons)  # Track cleared dungeons
    print(f"Starting HP: {k} HP, Dungeons: {dungeons}")
    
    def explore_dungeons(hp, count, cleared_dungeon_order):
        nonlocal max_dungeons
        max_dungeons = max(max_dungeons, count)  # Update max count
        print("=============================================================================================")
        print(f"Current HP: {hp}, Dungeons Cleared: {count}, Name of Cleared Dungeons: {cleared_dungeon_order}")

        for i in range(len(dungeons)):
            min_hp_required, consumption = dungeons[i]

            if not dungeons_cleared[i] and hp >= min_hp_required:  # Can we enter this dungeon?
                dungeons_cleared[i] = True  # Mark dungeon as cleared
                print(f"Entering Dungeon {i}: Current HP {hp}, Requires: {min_hp_required} HP, Consumes: {consumption} HP") 
                print(f"Remaining HP After clearing Dungeon {i}: {hp - consumption} HP")
                
                explore_dungeons(hp - consumption, count + 1, cleared_dungeon_order + [i])  # Explore next dungeon
                
                dungeons_cleared[i] = False  # Backtrack to explore other possibilities
                print(f"Backtracking from Dungeon {i}, Restoring HP to {hp}, to explore other dungeons order possibilities")
                
    explore_dungeons(k, 0, [])  # Start exploration with initial fatigue `k` and 0 dungeons explored
    return max_dungeons

# Example Test Case
print("\nMAX DUNGEONS CLEARED:", solution(80, [[80, 20], [50, 40], [30, 10]]))  # Expected Output: 3
