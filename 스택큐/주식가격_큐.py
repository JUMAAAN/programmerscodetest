def solution(prices):
      answer=[]
      pricequeue=prices
      front=0
      rear=len(prices)
      while(front!=rear):
            count=-1
            for i in range(front,rear):
                  count+=1
                  if pricequeue[front]-pricequeue[i]>0 or i==rear-1:
                        front+=1
                        answer.append(count)
                        break

      return answer

prices=[1,2,3,2,3]
print(solution(prices))
