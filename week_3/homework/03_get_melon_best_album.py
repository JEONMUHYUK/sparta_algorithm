genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

#  장르 별(key)로 우선 재생된 횟수(value)를 저장해야 합니다.
#  장르별 곡의 정보(인덱스, 재생횟수) 배열로 묶어 저장
def get_melon_best_album(genre_array, play_array):
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}
    n = len(genre_array)

    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict: #dict가 비었다면
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]
        else:  # dict의 값이 있다
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])
    print(genre_total_play_dict)
    print(genre_index_play_array_dict)
    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item:item[1], reverse=True)
    print(sorted_genre_play_array)
    result = []
    for genre, value in sorted_genre_play_array:
        index_play_array = genre_index_play_array_dict[genre]
        sorted_index_play_array = sorted(index_play_array, key=lambda item:item[1], reverse=True)
        print(sorted_index_play_array)

        for i in range(len(sorted_index_play_array)):
            if i > 1:
                break
            result.append(sorted_index_play_array[i][0])  # i번째 원소의 0번째 원소를 넣는다는 의
    return result

#  lamda = 특정인자를 받아서 어떤 값으로 돌려줄 건지를 간단한 수식으로 표현
#  sorted(a.item() key=lamde item:item[1])
#  sorted(배열, key=lamda )
#  item:item[1]  -> item 을 받아서 item[1]로 반환하겠다
#  즉, 뒤에 있는 value 값을 정렬하겠다 라는 의미가 된다.
print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!