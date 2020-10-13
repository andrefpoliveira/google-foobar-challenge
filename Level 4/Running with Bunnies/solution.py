import itertools

def calculateCosts(perm, distances):
    end = len(distances)-1
    before = 0
    cost = 0
    for next in perm:
        cost += distances[before][next]
        before=next
    return cost + distances[before][end]

def BellmanFord(matrix, src, distances):
    distances[src][src] = 0
    size = len(matrix)

    for _ in range(size - 1):
        for u in range(size):
            for v in range(size):
                if distances[src][u] != float("Inf") and distances[src][u] + matrix[u][v] < distances[src][v]:
                    distances[src][v] = distances[src][u] + matrix[u][v]

    for u in range(size):
        for v in range(size):
            if distances[src][u] != float("Inf") and distances[src][u] + matrix[u][v] < distances[src][v]:
                return True

    return False

def calculateDistances(matrix):
    distances = [[float("Inf") for _ in range(len(matrix))] for _ in range(len(matrix))]
    negativeCycles = False
    for i in range(len(matrix)):
        negativeCycles = negativeCycles or BellmanFord(matrix, i, distances)

    return distances, negativeCycles
    
    
def solution(times, time_limit):
    numBunnies = len(times)-2
    bunnies = set(range(len(times))) - set([0, len(times)-1])

    distances, negativeCycles = calculateDistances(times)
    if negativeCycles:
        return [i for i in range(numBunnies)]

    maxBunnies = set([])
    for i in range(numBunnies+1):
        for perm in itertools.permutations(bunnies, i):
            cost = calculateCosts(perm, distances)
            
            if cost <= time_limit and (len(perm) > len(maxBunnies) or len(perm) == len(maxBunnies) and sum(perm) < sum(maxBunnies)):
                maxBunnies = set(perm)

    return list(map(lambda x: x-1, sorted(maxBunnies)))
