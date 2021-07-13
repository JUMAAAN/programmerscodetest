def solution(n,computers):
      answer=0
      visited=[False]*n
      graph=[[]for x in range(n)]
      for i in range(n):
            for j in range(len(computers[i])):
                  if i==j or computers[i][j]==0:
                        continue
                  graph[i].append(j)
      for i in range(n):
            if not visited[i]:
                  dfs(graph,i,visited)
                  answer+=1
      return answer

def dfs(graph,v,visited):
      visited[v]=True
      for i in graph[v]:
            if not visited[i]:
                  dfs(graph,i,visited)

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
