finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]  # 이진 탐색은 배열이 순차적일때만 가능.

def is_exist_target_number_binary(target, numbers):
    for n in numbers:
        if target == n:
            return True
    return False

result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)