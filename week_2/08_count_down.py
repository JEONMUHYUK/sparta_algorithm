def count_down(number):
    if number < 0:
        return
    print(number)  # number를 출력하고
    count_down(number - 1)  # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(60)

#  즉, 자기 자신을 다시 부르는 것을 재귀함수라고 한다.
