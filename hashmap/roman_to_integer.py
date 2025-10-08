class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #step 1: break down test cases to understand question
        # XXVII -> 27
        # 10 + 10 + 5 + 1 + 1

        # XLIX -> 49
        # -10 + 50 - 1 + 10

        # step 2: talk through brute force plan
        
        # step 3: outline optimal solution. get ok from interviewer

        # map roman numerals to number
        symbol_int_map = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        # test: XLIX
        integer_num = 0
        # loop through s to get each numeral and convert to digit
        for i in range(len(s) - 1): # using i + 1 # s[0] = X, L

            # get map[s[i]] ie. map["M"] = 1000
            curr_val = symbol_int_map[s[i]] # currval = 10, 50

            # deal with IV and IX
            # if s[i+1] is > curr, we subtract curr instead of adding
            if symbol_int_map[s[i+1]] > curr_val: # s[i+1] = L -> 50 > 10, 1 < 50
                integer_num -= curr_val # 0-10 = -10
            else:
            # add to result ie. res += 1000
                integer_num += curr_val # -10+ 50 = 40
        # add the final char
        integer_num += symbol_int_map[s[-1]]

        # return the final added integer 
        return integer_num

        # step 4: walk through with test case
