def solution(brown, yellow):
    answer = []
    divisorset=[]#약수 세트
    area=brown+yellow#넓이
    for i in range(1,int(area**0.5)+1):# n이하 수 ma표현 m or a는 루트n 이하 
          if area%i==0:#약수
                divisorset.append((i,area//i))#튜플셋트
    for i, z in divisorset:
          if brown==(z+i)*2-4:
                answer=[z,i]
                break
    return answer

print(solution(10,2))
