from collections import deque

def process_samples(arrival_times):
    """
    Simulates the synthesis machine processing samples.
    
    Args:
        arrival_times: List of integers representing when each sample arrives
        
    Returns:
        Total time to process all non-rejected samples (int)
    """
    SYNTHESIS_TIME = 300
    MAX_QUEUE_SIZE = 10
    
    # Sort arrival times to process chronologically
    arrivals = sorted(arrival_times)
    
    queue = deque()  # Cooling chamber (FIFO)
    machine_free_at = 0  # When machine becomes available
    
    for arrival in arrivals:
        # If machine is free when sample arrives, process immediately
        if arrival >= machine_free_at:
            machine_free_at = arrival + SYNTHESIS_TIME
        # If machine is busy, try to add to queue
        elif len(queue) < MAX_QUEUE_SIZE:
            queue.append(arrival)
        # Queue is full, reject sample (do nothing)
    
    # Process remaining samples in queue
    while queue:
        queue.popleft()
        machine_free_at = machine_free_at + SYNTHESIS_TIME
    
    return machine_free_at


# Example usage and test cases
if __name__ == "__main__":
    # Test Case 1: Simple sequential arrivals
    print("Test Case 1: Sequential arrivals")
    arrivals1 = [1, 6, 9, 312]
    result1 = process_samples(arrivals1)
    print(f"Arrivals: {arrivals1}")
    print(f"Total time: {result1}")
    print()
    
    # Test Case 2: All samples arrive at once (queue overflow)
    print("Test Case 2: 15 samples arrive at time 0")
    arrivals2 = [0] * 15
    result2 = process_samples(arrivals2)
    print(f"Arrivals: 15 samples at time 0")
    print(f"Total time: {result2} (11 samples processed, 4 rejected)")
    print()
    
    # Test Case 3: Mixed timing
    print("Test Case 3: Mixed arrival times")
    arrivals3 = [0, 10, 20, 30, 500, 600, 700]
    result3 = process_samples(arrivals3)
    print(f"Arrivals: {arrivals3}")
    print(f"Total time: {result3}")
    print()
    
    # Test Case 4: Queue fills up and empties
    print("Test Case 4: Queue dynamics")
    arrivals4 = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 1000]
    result4 = process_samples(arrivals4)
    print(f"Arrivals: {arrivals4}")
    print(f"Total time: {result4}")