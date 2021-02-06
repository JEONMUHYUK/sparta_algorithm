input = "abcba"


def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n-1-i]: # n-1은 고정값으로 남기 때문에 인덱스의 지속적인 비교를 위해 i를 붙인다
            # 예를 들면 string[0] != string[5-1-0] -> string[1] != string[5-1-1]
            return False
    return True





print(is_palindrome(input))