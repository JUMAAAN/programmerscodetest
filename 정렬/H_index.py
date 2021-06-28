def solution(citations):
      answer=0
      hindex=0
      length=len(citations)
      if length<=min(citations):
            return length
      else:
            citations.sort()
            while(citations[hindex]<=length-hindex):
                  if citations[hindex]==length-hindex:
                        return citations[hindex]
                  hindex+=1
                  if hindex==length:
                        break
      answer=length-hindex      
      return answer

print(solution([0,0,0]))
