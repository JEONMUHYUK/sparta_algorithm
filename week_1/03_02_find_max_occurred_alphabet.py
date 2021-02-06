input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0]*26

    for char in string:
        if not char.isalpha():
            continue #띄어쓰기 제거

        array_index = ord(char) - ord("a") #string을 구성하는 char을 아스키문자를 이용하여 인덱스로 사용할 숫자로 변형
        alphabet_occurrence_array[array_index] += 1 #위에서 뽑은 숫자를 인덱스에 사용하여 배열의 숫자를 증가시켜준다
        # ord["a"] - ord["a"] = 0 /아스키 = ord["a"] = 76
        #alphabet_occurrence_array[0] += 1  -> [1, 0, 0, 0, 0...]

    max_occurence = 0 #지정변수
    max_alphabet_index = 0

    for index in range(len(alphabet_occurrence_array)): #인덱스를 사용하기 위해 len을 사용.
        alphabet_occurrence = alphabet_occurrence_array[index]# 반복문을 사용해 alphabet_occurrence 변수를 사용

        if alphabet_occurrence > max_occurence:
            # 위에서 반복되고있는 alphabet_occurence의 alphabet_occurrence_array[index]가 0이라면
            # 3>0이 되기 때문에 if문이 실행된다.
            max_alphabet_index = index
            # max_alphabet_index는 가장 큰 수의 index와 같아진다.
            max_occurence = alphabet_occurrence
            #max_occurence가 0 -> 3 이 되어 if문은 alphabet_occurrence > 3으로 바뀌어 3보다 작은수는 걸러진다
    print(max_alphabet_index)

    result = chr(max_alphabet_index + ord("a"))
    # 위에서 찾은 가장 큰 인덱스인 max_alphabet_index(0) 을 ord("a")(76)을 합해 아스키문자 수를 만들어준다.
    # 아스키 문자를 다시 알파벳으로 구해야 하기 때문에 그 위에 chr 아스키함수를 이용하여 덮어씌어주면, chr(76)이 되어
    # "a" 가 구해진다.
    return result


result = find_max_occurred_alphabet(input)
print(result)