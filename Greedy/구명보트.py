def solution(people, limit):
      answer=0
      people.sort(reverse=True)
      if people[0]+people[1]<=limit:
            if len(people)%2==0:
                  return len(people)//2
            else:
                  len(people)//2+1
      if people[-1]>limit//2:
            return len(people)
      #예외처리
      front=0
      rear=len(people)-1
      for i in people:
            if front>=rear:
                  if front==rear:
                        answer+=1
                  break
            if i+people[rear]<=limit:
                  answer+=1
                  front+=1
                  rear-=1
            else:
                  front+=1
                  answer+=1
      return answer
print(solution([70, 80, 50],100))
