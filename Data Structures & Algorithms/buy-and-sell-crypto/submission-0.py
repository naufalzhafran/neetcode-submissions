class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        maxVal = 0

        for j in range(len(prices)):
            if prices[i] > prices[j]:
                i = j
            else:
                maxVal = max(prices[j] - prices[i], maxVal)

        return maxVal

        