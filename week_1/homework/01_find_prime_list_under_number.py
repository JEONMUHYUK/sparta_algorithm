input = 20


def find_prime_list_under_number(number):
    prime_array = []
    for num in range(2, number+1):
        for i in prime_array:  # 반복문을 통해 계속해서 프라임 리스트가 추가되는 것을 이용하여 반복문 작성.
            if num % i == 0 and i * i <= num:  # num % i 가 0이 되는 것 뿐만 아니라
                # 해볼 필요도 없는 뒷 숫자 i*i가 num 보다 작을때의 숫자들만 이용해서 성능 개선!
                break
        else: prime_array.append(num)

    return prime_array


result = find_prime_list_under_number(input)
print(result)