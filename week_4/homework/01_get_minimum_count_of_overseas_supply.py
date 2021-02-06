import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


#  현재 재고가 바닥나는 시점 이전까지 받을 수 있는
#  라면 중 제일 많은 라면을 받는 게 목표이다.

#  현재 재고의 상태에 따라 최곳값을 받아야 된다.(동적으로 변경되는 상태)
#  제일 많은 값만 가져가면 된다.

#  데이터를 넣을 때 마다 최솟/최대값을 동적으로 변경시키며
#  최솟/최대값을 바로 꺼낼 수 있는 자료구조

#  -> Heap 을 쓰자.


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    current_day_index = 0  # 날짜 지정. 몇일인지 알아야 재고가 얼마나 남았는지 알 수 있다.
    max_heap = []  # 현재 공급량이 떨어지지 않는 선에서 가장 많은 공급량을 가져올수있는 supply 값을 가져올수 있게.
    while stock < k:  # 공급일자 보다 재고가 작을 때 까지 즉, 재고가 많으면 끝낼 수 있다. 1 번.
        for date_index in range(current_day_index, len(dates)):
            if dates[date_index] <= stock:
                heapq.heappush(max_heap, -supplies[date_index])
            else:
                current_day_index = date_index
                break
        answer += 1
        stock += -heapq.heappop(max_heap)
    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
