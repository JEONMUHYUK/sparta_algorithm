class MaxHeap:
    def __init__(self):
        self.items = [None]

    #  새 노드를 맨 끝에 추가한다.
    #  지금 넣은 새 노드를 부모와 비교한다. 만약 부모보다 크다면 교체한다.
    #  반복.
    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:
            parent_index = cur_index // 2  # 부모 인덱스는 자식인덱스 // 2
            if self.items[cur_index] > self.items[parent_index]:
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
                cur_index = parent_index

            else:
                break
        return

    #  완전 이진 트리의 최대 높이는 O(lg(N))
    #  반복하즉는 최대 횟수도 O(log(N))
    #  즉, 맥스 힙의 원소 추가는 O(log(N))


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!
