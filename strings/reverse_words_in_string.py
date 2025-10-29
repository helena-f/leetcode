class Solution:
    def reverseWords(self, s: str) -> str:
        partition = s.split(" ")
        reverse = []
        for i in range(len(partition) -1, -1, -1):
            if partition[i] != "":
                reverse.append(partition[i])
        return " ".join(reverse)