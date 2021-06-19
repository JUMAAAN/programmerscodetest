def solution(genres, plays):
      answer=[]
      totaldict={}
      playsum={}
      playindex=[]
      for i in genres:
            playsum[i]=0
            totaldict[i]=[]
      for i,z,y in zip(genres, plays, range(len(plays))):
            totaldict[i].append([z,y])
            playsum[i]+=z
      genline=sorted(playsum, key=lambda x: playsum[x], reverse=True)
      for x in genline:
            temp=[]
            for i in totaldict[x]:
                  temp.append(i)
            temp.sort(key= lambda x: (x[0],-x[1]),reverse=True)
            playindex.append(temp)
      for i in playindex:
            count=0
            for z in i:
                  if count==2:
                        break
                  answer.append(z[-1])
                  count+=1
      return answer


genres=["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"]
plays=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

print(solution(genres, plays))
