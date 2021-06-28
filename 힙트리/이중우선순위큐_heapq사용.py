import heapq as hp
def solution(operations):
      answer=[]
      total=0
      for op in operations:
            order, num=op.split()[0], int(op.split()[1])
            if total==0:
                  minheap=[]
                  maxheap=[]
            if order=='I':
                  hp.heappush(minheap,num)
                  hp.heappush(maxheap,(-num,num))
                  total+=num
            elif order=='D':
                  if total==0:
                        continue
                  else:
                        if num==1:
                              total-=hp.heappop(maxheap)[1]
                        else:
                              total-=hp.heappop(minheap)
      if total==0:
            return [0,0]
      else:
            return[hp.heappop(maxheap)[1],hp.heappop(minheap)]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
