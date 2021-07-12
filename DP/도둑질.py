def solution(money):
    answer=0
    dp1=[]#마지막 포함 첫 삭제
    for i in range(1,3):
        dp1.append(money[-i])
    for i in range(3,len(money)-1):
        templist=[]
        for j in range(0,i-1):
            templist.append(dp1[j]+money[-i])
        dp1.append(max(templist))
    return answer
