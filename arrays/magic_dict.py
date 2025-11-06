class MagicDictionary:

    def __init__(self):
        self.magic = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.magic = dictionary

    def search(self, searchWord: str) -> bool:
        for word in self.magic:
            if len(word) != len(searchWord):
                continue
            
            diff_count = 0
            for i in range(len(searchWord)):
                if searchWord[i] != word[i]:
                    diff_count += 1
                    
            if diff_count == 1:
                return True

        return False



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)