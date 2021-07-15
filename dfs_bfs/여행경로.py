import copy as cp

def solution(tickets):
      answer=[]
      firstnode=[]
      temp=[]
      for i in tickets:
            if i[0]=='ICN':
                  firstnode.append(i) #인천출발
      for i in firstnode:
            stack=['ICN']
            dfs(i,tickets,stack,temp)
      answer=min(temp)
      return answer


def dfs(listnode,tickets,stack,temp):#listnode=[출발,도착]
      clone=cp.deepcopy(tickets)
      clone.remove(listnode)
      arri=listnode[1]
      stack.append(arri)
      for i in clone:
            if i[0]==arri:
                  dfs(i,clone,stack,temp)
      if clone==[]:
            tmp=cp.deepcopy(stack)
            temp.append(tmp)
            stack.pop()
      else:
            stack.pop()
            
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
