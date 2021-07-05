def solution(numbers,k): # N^2으로 풀이 불가 
      answer=''
      numberlist=[]
      maxindex=0
      endindex=k+1
      for i in numbers:
            numberlist.append(i)
      if k==1:
            numberlist.remove(min(numberlist))
            for i in numberlist:
                  answer+=i
            return answer
      templist=[]
      while(maxindex+1!=endindex and endindex-1!=len(numbers)):
            slicing=numberlist[maxindex:endindex]
            maxvalue='0'
            memoindex=0
            for i in range(len(slicing)):
                  if slicing[i]==9:
                        memoindex=i
                        break
                  if slicing[i]>maxvalue:
                        memoindex=i
                        maxvalue=slicing[memoindex]
            maxindex=memoindex+maxindex+1
            answer+=maxvalue
            endindex+=1
      if endindex-1!=len(numbers):
            for i in numberlist[maxindex:]:
                  answer+=i
      return answer
print(solution("9998887776665554443332221110009",30))
