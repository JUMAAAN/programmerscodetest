def solution(triangle):
    answer=0
    dp=[]
    dp.append(triangle[0])
    dp2=[triangle[0][0]+triangle[1][0],triangle[0][0]+triangle[1][1]]
    dp.append(dp2)
    for i in range(2,len(triangle)):
            dp.append(makedp(i,triangle[i],dp))
    answer=max(dp[len(dp)-1])
    return answer

def makedp(index,triangle,dp):
    templist=[]
    templist.append(dp[index-1][0]+triangle[0])
    for i in range(1,len(triangle)-1):
        slicing=dp[index-1][i-1:i+1]
        templist.append(max([triangle[i]+slicing[0],triangle[i]+slicing[1]]))
    templist.append(dp[index-1][-1]+triangle[-1])
    return templist
    

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
