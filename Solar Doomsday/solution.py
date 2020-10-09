import math
    
def solution(area):
    res = []
    while area >= 1:
        x = int(math.sqrt(area))
        res.append(x*x)
        area -= x*x

    return res
