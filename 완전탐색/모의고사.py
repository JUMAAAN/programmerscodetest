def solution(answers):
      answer=[]
      sol1=[1,2,3,4,5]
      sol2=[2,1,2,3,2,4,2,5]
      sol3=[3,3,1,1,2,2,4,4,5,5]
      count1=0
      count2=0
      count3=0
      for i in range(len(answers)):
            if sol1[i%5]==answers[i]:
                  count1+=1
            if sol2[i%8]==answers[i]:
                  count2+=1
            if sol3[i%10]==answers[i]:
                  count3+=1
      maxlist=[count1,count2,count3]
      maxvalue=max(maxlist)
      for i in range(3):
            if count1==maxvalue:
                  answer.append(1)
                  count1=0
            elif count2==maxvalue:
                  answer.append(2)
                  count2=0
            elif count3==maxvalue:
                  answer.append(3)
                  count3=0
      return answer

print(solution([1]))
