input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    mutiply_sum = 0 #대입연산 1
    for number in array: #N
        if number <= 1 or mutiply_sum <= 1: #비교연산 1
            mutiply_sum += number #대입연산 1
        else :
            mutiply_sum *= number #대입연산 1

    return mutiply_sum

# 1+3N -> O(N)
result = find_max_plus_or_multiply(input)
print(result)