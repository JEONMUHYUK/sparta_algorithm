from collections import deque

balanced_parentheses_string = "()))((()"

#   균형잡힌 괄호 문자열 -> 올바른 괄호 문자열

def is_correct_parenthesis(string):
    stack = []

    for s in string:
        if s == "(":
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0

def seperate_to_u_v(string):
    queue = deque(string)
    left, right = 0, 0  # "(", ")"의 개수를 세기위한 카운트 변수
    u, v = "", ""  # u,v 의 활용을 위해 빈문자열로 초기화
    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:  # left 와 right 가 같다면 균형잡힌 문자열 이것은 u 에다가 넣는다.
            break  # u가 균형잡인 괄호 문자열이 안되게 하기 위해  여기서 더이상 쌍이 안생기도록 멈추는것.

    v = ''.join(list(queue))
    return u, v

#   1. 입략이 빈 문자열인 경우, 빈 문자열 반환.
#   2. 문자열 w를 두 " 균형 잡힌 괄호 문자열 " u, v 로 분리.
#   단, u 는 " 균형잡힌 괄호 문자열" 로 더 이상 분리할 수 없어야 하며,
#   v 는 빈 문자열이 될 수 있다.
#   (  )개수 가 같아야 한다.
#   3. 문자열 u 가 올바른 괄호 문자열이라면 문자열 v에 대해
#   1단계부터 다시 수행.
#   3-1. 수행한 결과 문자열을 u에 이어붙인뒤 반환한다.
#   -> change_to_correct_parenthesis
#   4. 문자열 u가 올바른 괄호 문자열이 아니라면.
#   4-1. 빈 문자열에 첫 번째 문자로 (를 붙인다.
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자를 이어 붙인다.
#   4-3. )를 다시 붙인다.
#   4-4. u의 첫번째 문자와 마지막 문자를 제거 하고 , 나머지 문지열의 괄호를 뒤집어서 뒤에 붙인다.

def reverse_parenthesis(string):
    reversed_string = ""
    for char in string:
        if char == "(":
            reversed_string += ')'
        else:
            reversed_string += '('
    return reversed_string
def change_to_correct_parenthsis(string):
    if string == "":
        return ""
    u, v = seperate_to_u_v(string)

    if is_correct_parenthesis(u):
        return u + change_to_correct_parenthsis(v)

    else:
       return "(" + change_to_correct_parenthsis(v) + ")" + reverse_parenthesis(u[1:-1])



def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parenthesis(balanced_parentheses_string):
        return balanced_parentheses_string

    else:
        return change_to_correct_parenthsis(balanced_parentheses_string)



print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!