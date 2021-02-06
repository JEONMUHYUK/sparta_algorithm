shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]
# 집합자료형 함순는 = set() -> 중복 허용x


# O(N) + #O(M) = #O(N+M)
def is_available_to_order(menus, orders):
    menus_set = set(menus)  #O(N)
    for order in orders: #M
        if order not in menus_set: #O(1)
            return False

    return True

    '''# O((M+N) * logN)
    menus.sort()  # 정렬의 시간 복잡도는 배열의 길이 N이라고 한다면 시간복잡도는
    # O(N * log M)
    for order in orders:  # O(m * log N)
        if not is_existing_target_number_binary(order, menus):
            return False

    return True'''


def is_existing_target_number_binary(target, array):
    current_min = 0  # 인덱스
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2
    while current_min <= current_guess:

        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1

        current_guess = (current_min + current_max) // 2
    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)
