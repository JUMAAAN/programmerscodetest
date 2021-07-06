def solution(n,costs):
    answer=0
    visted=[0]*n
    graph={}
    visted[0]=1
    primnode=[0]
    count=0
    for i in range(n):
        graph[i]=[]
    for node1, node2, weight in costs:
        graph[node1].append([node2,weight])
        graph[node2].append([node1,weight])
    while(count<n-1):
        templist=[]
        for i in primnode:
            templist+=graph[i]
        templist=sorted(templist,key=lambda x:x[1])
        for node, weight in templist:
            if visted[node]==1:
                continue
            else:
                visted[node]=1
                answer+=weight
                primnode.append(node)
                break
        
        count+=1
    return answer

    
print(solution(5,[[0,1,1],[0,2,2],[1,2,5],[1,3,3],[2,3,8],[3,4,1]]))
