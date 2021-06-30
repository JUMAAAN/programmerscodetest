def solution(n, lost, reserve):
    student=[]
    answer=0
    for i in range(n):
        student.append(1)
        if (i+1) in reserve:
            student[i]+=1
        if (i+1) in lost:
            student[i]-=1
    for i in range(n-1):
        if student[i]==0:
            if student[i+1]==2:
                student[i+1]-=1
                student[i]+=1
            elif student[i-1]==2:
                if i-1<0:
                    continue
                student[i-1]-=1
                student[i]+=1
    if student[n-1]==0 and student[n-2]==2:
        student[n-1],student[n-2]=1,1
    answer=n-student.count(0) 
    return answer
