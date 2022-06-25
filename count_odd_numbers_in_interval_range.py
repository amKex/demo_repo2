class Solution:
    def countOdds(self, low: int, high: int) -> int:
        list_t = []
        countOdd = 0
        for i in range(low,(high+1)):
            t = i
            list_t.append(t)
            
        for val in list_t:
            if val%2 != 0:
                countOdd = countOdd + 1

        return countOdd

# i solved this question at leetcode by my own