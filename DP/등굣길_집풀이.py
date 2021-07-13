def solution(m, n, puddles):
    answer=0
    matrix=[[0]*(m+1) for x in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1:
                matrix[1][1]=1 #시작점
            elif [j,i] in puddles:
                matrix[i][j]=0#웅덩이
            else:
                matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
    print(matrix)
    answer=matrix[n][m]%1000000007
    return answer

print(solution(5,4,[[2,1],[2,2],[2,3],[4,4],[4,3],[4,2]]))

