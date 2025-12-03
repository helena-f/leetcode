#routes[0] = [1, 5, 7]]

#th: 1 -> 5 -> 7 -> 1 -> 5 -> 7 ...

#source (not a bus stop)
#target (bus stop)

# Example 1:
                    # 0.     1
# Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

# Example 2:

# Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# Output: -1

# input: routes = [[1,2],[3,4]] source = 2, target = 1
# output: 1

# input: routes = [[1,2],[2,3, 4], [2,4]], source = 1, target = 4
# output: 2

# input: routes = [[1,2],[2,3, 4], [3, 4]], source = 1, target = 4
# output: 2

# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 10^5
# routes are natural numbers

# undirected, weighted graph
# edge weights between route is 0, between buses is 1

# algorithm
# build adjacency list
# bfs, starting from source
# how do i keep track of jumping between routes
# 
# once reach target, then i know it's possible

# stop_to_routes = {
#     1: [0],              # Stop 1 is on route 0
#     2: [0],              # Stop 2 is on route 0
#     7: [0, 1],           # Stop 7 is on routes 0 AND 1
#     3: [1],              # Stop 3 is on route 1
#     6: [1]               # Stop 6 is on route 1
# }
# original example
# routes = [[1, 2, 7], [3, 6, 7]]
# source = 1
# target = 6

from collections import defaultdict, deque

def bus_routes(routes, source, target):
    if source == target:
        return 0
    
    min_transfers = 1

    stop_to_routes = defaultdict(list)
    for i, route in enumerate(routes):
        for bus_stop in route:
            stop_to_routes[bus_stop].append(i)

    visited_routes = set() # set of routes visited
    visited_stops = set([source])
    q = deque([source])
    while q:
        curr_routes = q.popleft()
        visited_routes.add(curr_routes)

        for route in stop_to_routes[curr_routes]:

            if route not in visited_routes:

                for stop in routes[route]:
                    if stop == target:
                        return min_transfers
                    if stop not in visited_stops:
                        visited_stops.add(stop)
                        q.append(stop)
            
            min_transfers += 1
        
        

        
    return -1


routes = [[1, 2, 7], [3, 6, 7]]
source = 1
target = 6
print(bus_routes(routes, source, target))