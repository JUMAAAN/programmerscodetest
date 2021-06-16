def solution(progresses, speeds):
    answer = []
    dayli=[]
    times=len(speeds)
    for i in range(times):
        day=0
        top=progresses.pop(0)
        speedtop=speeds.pop(0)
        while top<100:
            top=top+speedtop
            day+=1
        dayli.append(day)
    daytop=dayli.pop(0)
    count=1
    while(dayli != []):
        if daytop>=dayli[0]:
            count+=1
            dayli.pop(0)
        else:
            answer.append(count)
            count=1
            daytop=dayli.pop(0)
    
    answer.append(count)
    return answer
