def solution(m, n, puddles):
      answer=0
      matrix = [[0]*(n+1) for i in range(m+1)]
      for i,j in puddles:
            matrix[i][j]=-1
      matrix[1][1]=1
      queue=[[1,1]]#u,d,l,r 저장/ 시작점 
      while():
            dodirect(queue.pop(0),matrix)

def dodirect(indexlist,matrix):
      
