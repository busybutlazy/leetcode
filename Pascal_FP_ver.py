def pascal(n:int) -> list[list]:
    if n==1:
        return [[1]]
    if n>=2:
        tmp=pascal(n-1)
        tmp.append([1])
        for i in range(len(tmp[-2])-1):
            tmp[-1].append(tmp[-2][i]+tmp[-2][i+1])
        tmp[-1].append(1)
        return tmp                     




print(pascal(30))