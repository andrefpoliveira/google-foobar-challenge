from sys import maxsize

def find_shortest_path(m):
    h, w = len(m), len(m[0])
    min_path = h*w

    looking = [(0,0)]
    found = []
    parent = {}
    while len(looking) > 0:
        x, y = looking.pop(0)

        if (x,y) in found:
            continue

        found.append((x,y))
        for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
            sx, sy = x+dx, y+dy
            if sx < h and sx >= 0 and sy < w and sy >= 0:
                if m[sx][sy] == 1:
                    continue

                if (sx, sy) == (h-1, w-1):
                    p = 2
                    while (x, y) != (0, 0):
                        p += 1
                        x, y = parent[(x, y)]
                    return p

                looking.append((sx, sy))
                if (sx, sy) not in parent.keys():
                    parent[(sx, sy)] = (x, y)
                
    return min_path

def allMazes(m):
    yield m
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 1:
                m[i][j] = 0
                yield m
                m[i][j] = 1

def solution(m):
    sol = maxsize
    for matrix in allMazes(m):
        sol = min(sol, find_shortest_path(matrix))
    return sol
