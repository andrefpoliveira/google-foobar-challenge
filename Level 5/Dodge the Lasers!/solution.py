from math import sqrt, floor

def s(n):
    if n==0: return 0

    sqrt = "414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641572735013846230912297024924836055850737212644121497099935831"
    _n = str(int(sqrt)*n)[:-156]
    if not _n: _n = 0
    else: _n = int(_n)

    return (_n + n) * (_n + n + 1)/2 - _n*(_n+1) -  s(_n)

def solution(n):
    return str(int(s(int(n))))
