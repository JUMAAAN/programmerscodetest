def solution(n, lost, reserve):
      answer=n-len(lost)
      lostcontroll=[]
      lost.sort()
      reserve.sort()
      for i in lost:
            if i in reserve:
                  answer+=1
                  reserve.remove(i)
                  lostcontroll.append(i)
      for i in lostcontroll: 
            if i in lost:
                  lost.remove(i)
      #자급자족 제거
      for i in lost:
            if i-1 in reserve:
                  answer+=1
                  reserve.remove(i-1)
            elif i+1 in reserve:
                  answer+=1
                  reserve.remove(i+1)
      return answer

print(solution(5, [2, 3, 4], [3, 4, 5]))
