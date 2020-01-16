#Coin Change
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/809/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = [0] * (amount + 1)
        
        def coinChangeFor(amnt: int) -> int:
            if amnt < 0:
                return -1
            if amnt == 0:
                return 0
            if mem[amnt] != 0:
                return mem[amnt]
            minCoins = float('inf')
            for coin in coins:
                res = coinChangeFor(amnt - coin)
                if res > -1 and res < minCoins:
                    minCoins = res + 1
            mem[amnt] = -1 if minCoins == float('inf') else minCoins
            return mem[amnt]
            
        return coinChangeFor(amount)
