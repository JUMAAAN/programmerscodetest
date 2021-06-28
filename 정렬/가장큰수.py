def solution(numbers):
      answer=''
      if max(numbers)==0:
            return '0'
      temp=list(map(str,numbers))
      temp=sorted(temp, key=lambda y:y+y[0]+y[-1],reverse=True)
      for i in temp:
            answer+=i
      return answer

print(solution([6,646] ))
