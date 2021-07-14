def solution(begin, target, words):
    answer=0
    if target not in words:
        return 0
    temp=[[begin]] #bfs0
    for i in temp:# q
        if target in i:
            return answer
        temp.append(bfs(i,words))
        answer+=1

def bfs(item,words):
    temp=[]
    for i in item:
        for j in words:#q
            count=0
            for x,y in zip(i,j):
                if x!=y:
                    count+=1
            if count==1:
                temp.append(j)#한개차이
    return temp
