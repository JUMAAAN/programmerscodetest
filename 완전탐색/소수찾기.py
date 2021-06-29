global numberscom
numberscom=[]

def makepermutation(listy,depth,n,k):
      if depth==k:
            numberscom.append(int("".join(listy[0:k])))
            return 0
      for i in range(depth,n):
            swap(listy,depth,i)
            makepermutation(listy,depth+1,n,k)
            swap(listy,depth,i)

def swap(listy,i,j):
      temp=listy[i]
      listy[i]=listy[j]
      listy[j]=temp

def solution(numbers):
      answer=0
      onenumber=[]
      for i in numbers:
            onenumber.append(i)
      for i in range(len(onenumber)):
            makepermutation(onenumber,0,len(onenumber),i+1)
      combe=set()
      combe.update(numberscom)#중복제거
      list(combe)
      for i in combe:
            if i==2:
                  answer+=1
            for z in range(2,i):
                  if i%z==0:
                        break
                  if z==i-1:
                        answer+=1
      return answer

print(solution("7843"))
