import heapq as hp

#SPN으로 해결 
def solution(jobs):
      answer=0
      readyq=[]#heaptree
      waitq=[]#Q
      current_time=0
      jobs=sorted(jobs)
      z=0
      for i in range(len(jobs)):
            while z!=len(jobs):
                  if jobs[z][0]<=current_time:
                        hp.heappush(readyq,jobs[z][1])
                        waitq.append(jobs[z][0])
                        z+=1
                  else:
                        if len(readyq)==0:
                              current_time=jobs[z][0]
                              hp.heappush(readyq,jobs[z][1])
                              waitq.append(jobs[z][0])
                              z+=1
                        break
            runnode=hp.heappop(readyq)
            waittime=waitq.pop(0)
            answer+=current_time+runnode-waittime
            current_time=current_time+runnode
            
      return answer//len(jobs)

      
print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))
