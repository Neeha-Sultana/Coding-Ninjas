"""
#BruteForce
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]<prices[j]:
                    if (prices[j]-prices[i])>diff:
                        diff=(prices[j]-prices[i])


                        
        return diff
"""
#Optimal
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        minPrice = float('inf')
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            maxPro = max(maxPro, prices[i] - minPrice)
        return maxPro
