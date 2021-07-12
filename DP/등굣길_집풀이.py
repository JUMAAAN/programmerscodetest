def solution(m, n, puddles):
<<<<<<< HEAD
    answer=0
    matrix=[[0]*(m+1) for x in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1:
                matrix[1][1]=1 #시작점
            elif [i,j] in puddles:
                matrix[i][j]=0#웅덩이
            else:
                matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
    print(matrix)
    answer=matrix[n][m]%1000000007
    return answer

print(solution(5,4,[[2,1],[2,2],[2,3],[4,4],[4,3],[4,2]]))
=======
      answer=0
      matrix = [[0]*(n+1) for i in range(m+1)]
      for i,j in puddles:
            matrix[i][j]=-1
      matrix[1][1]=1
      queue=[[1,1]]#u,d,l,r 저장/ 시작점 
      while():
            dodirect(queue.pop(0),matrix)

def dodirect(indexlist,matrix):
      
>>>>>>> d3eaab5e2a590fcbd4227009abd1c56f76560d49
