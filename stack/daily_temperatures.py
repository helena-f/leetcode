# monotonic decreasing or equal stackclass MonotonicStack:


    def daily_temperatures(self, temperatures):
        n = len(temperatures)
        result = [0] * n  # Result array initialized with 0s
        stack = []  # Monotonic decreasing stack

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)

        return result