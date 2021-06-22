def solution(priorities, location):
      answer=0
      qqq=priorities
      front=0
      rear=len(qqq)
      maxprior=qqq.index(max(qqq))
      while(qqq[maxprior]!=-1):
            for i in range(rear):
                  if qqq[front]==qqq[maxprior]:
                        qqq[front]=-1
                        maxprior=qqq.index(max(qqq))
                        answer+=1
                        print(front)
                        if front==location:
                              return answer
                        break
                  front=(front+1)%rear
                                    
      return answer


print(solution(	[1, 1, 9, 1, 1, 1], 0))
