numbers = [1, 1, 1, 1, 1]
target_number = 3

#  [2, 3] -> +2 +3 , +2 -3,  -2 +3, -2 -3

result_count = 0
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
    if current_index == len(numbers):
        if current_sum == target:
            global result_count
            result_count += 1
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1, current_sum + numbers[current_index]) #get_all_ways_to_by_doing_plus_or_minus(arrat, 1 , 0, 0 + 2, all_ways)
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1, current_sum - numbers[current_index]) #get_all_ways_to_by_doing_plus_or_minus(arrat, 1 , 0, 0 - 2, all_ways)




print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0))  # 5를 반환해야 합니다!
print(result_count)


# call by object reperance : 함수 내에서는 외부에 있는 변수를  찾지 못한다 즉, 리턴시 초기화를 시키기 때문에 global이라는 함수를 사용.
# global 함수 외의 변수를 사용가능하게 해준다.