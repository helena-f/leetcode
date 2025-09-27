class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n == 1:
            return 1
        # if town judge exists, incoming edges are n - 1
        # outgoing edges is 0
        # there can't be two town judges if incoming edges are n - 1
        counts_incoming = {}
        counts_outgoing = {}
        for i, j in trust:
            # i trusts -> j
            if j in counts_incoming:
                counts_incoming[j] += 1
            else:
                counts_incoming[j] = 1
            if i in counts_outgoing:
                counts_outgoing[i] += 1
            else:
                counts_outgoing[i] = 1
            
        for i, j in trust:
            if counts_incoming[j] == n - 1 and j not in counts_outgoing:
                return j
          
        return -1