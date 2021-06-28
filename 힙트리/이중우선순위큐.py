def solution(operations):
      answer=[]
      for op in operations:
            order, num=op.split()[0], int(op.split()[1])
            if order=='I':
                  answer.append(num)
            elif order=='D':
                  if len(answer)>0:      
                        if num==1:
                              answer.remove(max(answer))
                        elif num== -1:
                              answer.remove(min(answer))
                  else:# 삭제 원소 x
                        continue 
            else:# 예외처리
                  print("wrong order")
      if answer==[]:
            return [0,0]
      else:
            return [max(answer),min(answer)]


print(solution(["I 16","D 1"]))
