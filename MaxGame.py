# Author: Simeng Li
# Dynamic Programming

"""
You are playing a two player game. 
There are n cards, face up in front of you in a row, and each card has a positive integer labeled on it. 
You take turns either taking a card from either the beginning or end of the list of cards.

For example, if you were looking at the cards [222315], you would have to option of picking up either the last 5, 
leaving [22231] or the first 2, leaving [22315]. Then it would be Dr. Bhakta’s turn to choose a card, then yours, etc.
Play ends when all cards are gone. 

You goal is to get the highest sum possible for the cards you take. 
Note that this is a zero sum game - all the cards eventually are shared between you and your opponent, 
so maximizing your score is equivalent to minimizing your opponent’s score.
"""

cards = [8, 4, 1, 2, 1]
arr1 = [8, 15, 3, 7]
arr2 = [2, 2, 2, 2]
arr3 = [20, 30, 2, 2, 2, 10]


def maxGame(cards):
    n = len(cards)

    # Create the Array
    mSum = list([0] * n for _ in range(n))

    # Base case
    for i in range(n):
        for j in range(i, n):
            if i == j:
                mSum[i][j] = cards[i]
            elif j == i + 1:
                mSum[i][j] = max(cards[i], cards[j])

    # recursive Step
    for m in range(3, n + 1):
        for i in range(0, n - m + 1):
            j = i + m - 1
            if j > i + 1:
                mSum[i][j] = max((cards[i] + min(mSum[i + 1][j - 1], mSum[i + 2][j])),
                                 (cards[j] + min(mSum[i][j - 2], mSum[i + 1][j - 1])))
    # print(mSum)
    return mSum[0][n - 1]


print(maxGame(cards))
print(maxGame(arr1))
print(maxGame(arr2))
print(maxGame(arr3))

print(467)
