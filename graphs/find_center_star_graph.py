class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """

        return (edges[0][0] if edges[0][0] in edges[1] else edges [0][1])
        
        # edge [2, 1] also means [1, 2]
        # counts = {}
        # for i, j in edges:
        #     if j in counts:
        #         counts[j] += 1
        #     else:
        #         counts[j] = 1
        #     if i in counts:
        #         counts[i] += 1
        #     else:
        #         counts[i] = 1

        #     if counts[i] == len(edges):
        #         return i
        #     if counts[j] == len(edges):
        #         return j

        # return -1