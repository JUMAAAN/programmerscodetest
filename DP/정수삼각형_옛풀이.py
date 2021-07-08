def solution(triangle):
    answer = 0
    clone=triangle[:]
    clone[0]=triangle[0]#바꾸면서 저장용
    for i in range(1,len(triangle)):
        for j in range(i+1):
            if j==0:#처음왼쪽 대각선 
                clone[i][j]=triangle[i][j]+clone[i-1][j]
            elif j==i:#맨끝오른쪽 대각선
                clone[i][j]=triangle[i][j]+clone[i-1][j-1]
            else: #평범 자기자식은 밑에 양옆
                clone[i][j]=triangle[i][j]+max([clone[i-1][j-1],clone[i-1][j]])
    answer=max(clone[len(triangle)-1])
    return answer
