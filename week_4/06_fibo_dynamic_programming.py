input = 100

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}

#  메모에 있다면 그 값을 바로 반환
#  없으면 아까 수식대로 구한다
#  그리고 그 값을 다시 메모에 기록한다.

#  Fibo(100) -> Fibo(99) -> Fibo(98)..... = Top Down 방식
#  Fibo(1)  ->  Fibo(2) ... = Top Up

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo


print(fibo_dynamic_programming(input, memo))