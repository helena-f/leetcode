class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # use binary search
        # create a function to determine if you can eat the bananas
        # if you can, try the decreased rate
        # if you can't, try the increased rate

        def hours_finish(rate, piles): 
            hours_taken = 0
            for pile in piles:
                # hours_taken += math.ceil(float(pile / rate))
                hours_taken += (pile + rate - 1) // rate
            return hours_taken
        
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2

            if hours_finish(mid, piles) > h:
                left = mid + 1
            else:
                right = mid 
        return left 

