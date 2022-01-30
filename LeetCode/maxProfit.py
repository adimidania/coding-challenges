'''
You are given an array prices where
prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to
buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0
'''
# The most straightforward solution that came to my mind
# Obviousely, It's not optimal, because I don't know a lot about Dynamic Programming
def maxProfit(prices):
    buy = prices[0]
    day = 0
    for i in range(1,len(prices)):
        if(buy > prices[i]):
            buy = prices[i]
            day = i
    sell = buy
    for i in range(day,len(prices)):
        sell = max(sell, prices[i])        
    return sell - buy

# As usual, I made sure to look up for other solutions, 
# in order to improve my way of solving problems, and here's what I found
# There's one for loop that does the work for us.
# We just initialize the min to first element of the array, the diff to zero
# We loop through the array, and we update the the diff and the min
def maxProfitSolution(prices):
    minimum = prices[0]
    max_difference = 0
    for i in range(1, len(prices)):
        max_difference = max(max_difference, prices[i] - minimum)
        minimum = min(prices[i], minimum)
    return max_difference