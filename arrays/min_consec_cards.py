class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min_cards = float("inf")

        visited = {}
        for i in range(len(cards)):
            if cards[i] in visited:
                min_cards = min(min_cards, i - visited[cards[i]] + 1)
                visited[cards[i]] = i
            
            visited[cards[i]] = i

        
        if min_cards == float("inf"):
            return -1
        return min_cards