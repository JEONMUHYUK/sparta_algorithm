from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


#   방문 저장 여부 visited 생성.
#   공이 2개??
#   4차원 배열 사용.
#               n               m               n               m
#   visited[red_marble_row][red_marble_col][blue_marble_row][blue_marble_col]
#   보드의 행과 열의 길이가 3이상 10이하 -> 3 <= x <= 10
def move_untile_wall_or_hole(r, c, diff_r, diff_c, game_map):
    move_count = 0
    while game_map[r + diff_r][c + diff_c] != "#" and game_map[r][c] != "0":
        r += diff_r
        c += diff_c
        move_count += 1
    return r, c, move_count


def is_available_to_take_out_only_red_marble(game_map):
    n, m = len(game_map), len(game_map[0])
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1
    queue = deque()
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_row, red_col = i, j
            elif game_map[i][j] == "B":
                blue_row, blue_col = i, j
    queue.append((red_row, red_col, blue_row, blue_col, 1))
    visited[red_row][red_col][blue_row][blue_col] = True

    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()
        if try_count > 10:
            break

        for i in range(4):
            next_red_row, next_red_col, r_count = move_untile_wall_or_hole(red_row, red_col, dr[i], dc[i], game_map)
            next_blue_row, next_blue_col, b_count = move_untile_wall_or_hole(blue_row, blue_col, dr[i], dc[i], game_map)

            if game_map[next_blue_row][next_blue_col] == "O":
                continue
            if game_map[next_red_row][next_red_col] == "O":
                return True
            if next_red_row == next_blue_row and next_red_col == next_blue_col:
                if r_count > b_count:
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]

            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_count + 1))
    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다