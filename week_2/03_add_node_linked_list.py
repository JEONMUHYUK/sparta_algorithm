class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):  # 원하는 index 에 value 값을 얻기 위해 둘 다 가져온다.
        new_node = Node(value)  # 새로 넣을 노드
        if index == 0:  # 만약 첫번째에 노드를 넣을 시 오류가 나기 때문에 예외처리를 해주어야 한다
            new_node.next = self.head  # 미리 new_node 다음이 self.head 임을 알려줘야 누락되지 않는다.
            self.head = new_node  # 그 후 head 를 new_node 로 지정
            return

        node = self.get_node(index - 1) # 현재 노드 index-1은 원하는 위치에 놓기위해 즉, -1을 하지 않으면 원하는 인덱스 그 다음 값에 추가된다.
        next_node = node.next  # 누락 되지 않기 위해 미리 다음 인덱스를 저장해둔다.
        node.next = new_node  # 현재 노드의 다음이 새로운 노드임을 알려준다.
        new_node.next = next_node  # 새로 저장된 노드 다음이 미리 잘라놓은 뒷 노드 값임을 알려준다.
        return

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
print(linked_list.get_node(1).data) # -> 5를 들고 있는 노드를 반환해야 합니다!
linked_list.add_node(1, 6)
linked_list.print_all()