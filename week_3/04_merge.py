array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    array_c = []
    array_index_1 = 0
    array_index_2 = 0

    while array_index_1 < len(array1) and array_index_2 < len(array2):
        if array1[array_index_1] < array2[array_index_2]:
            array_c.append(array1[array_index_1])
            array_index_1 += 1
        else:
            array_c.append(array2[array_index_2])
            array_index_2 += 1
    if array_index_1 == len(array1):
        while array_index_2 < len(array2):
            array_c.append(array2[array_index_2])
            array_index_2 += 1
    else:
        while array_index_1 < len(array1):
            array_c.append(array1[array_index_1])
            array_index_1 += 1

    return array_c


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!