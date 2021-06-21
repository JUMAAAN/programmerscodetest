def solution(progresses, speeds):
      answer=[]
      front=0
      rear=len(speeds)
      c=progresses
      while(front<rear):
            c=list(map(lambda x,y: x+y,c,speeds))
            if c[front]>=100:
                  count=1
                  front+=1
                  for z in range(front,rear):
                        if c[z]>=100:
                              front+=1
                              count+=1
                        else:
                              break
                  answer.append(count)                
      return answer

progresses=[95, 90, 99, 99, 80, 99]
speeds=[1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))
