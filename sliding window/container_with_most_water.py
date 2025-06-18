class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
                
        maxh = 0

        l,r = 0, len(height) -1

        while l < r:
            currarea = (r-l) * min(height[l],height[r])
            if currarea > maxh:
                maxh = currarea
            
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maxh
    
    
    class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max = 0

        # multiply difference between the bar and the distance

        for i in range(len(heights)):
            for j in range(len(heights)):
                dist = abs(i - j)
                currarea = dist * min(heights[i],heights[j])
                if currarea > max:
                    max = currarea

        return max