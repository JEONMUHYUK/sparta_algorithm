top_heights = [6, 9, 5, 7, 4]


# 맨 뒤쪽이 없어진다 -> stack
def get_receiver_top_orders(heights):
    answer = [0] * len(heights)  # [0, 0, 0, 0, 0] -> 0으로 초기화 하여 삽입
    while heights:  # O(N^2)
        height = heights.pop()  # -> 하나 씩 줄여 나간다. height 가 존재하는 동안. 즉, height의 값은 4 -> 7 -> 5 -> 9 -> 6
        #  [6, 9, 5, 7]
        for idx in range(len(heights) - 1, 0, -1):  # 3에서 하나씩 줄여 나간다. O(N)
            if heights[idx] > height:  # 만약 heights[3](3) > height(4) 보다 크다면
                answer[len(heights)] = idx + 1  # 현재 주어진 스택의 길이 즉 answer[4] -> answer[3] -> ...
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
