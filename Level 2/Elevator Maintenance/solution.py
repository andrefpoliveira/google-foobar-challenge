def solution(l):
    splitted = [x.split(".") for x in l]
    beforeSorting = [map(int, e) for e in splitted]
    sort = sorted(beforeSorting)
    return [(".".join(str(x) for x in e)) for e in sort]
