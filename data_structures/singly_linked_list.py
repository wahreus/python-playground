"""A singly linked list implementation."""


from dataclasses import dataclass


@dataclass
class Node:
    data: int
    next: "Node | None" = None


class SinglyLinkedList:
    def __init__(self, items: list[int]) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        for item in items:
            self.append(item)

    def append(self, item: int) -> None:
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        assert self.tail is not None
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, item: int) -> bool:
        current = self.head
        previous: Node | None = None
        while current is not None:
            if current.data == item:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                if current is self.tail:
                    self.tail = previous
                return True
            previous = current
            current = current.next
        return False

    def sort_list(self) -> None:
        values: list[int] = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        values.sort()
        self.head = None
        self.tail = None
        for value in values:
            self.append(value)

    def fetch_list(self) -> str:
        if self.head is None:
            return "(empty)"
        values: list[str] = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        return " ".join(values)

    def size(self) -> int:
        size = 0
        current = self.head
        while current is not None:
            size += 1
            current = current.next
        return size


def main() -> None:
    linked_list = SinglyLinkedList([4, 2, 7, 1, 9, 6, 5, 8, 3])

    print("Original list:")
    print(linked_list.fetch_list())

    linked_list.append(10)
    print("\nAfter appending 10:")
    print(linked_list.fetch_list())

    linked_list.remove(7)
    print("\nAfter removing 7:")
    print(linked_list.fetch_list())

    print(f"\nLength:\n{linked_list.size()}")

    linked_list.sort_list()
    print("\nSorted list:")
    print(linked_list.fetch_list())


if __name__ == "__main__":
    main()