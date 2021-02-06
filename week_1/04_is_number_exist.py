input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for n in array:  # array 의 길이만큼 아래의 연산이 실행된다.
        if number == n:  # 비교연산이 1번 실행된다.
            return True  # N * 1 = N
    return False


result = is_number_exist(3, input)
print(result)

  #점근 계산법
  # 입력값이 좋을때는 1이고 안 좋을때는 N이 된다.
  # 즉 O(N), Ω(1)의 시간 복잡도를 가진 알고리즘이다.