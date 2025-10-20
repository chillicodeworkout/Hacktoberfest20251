class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dfs(i, can_buy, transactions_left):

            if i == len(prices) or transactions_left == 0:
                return 0 

            if can_buy:
                ##here you can either buy or not buy
                #if you buy, you subtract current price(cuz you paid) and recursively call sell
                ##why not doing trancsation-1 in case of buy
                ##Because a transaction is only completed when you SELL, not when you buy.
                return max(
                    -prices[i] + dfs(i+1, False, transactions_left),  # buy
                    dfs(i+1, True, transactions_left)                 # not buy
                )
            else:
                return max(
                    prices[i]+dfs(i+1, True, transactions_left-1),
                    dfs(i+1, False, transactions_left)
                )

        return dfs(0, True, 2)
