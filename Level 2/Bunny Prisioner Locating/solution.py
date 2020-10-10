def solution(x, y):
    idPrisioner = int((x*x + x)/2)
    for i in range(y-1):
        idPrisioner += x
        x+=1
        
    return str(idPrisioner)
