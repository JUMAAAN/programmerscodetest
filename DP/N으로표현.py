def solution(N,number):
      dp=[]
      for i in range(8):#최대 8
            dp.append([])
      dp[0].append(N)#F1=N, F1=dp[0] 1차이
      dp[1]=[N+N,N-N,N*N,int(N/N),N*11]# F2 F2=dp[1]
      if number in dp[0]:
            return 1
      if number in dp[1]:
            return 2
      for i in range(2,8):
          dp[i]=makedp(dp,i,N)
          print(dp[i])
          if number in dp[i]:
                return i+1
      return -1 #8번 안에 못 찾음
      

def makedp(dp,i,N):
      templist=[]
      count='1'
      for j in range(0,i):
            count+='1'
            for x in dp[j]:
                  for z in dp[i-j-1]:
                        templist.append(x+z)
                        templist.append(x-z)
                        templist.append(x*z)
                        if z!=0:
                              templist.append(int(x/z))
      templist.append(N*int(count))
      return templist
                        
print(solution(5,12))
