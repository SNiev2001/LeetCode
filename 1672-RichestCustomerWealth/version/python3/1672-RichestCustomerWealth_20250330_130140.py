# Last updated: 3/30/2025, 1:01:40 PM
# The best answer in terms of speed employs an external function max()
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Most efficent way to do it?
        # They are not asking for the customer row or id, they are only asking for a number
        # Store length as statics so we dont have to check every time
        '''
        Normal code withouth libraries
        money = 0
        total = 0
        for i in range(0, len(accounts)):
            for j in range(0,len(accounts[i])):
                print(i)
                print(j)
                total += accounts[i][j]
                if money < total:
                    money = total
            total = 0
        return money
        '''
        # Code with libraries
        return max(sum(i) for i in accounts)

        