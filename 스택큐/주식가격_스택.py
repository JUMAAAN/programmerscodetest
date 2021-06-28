def solution(prices):
      answer=[]
      stostack=prices#스택에 저장
      minvalue=min(stostack)#O(N)
      for i in range(len(prices)-1):#O(N)
            temp=stostack.pop(0)#O(N)으로 스택 풀이 불가.0(N^2)
            if temp==minvalue:
                  answer.append(len(stostack))
                  continue
            z=0
            while(z!=len(stostack)):#O(N^3)
                  if temp>stostack[z]:
                        z+=1
                        break
                  z+=1
            if z==0:
                  z=1
            answer.append(z)
      answer.append(0)                 
      return answer


prices=[1]*10000
print(solution(prices))
