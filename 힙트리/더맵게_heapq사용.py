import heapq as hp

def solution(scoville, K):
      answer=0
      heaptree=[]
      heaptree=scoville
      hp.heapify(heaptree)#N복잡도
      root=heaptree[0]
      while(len(heaptree)>=2):#N복잡도-> NlogN
            if root >=K:
                  break
            first=hp.heappop(heaptree)#logN복잡도
            second=hp.heappop(heaptree)
            newone=first+(second*2)
            hp.heappush(heaptree,newone)
            answer+=1
            root=heaptree[0]
      if root<K:
            return -1
      return answer
