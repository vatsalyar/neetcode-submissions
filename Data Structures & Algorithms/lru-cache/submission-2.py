class ListNode:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node: ListNode) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1
        node = self.hm[key]
        self._remove(node)
        self._add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self._remove(self.hm[key])
        
        node = ListNode(key, value)
        self.hm[key] = node
        self._add(node)
        
        if len(self.hm) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.hm[lru.key]