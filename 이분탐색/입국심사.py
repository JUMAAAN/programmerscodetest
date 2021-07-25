def solution(n, times):
    left=0
    right=max(times)*n
    middle=min(times)*n
    while(left+1<right):
        count=0
        for i in times:
            count+=middle//i
        if n<=count: #answer n==
            right=middle
            middle=(right+left)//2
        else:
            left=middle
            middle=(right+left)//2
    return right
