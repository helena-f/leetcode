pairs = [
    ("P1", "B1"),
    ("P2", "B1"),
    ("P3", "B2"),
    ("P4", "B2"),
    ("P1", "B3"),
    ("P5", "B3"),
    ("P6", "B4")
]
from collections import defaultdict
def get_pins(pairs):
    board_to_pins = defaultdict(set)
    for pin, board in pairs:
        board_to_pins[board].add(pin)

    pins_to_pins = {}
    for pins in board_to_pins.values():
        for pin_first in pins:
            for pin_second in pins:
                if pin_first not in pins_to_pins:
                    pins_to_pins[pin_first] = set()
                if pin_first != pin_second:
                    pins_to_pins[pin_first].add(pin_second)


    return {p:sorted(list(pins)) for p, pins in pins_to_pins.items()} 

print(get_pins(pairs))

from collections import deque
def clusters(pairs):
    graph = get_pins(pairs)
    
    clusters = []
    visited = set()
    for pin in graph:
        # bfs on each pin
        if pin not in visited:
            q = deque([pin])
            cluster = []
            while q:
                curr = q.popleft()
                visited.add(curr)
                cluster.append(curr)
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        q.append(neighbor)
            if cluster:
                clusters.append(sorted(cluster))

    return clusters

print(clusters(pairs))