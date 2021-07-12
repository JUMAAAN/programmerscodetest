def solution(money): #시간초과 
    answer=0
    dp1=[]#마지막 포함 첫 삭제
    dp2=[]#마지팍 포함 x 첫 포함
    for i in range(1,3):
        dp1.append(money[-i])
        dp2.append(money[-i-1])
    for i in range(3,len(money)):
        templist1=[]
        templist2=[]
        for j in range(0,i-2):
            templist1.append(dp1[j]+money[-i])
            templist2.append(dp2[j]+money[-i-1])
        print(templist1,templist2)
        dp1.append(max(templist1))
        dp2.append(max(templist2))
    answer=dp1+dp2
    answer=max(answer)
    return answer
print(solution([91,90,5,7,5,7]))
