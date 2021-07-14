def solution(tickets):
      answer=[]
      firstnode=[]
      for i in tickets:
            if i[0]=='ICN':
                  firstnode.append(i) #인천출발

      for i in firstnode:
            answer+=dfs(i,tickets)
      return answer


def dfs(listnode,tickets):#listnode=[출발,도착]
      visted=tickets
      visted.remove(listnode)
      temp=[]
      if visted==[]:#올바른 경로
            return listnode[1]
      arrive=listnode[1]
      for i in visted:
            if i[0]==arrive:
                  temp.append(listnode[1]+dfs(i,visted))
      return temp

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
