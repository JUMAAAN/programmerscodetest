def solution(priorities, location):
    answer = 0
    total=len(priorities)
    while priorities != []:
        mac=max(priorities)
        top=priorities.pop(0)
        print(location)
        print("탑",top)
        print(mac)
        if top != mac :
            priorities.append(top)
            if location==0:
                location=len(priorities)-1
            else:
                location-=1
        if top == mac:
            if location==0:
                answer=total-len(priorities)
                return answer
            else:
                location-=1

print(solution([2, 1, 3, 2], 2))
