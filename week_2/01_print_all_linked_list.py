class Node: # node_class
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)  # Node 클래스를 호출해서 해드 데이터값 입력.

    def append(self, data):
        cur = self.head  # cur = linked_list 첫번째 노드값.
        while cur.next is not None:  # linked_list 다음 노드 값이 None 이 아닐 동안. 즉, 노드값이 끝까지 이동해야 된다.
            cur = cur.next  # cur 은 다음 노드로 이동.
        cur.next = Node(data)  # cur.next는 다음 노드값을 받는다.
        print(cur.data)

    def print_all(self):  # 노드 전체 출력 함수
        cur = self.head  # 마찬가지로 cur 을 head 값으로 변수 지정.
        while cur is not None:  # cur이 none이 아닐 동안.
            print(cur.data)  # 즉, 위에는 전체 스캔후 추가 하였다면 여기는 None값이 나오기 전까지 출력.
            cur = cur.next


linked_list = LinkedList(3) # LinkedList head 값 입력.
linked_list.append(4)  # append 함수에 next 를 추가한다.
linked_list.append(5)
linked_list.print_all()