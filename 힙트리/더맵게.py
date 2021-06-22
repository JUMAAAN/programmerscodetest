def solution(scoville, K):
      answer=0
      root=-1
      global heaptree
      heaptree=[]
      heaptree.append(root)
      for i in range(len(scoville)):
            makeheaptree(scoville[i],i+1)
      while len(heaptree)>2:
            if heaptree[1]<K:
                  modiheaptree()
                  print(heaptree)
                  answer+=1
            else:
                  break
      if heaptree[1]>=K:
            return answer
      else:
            return -1


def makeheaptree(value, location):#minheaptree
      heaptree.append(value)
      if location==1:
            return 0 # don't touch root
      if value<=heaptree[int(location/2)]:
            elementswap(int(location/2),location)
            makeheaptree(value,int(location/2))
      
def elementswap(parient, child):
      temp=heaptree[parient]
      heaptree[parient]=heaptree[child]
      heaptree[child]=temp

def modiheaptree():
      first=delelement()
      second=delelement()
      newone=first+(second*2)
      print(heaptree,newone)
      makeheaptree(newone,len(heaptree))

      

def delelement():
      delnode=heaptree[1]
      if len(heaptree)<3:
            heaptree.pop()
            return delnode
      heaptree[1]=heaptree.pop()
      temp=1
      child=2
      while(child<len(heaptree)-1):
            if heaptree[child]>heaptree[child+1]:
                  child=child+1
            if heaptree[child]<=heaptree[temp]:
                  elementswap(temp,child)
                  temp=child
                  child*=2
            else:
                  break
      return delnode
      
      
      

scoville=[1,1,1]
K=4
print(solution(scoville,K))
