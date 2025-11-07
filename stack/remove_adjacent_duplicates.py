stack = []  # Each element: [char, count]

        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()  # remove the k duplicates
            else:
                stack.append([ch, 1])

        # Rebuild string
        return "".join(ch * count for ch, count in stack)

            