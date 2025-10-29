class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()

        i = 0
        while (i < len(strs[0]) and i < len(strs[-1]) 
                and strs[0][i] == strs[-1][i]):
            i += 1
        
        return strs[0][:i]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len = float("inf")

        for word in strs:
            min_len = min(min_len, len(word))

        prefix = []
        
        for i in range(min_len):
            ch = strs[0][i]
            is_common = True
            for word in strs:
                if word[i] != ch:
                    is_common = False

            
            if is_common:
                prefix.append(ch)
            else:
                break

        return "".join(prefix)