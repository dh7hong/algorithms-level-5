def solution(book_time):
    # Convert "HH:MM" to total minutes
    def to_minutes(time_str):
        hh, mm = map(int, time_str.split(":"))
        return hh * 60 + mm

    events = []
    
    # Convert bookings into (start_time, +1) and (end_time + 10, -1)
    for start, end in book_time:
        events.append((to_minutes(start), 1))  # Check-in event
        events.append((to_minutes(end) + 10, -1))  # Check-out event (+10 min cleaning)

    # Sort events: first by time, then by type (-1 before +1 if equal)
    events.sort()

    # Count rooms in use
    max_rooms = 0
    current_rooms = 0

    for _, change in events:
        current_rooms += change
        max_rooms = max(max_rooms, current_rooms)

    return max_rooms

# Test Cases
print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))  # 3
print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))  # 1
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))  # 3
