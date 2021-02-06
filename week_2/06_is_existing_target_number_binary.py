finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    current_min = 0 # 인덱스
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2
    find_count = 0
    while current_min <= current_guess:
        find_count += 1
        if array[current_guess] == target:
            print(find_count)
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess -1

        current_guess = (current_min + current_max) // 2
    return False




result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
    #  1번 탐색하면 반절이 줄어드니 N/2 개가 남는다.
    #  2번 탐색하면 반 절이 줄어드니 N/4 = N/2² 가 남는다.
    #  시간 복잡도 N / 2ᴷ = 1 이다 즉, k = log₂N 인 걸 알 수있다.
    #  상수는 무시해도 되기 때문에 즉, "O(logN)" 만큼 걸린다.