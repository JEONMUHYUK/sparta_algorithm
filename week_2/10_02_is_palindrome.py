input = "abcba"


def is_palindrome(string):
    if string[0] != string[-1]:
        return False
    elif len(string) <= 1:
         return True
    return is_palindrome(string[1:-1]) # 탈출문에 걸리지 않을 시 string이 앞뒤 한칸씩 줄어들어 다시 실행 된다.

# 반복해결문일시 재귀함수를 쓰자





print(is_palindrome(input))