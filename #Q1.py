#Q1

def solution(my_string, target):
    answer = 1 if target in my_string else 0
    return answer

# 테스트
result = solution("abcdef", "abcd")
print(result)  

result = solution("abcdef", "ghij")
print(result)  