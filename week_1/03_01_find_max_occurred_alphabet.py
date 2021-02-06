input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i,", "j", "k", "l", "m", "n",
                      "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # 알파벳 리스트 -26개의 공간사용
    max_occurrence = 0 # -1개의 공간 사용
    max_alphabet = alphabet_array[0] # -1개의 공간 사용

    for alphabet in alphabet_array: # alphabet_array 의 길이(26)만큼 아래연산
        occurrence = 0 # -1개의 공간 사용/ 대입연산 1번 실행
        for char in string : #string의 길이 만큼 아래 연산 실행
            if char == alphabet: #비교연산 1번 실행
                occurrence += 1 # -1개의 공간 사용 / #대입연산 1번 실행

        if occurrence > max_occurrence: #비교연산 1번 실행

            max_occurrence = occurrence # -1개의 공간 사용 / #대입연산 1번 실행
            max_alphabet = alphabet # -1개의 공간 사용 / #대입연산 1번 실행

    return max_alphabet


result = find_max_occurred_alphabet(input) # -1개의 공간 사용
print(result)

#공간 복잡도는 저장공간을 기준으로 계산한다.
# 총 36개의 공간이 사용되었다.
# 알고리즘의 성능은 공간에 의해서 결정되지 않는다 고로 시간복잡도에 신경을 더 써야한다.
#시간복잡도는 26*(1+2*N+3) = 52N+104