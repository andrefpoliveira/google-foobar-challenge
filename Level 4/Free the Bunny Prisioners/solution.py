from itertools import combinations

def solution(num_buns, num_required):
    res = [[] for _ in range(num_buns)]
    copies_key = num_buns - num_required + 1
    
    for k, b in enumerate(combinations(range(num_buns), copies_key)):
        for bunnie in b:
            res[bunnie].append(k)

    return res
