def solution(clothes):
    hashtable={}
    answer=1
    for i in clothes:
        hashtable[i[1]]=0
    length=len(hashtable)
    for i in clothes:
        hashtable[i[1]]+=1
    for i in hashtable.keys():
        n=hashtable[i]+1
        answer*=n
    return answer-1
