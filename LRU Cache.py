"""
    Intuition:
    - We need a data structure that maintains the **most recently used** entries at the front
      and **least recently used** at the end, with constant-time access and eviction.

    Brute Force:
    - A naive approach is to use a **singly linked list** to track usage order.
    - But insertion/removal from the middle would take O(n) time, and so would searching for a key.

    Slight Improvement:
    - A **doubly linked list** allows O(1) removal and insertion once the node is found.
    - But finding the node still takes O(n) time.

    Optimal Design:
    - Use a **hashmap for O(1) access** and a **doubly linked list for O(1) ordering**.
    - Together, this forms a structure similar to a **LinkedHashMap** — combining quick lookup with ordered updates.

    Approaches:
    1. ✅ Hashmap + Doubly Linked List → O(1) time, O(n) space (Best for fast access + eviction)
    2. ❌ Doubly Linked List only → O(n) lookup, O(1) insert/remove
    3. ❌ Singly Linked List → O(n) lookup, O(n) insert/remove
"""

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}  # key -> node
        self.capacity = capacity

        # Dummy head and tail nodes to simplify edge ops
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1

        node = self.dict[key]

        # Move node to front (MRU)
        self.remove(node)
        self.add(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            # Remove old node
            self.remove(self.dict[key])

        # Insert new node at front
        node = ListNode(key, value)
        self.dict[key] = node
        self.add(node)

        # Evict LRU if over capacity
        if len(self.dict) > self.capacity:
            lru_node = self.tail.prev
            self.remove(lru_node)
            del self.dict[lru_node.key]

    def remove(self, node):
        """Disconnects a node from the linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        """Inserts a node right after head (marks as MRU)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node


# ----------------------------------------------------
# ❌ Singly Linked List Approach (Brute Force)
# ----------------------------------------------------
# Would maintain ordering of usage, but searching would take O(n),
# and removal from the middle would also be O(n).
# This is why we opted for hashmap + doubly linked list instead.

# ----------------------------------------------------
# Local Testing
# ----------------------------------------------------
if __name__ == "__main__":
    lru = LRUCache(2)

    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))  # Expected: 1

    lru.put(3, 3)  # Evicts key 2
    print(lru.get(2))  # Expected: -1

    lru.put(4, 4)  # Evicts key 1
    print(lru.get(1))  # Expected: -1
    print(lru.get(3))  # Expected: 3
    print(lru.get(4))  # Expected: 4
