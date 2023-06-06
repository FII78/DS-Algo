class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we can buy and sell multiple times 
        # after 1 buy we have to sell it first to buy another stock BSBSBS

        # two possibilities: can buy and can't buy
        # can buy: buy or not buy
        # can't buy: sell or not sell

        @cache

        def dfs(index,buy):
            if index == len(prices):
                return 0
            if buy:
                return max(-prices[index] + dfs(index+1, 0), dfs(index+1, 1))
            else:
                return max(prices[index] + dfs(index+1,1), dfs(index+1, 0))
                
        return dfs(0,1)
            



        