def solution(name):
      answer=0
      length=len(name)
      namelist=[]
      for i in name: #리스트화
            namelist.append(i)
      currentindex=0
      for i in name:#수직이동 완료
            if i<='N':
                  answer+=ord(i)-65
            else:
                  answer+=91-ord(i)
      namelist[0]='A'#첫자리 제일먼저 수정
      while(namelist!=['A']*length):
            print(namelist, currentindex)
            leftcount=0
            rightcount=0
            for i in range((length//2)+1):#우측이동계산
                  if namelist[(currentindex+i)%length]!='A':
                        break
                  rightcount+=1
            for i in range((length//2)+1):#좌측이동계산
                  if namelist[currentindex-i]!='A':
                        break
                  leftcount+=1
            if rightcount>leftcount:#좌측이동 빠름
                  currentindex=currentindex-leftcount
                  if currentindex<0:
                        currentindex+=length
                  namelist[currentindex]='A'
                  answer+=leftcount
            else:
                  currentindex=(currentindex+rightcount)%length
                  namelist[currentindex]='A'
                  answer+=rightcount
      return answer

print(solution("JAN"))
