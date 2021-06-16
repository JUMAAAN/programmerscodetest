def solution(phone_book):
    answer = True
    hashtable={}
    for i in phone_book:
        hashtable[i]=1
    for i in phone_book:
        temp=''
        for z in i:
            temp+=z
            if temp in hashtable and i!= temp:
                  print(temp, i)
                  return False
    return answer

phone_book=["119", "97674223", "1195524421"]
print(solution(phone_book))
