def solution(m, n, puddles):
    answer = 0
    Matrix = [[0]*(n+1) for i in range(m+1)]#다 1로 세팅
    for i,j in puddles:
        Matrix[i][j]=-1#웅뎅이 0으로 구분
    Matrix[1][1]=1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if m==n==1:
                continue
            if Matrix[i][j]==-1:
                Matrix[i][j]=0
                continue
            else:
                Matrix[i][j]=Matrix[i][j-1]+Matrix[i-1][j]
    answer=Matrix[m][n]%1000000007
    return answer
solution(4,5,[[2, 2],[3,4]])
