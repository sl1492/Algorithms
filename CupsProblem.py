# Author: Simeng Li
# Graph theory - BFS

"""
A classic puzzle is set up as follows. You are given three glasses of water that hold different amounts of water (for example 8 oz, 5 oz, and 4 oz), and you are next to a stream.
At each step, you can do one of the following things:
• Fill up any of the three cups with water from the stream. By doing this, the amount of water in that cup becomes fully filled to maximum capacity.
• Empty any of the cups into the stream. By doing this, the amount of water in that cup becomes 0.
• Pour water from one cup to any other cup until either the destination cup is full or the source cup is empty, which ever happens first.
After a sequence of such steps, your goal is to end up with a target t amount of water in the original cup (for example, t = 2oz).
"""

from collections import deque
import sys

# Create all the vertices
def create(x, y, z):
    G_a = {}
    for i in range(0, x+1):
        for j in range(0, y+1):
            for k in range(0, z+1):
                G_a[(i, j, k)] = 0
    return G_a

# Create all the actions/edges
def action(Vertices, A, B, C):
    G_a = create(A, B, C)
    for v in Vertices:
        actions = set()
        a = int(v[0])
        b = int(v[1])
        c = int(v[2])
# To empty:
        if a > 0:
            actions.add((0, b, c))
        if b > 0:
            actions.add((a, 0, c))
        if c > 0:
            actions.add((a, b, 0))
    # To fill:
        if a < A:
            actions.add((A, b, c))
        if b < B:
            actions.add((a, B, c))
        if c < C:
            actions.add((a, b, C))
    # To pour:
        # b to a
        if a < A and b > 0:
            aNew = a
            n = 1
            while aNew < A and n <= b:
                aNew += 1
                n += 1
            bNew = b-(n-1)
            actions.add((aNew, bNew, c))
        # a to b
        if b < B and a > 0:
            bNew = b
            n = 1
            while bNew < B and n <= a:
                bNew += 1
                n += 1
            aNew = a-(n-1)
            actions.add((aNew, bNew, c))
        # c to a
        if a < A and c > 0:
            aNew = a
            n = 1
            while aNew < A and n <= c:
                aNew += 1
                n += 1
            cNew = c-(n-1)
            actions.add((aNew, b, cNew))
        # a to c
        if c < C and a > 0:
            cNew = c
            n = 1
            while cNew < c and n <= a:
                cNew += 1
                n += 1
            aNew = a-(n-1)
            actions.add((aNew, b, cNew))
        # b to c
        if c < C and b > 0:
            cNew = c
            n = 1
            while cNew < C and n <= b:
                cNew += 1
                n += 1
            bNew = b-(n-1)
            actions.add((a, bNew, cNew))
        # b to c
        if b < B and c > 0:
            bNew = b
            n = 1
            while bNew < B and n <= c:
                bNew += 1
                n += 1
            cNew = c-(n-1)
            actions.add((a, bNew, cNew))
        G_a[v] = actions
    return G_a

# Finally Got here!!!!!!!BFS
def BFS(G, start):
  visited = {}
  visited[start] = 0
  q = deque()
  q.append(start)

  while(q):
    u = q.popleft()
    for neighbor in G[u]:
      if neighbor not in visited:
        visited[neighbor] = visited[u] + 1
        q.append(neighbor)
  return visited

# The main function
def Main(A, B, C, t):
    G = action(create(A, B, C), A, B, C)
    distances = BFS(G, (0, 0, 0))
    BestDist = sys.maxsize
    Best = None
    for i in range(0, B+1):
        for j in range(0, C+1):
            m = (t, i, j)
            if m in distances:
                if distances[m] < BestDist:
                    Best = BestDist
                    BestDist = distances[m]
    if Best == None:
        print("No solutions.")
    else:
        print("The shortest distance is : " + str(BestDist))

Main(8, 5, 4, 2)
Main(90, 70, 80, 10)
