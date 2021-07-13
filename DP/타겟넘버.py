def solution(numbers, target):
      answer=0
      templist=[numbers[0],-numbers[0]]
      for i in numbers[1:]:
            templist=plusminus(i,target,templist)
      answer=templist.count(target)
      return answer

def plusminus(number,target,templist):
      tmp=[]
      for i in templist:
            tmp.append(i+number)
            tmp.append(i-number)
      return tmp

print(solution([1,1,1,1,1],3))
