def findroot(node,root):
      if root[node]==node:
            return node
      p=findroot(root[node],root)
      root[node]=p
      return root[node]

def findcycle(node1, node2,rank, root):
      node1=findroot(node1,root)
      node2=findroot(node2,root)
      if node1==node2:
            return 1#cycle
      if rank[node1]>rank[node2]:
            root[node2]=node1
      else:
            root[node1]=node2
      if rank[node1]==rank[node2]:
            rank[node1]+=1

def solution(n,costs):
      answer=0
      rank=[0]*n
      root=[i for i in range(n)]
      sortcost=sorted(costs, key=lambda x:x[2])#크루스칼 가중치 오름차순
      for node1, node2, weight in sortcost:
            print(root, rank)
            if findcycle(node1, node2, rank, root):
                  continue #cycle 
            else:
                  answer+=weight
      return answer

      
print(solution(5, [[0,1,1],[0,4,5],[2,4,1],[2,3,1],[3,4,1]]))
