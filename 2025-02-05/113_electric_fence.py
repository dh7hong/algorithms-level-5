from collections import deque

def count_nodes(graph, start, n):
    """ Counts the number of nodes in a component using BFS """
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 1  # Start with one node

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:  # If not visited, add to queue
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    
    return count

def solution(n, wires):
    # Step 1: Convert wires into adjacency list
    graph = {i: [] for i in range(1, n + 1)}
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    min_difference = float('inf')  # Track minimum difference

    # Step 2: Try removing each edge and compute size difference
    for v1, v2 in wires:
        # Temporarily remove the connection (v1, v2)
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        # Count the size of one subnetwork (BFS from v1)
        count1 = count_nodes(graph, v1, n)
        count2 = n - count1  # Remaining nodes in the other network

        # Compute the difference and update min_difference
        min_difference = min(min_difference, abs(count1 - count2))

        # Restore the connection
        graph[v1].append(v2)
        graph[v2].append(v1)

    return min_difference