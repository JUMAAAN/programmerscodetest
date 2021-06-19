def solution(genres, plays):
      total={}
      length=len(genres)
      answer=[]
      for i in range(length): # 장르별 회수 초기화
            total[genres[i]]=0
      for i,z in zip(genres, plays):
            total[i]+=z# 장르별 회수 최대값 구하기
      genleng=len(total.keys())#장르 숫자 구하기
      genline=sorted(total,key=lambda x:total[x], reverse=True)# max->min list
      a=[]#play list
      for i in range(genleng):
            temp=[]
            for genre, play in zip(genres, plays) :
                  if genre==genline[i]:
                        temp.append(play)
            temp.sort(reverse=True)
            a.append(temp)
      for i in range(genleng):
            for z in range(len(a[i])):
                  y=0#index
                  count=0 # 2개곡 카운트 
                  if len(answer)==(i+1)*2:
                        break
                  for genre, play in zip(genres, plays):
                        if genre==genline[i] and play==a[i][z]:
                              answer.append(y)
                              count+=1
                        if count==2:
                              break
                        y+=1  
      return answer

genres=["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"]
plays=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(solution(genres, plays))
