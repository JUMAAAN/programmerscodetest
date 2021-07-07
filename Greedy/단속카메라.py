def solution(routes):
      answer=0
      visted=[0]*len(routes)
      sortroute=sorted(routes, key=lambda x: x[1])
      for i in range(len(visted)):
            if visted[i]==1:
                  continue
            else:
                  visted[i]=1
                  maxvalue=sortroute[i][1]
                  k=i+1
                  while(k<len(visted)):
                        if sortroute[k][0]<=maxvalue<=sortroute[k][1]:
                              visted[k]=1
                        k+=1
                  answer+=1                       
      return answer

