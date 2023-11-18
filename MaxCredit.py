# Author: Simeng Li
# Dynamic Programming

"""
Question:

You have n class homeworks to work on in your algorithms class, and each is worth 100 points. Because you’ve procrastinated, you can’t hope to finish all the homeworks completely, and have to try to maximize your partial credit. You have h hours total to spend among these homeworks.
You are given an nx(h + 1) array points, where points[i][j] contains the points you will get for assignment i if your spend exactly j hours on that assignment.
You are given that points[i][0] = 0 (0 time = 0 points), points[i][j] <= points[i][j + 1] (more time on an assignment doesn’t decrease points).
For example, for n = 3, you might be given the below input:
      points = [ [0, 50, 75,  90,  100, 100, 100],
                 [0, 80, 100, 100, 100, 100, 100],
                 [0, 40, 70,  80,  90,  93,  100] ]
Your goal is to allocate your available hours to these assignments in order to maximize your total points.
"""

points = [[0, 30, 60, 100, 100, 100],
         [0, 25, 90, 100, 100, 100],
         [0, 30, 70, 100, 100, 100]]


# Explanations of the returned results:
# The integer (mpc[n-1][h-1]) is the maximum score I can get
# The first list (problems) records the problem indexes that I am going to do
# The second list (timeforProblem) records the number of hours I am going to do for each corresponding problem

def MaxPC(A):
    n = len(A)
    h = len(A[0])

    # Create my Array
    mpc = list([0] * h for _ in range(n))
    Jump = list([0] * h for _ in range(n))

    # Base Cases
    # recursive
    for i in range(0, n):
        for j in range(h):
            if i == 0:
                mpc[0][j] = A[0][j]
                Jump[i][j] = j

            m = A[i][j]
            for k in range(0, j):
                if mpc[i-1][j-k] + A[i][k] > m:
                    m = mpc[i-1][j-k] + A[i][k]
                    Jump[i][j] = k
                mpc[i][j] = m
    print(n, h)
    # print(Jump)
    #return mpc[n-1][h-1]

    # Recovering the solution
    curH = h-1
    problems = []
    timeforProblem = []

    for i in range(n-1,-1,-1): #i .... 1
        if Jump[i][curH] != 0:
            problems.append(i)
            timeforProblem.append(Jump[i][curH])
        curH -= Jump[i][curH]
    problems.reverse()
    timeforProblem.reverse()

    return mpc[n-1][h-1], problems, timeforProblem

print(MaxPC(points))
