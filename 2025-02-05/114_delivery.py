def solution(N, road, K):
    # Step 1: Build the graph using an adjacency list
    # Initialize an empty dictionary to represent the graph
    graph = {}

    # Iterate through numbers from 1 to N
    for i in range(1, N + 1):
        # Assign an empty list to each node in the graph
        graph[i] = []
    
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))  # Since the roads are bi-directional
    
    # Step 2: Initialize Dijkstra’s Algorithm
    INF = float('inf')  # Set a large value for infinity
    # Initialize a dictionary to store the minimum time for each node
    min_time = {}

    # Iterate through numbers from 1 to N
    for i in range(1, N + 1):
        # Set each node's initial time to INF (a large predefined value)
        min_time[i] = INF
    
    min_time[1] = 0  # The restaurant is at town 1, so its distance is 0
    
    visited = set()  # Keep track of visited towns
    
    while len(visited) < N:
        # Step 3: Find the unvisited town with the smallest known delivery time
        current_town = -1
        current_time = INF
        for town in range(1, N + 1):
            if town not in visited and min_time[town] < current_time:
                current_town = town
                current_time = min_time[town]
        
        # If no town is found, break (this happens when all reachable towns are visited)
        if current_town == -1:
            break
        
        # Mark the current town as visited
        visited.add(current_town)
        
        # Step 4: Update the shortest path for neighbors
        for neighbor, travel_time in graph[current_town]:
            if neighbor not in visited:
                new_time = min_time[current_town] + travel_time
                if new_time < min_time[neighbor]:
                    min_time[neighbor] = new_time
    
    # Step 5: Count the number of towns that can receive food within time K
    return sum(1 for town in min_time if min_time[town] <= K)

# Example Test Cases
print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))  # Output: 4
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))  # Output: 4
