def solution(money): #시간초과 
    answer=0
    dp1=[]#마지막 포함 첫 삭제
    dp2=[]#마지팍 포함 x 첫 포함
    for i in range(1,3):
        dp1.append(money[-i])
        dp2.append(money[-i-1])
    for i in range(2,len(money)-1):
        dp1.append(max(dp1[i-2]+money[-i-1],dp1[i-1]))
        dp2.append(max(dp2[i-2]+money[-i-2],dp2[i-1]))
        print(dp1,dp2)
    answer=dp1+dp2
    answer=max(answer)
    return answer
print(solution([90, 0, 0, 95, 1, 1]))
