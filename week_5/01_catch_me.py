from collections import deque

c = 11
b = 2


#   코나의 위치 변화
#   코니는 처음 위치에서 1초후 1만큼, 매초마다 이전 이동거리 +1 만큼 움직인다.
#   즉, 증가하는 속도가 1초마다 1씩 증가.
#   속도 : 1, 2, 3, 4, 5, 6,..
#   시간에 따라 더 해주면 된다.
#    1 2 3 4  5
#   3 4 6 9 13 18

#   브라운의 위치 변화.
#   B - 1, B + 1, 2 * B

#   모든 경우의 수 나열 -> BFS를 사용.
#   잡았다! 는 똑같은 시간에 똑같은 위치에 존재.
#   시간은 + 1
#   위치는 코니도 브라운도 값이 자유자재.
#   규칙적 -> 배열 / 자유자재 -> dict

#   각 시간마다 브라운이 갈 수 있는 위치를 저장
#   visited = [{} for _ in range(200001)] -> 시간과 위치를 알고 있으면 즉각적으로 알수있는 자료구조.
#   visited [0] = {   -> 0은 time
#       2: True    -> location
#   }
#   visited [1] = {
#       1: True,
#       3: True,
#       4: True
#   }
#   즉, visited[time][cony_loc] 하면 도달했는지 도달하지 않았는지 알 수 있다.
#   즉, visited[위치][시간] -> visited[3] 에 5 라는 키가 있냐? 라고 하면 3위치에 5초에 간 적이 있냐? 이다.
#   0   1   2   -> visited[2] = { 0 : True, 2 : True}
#   2 ->1   0   -> visited[1] = { 1 : True }
#       3   2   -> visited[3] = { 1 : True }
#       4   3   -> visited[4] = { 1 : True }

def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))  # 위치와 시간을 동시에 담아준다. 즉, 위치와 시간이 같아야 만났다라고 할 수 있기 때문.
    visited = [{} for _ in range(200001)]  # -> 200000만개의 딕셔너리를 배열 안에 넣는다는 의미

    while cony_loc <= 200000:
        cony_loc += time  # 시간만큼 이동 즉, +1 +2 +3 +4..
        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()

            new_time = current_time

            new_position = current_position - 1
            if 0 <= new_position <= 200000:
                queue.append((new_position, new_time))
            new_position = current_position + 1
            if 0 <= new_position <= 200000:
                queue.append((new_position, new_time))
            new_position = current_position * 2
            if 0 <= new_position <= 200000:
                queue.append((new_position, new_time))

    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!
