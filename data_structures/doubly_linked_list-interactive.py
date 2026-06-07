"""A doubly linked list implementation with an interactive command-line menu."""


from dataclasses import dataclass
import os


@dataclass
class Node:
    data: int
    prev: "Node | None" = None
    next: "Node | None" = None


class DoublyLinkedList:
    def __init__(self, items: list[int]) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        current: Node | None = None
        for item in items:
            new_node = Node(item)
            if current is None:
                self.head = new_node
            else:
                current.next = new_node
                new_node.prev = current
            current = new_node
        self.tail = current

    def append(self, item: int) -> None:
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        assert self.tail is not None
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def fetch_reversed_list(self) -> str:
        if self.head is None:
            return "(empty)"
        current = self.tail
        values: list[str] = []
        while current is not None:
            values.append(str(current.data))
            current = current.prev
        return " ".join(values)

    def __len__(self) -> int:
        size = 0
        current = self.head
        while current is not None:
            size += 1
            current = current.next
        return size

    def print_list(self) -> None:
        if self.head is None:
            print("(empty)")
            return
        current = self.head
        values: list[str] = []
        while current is not None:
            values.append(str(current.data))
            current = current.next
        print(" ".join(values))

    def remove(self, item: int) -> bool:
        if self.head is None:
            return False
        if self.head.data == item:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None
            return True
        current = self.head
        while current.next is not None:
            if current.next.data == item:
                removed_node = current.next
                current.next = removed_node.next
                if removed_node.next is not None:
                    removed_node.next.prev = current
                if removed_node is self.tail:
                    self.tail = current
                return True
            current = current.next
        return False

    def sort_list(self) -> None:
        values: list[int] = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        values.sort()
        sorted_list = DoublyLinkedList(values)
        self.head = sorted_list.head
        self.tail = sorted_list.tail


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def command_loop(linked_list: DoublyLinkedList) -> None:
    clear_screen()
    while True:
        print("Current list: ", end="")
        linked_list.print_list()
        print("____________________")
        command = input(
            "Command options:\n"
            "    1  append item\n"
            "    2  remove item\n"
            "    3  count items\n"
            "    4  sort list\n"
            "    5  print reverse\n"
            "    6  exit\n"
            "____________________\n"
            "Command: ")

        if command == "1":
            try:
                item = int(input("\nEnter item to append: "))
                linked_list.append(item)
            except ValueError:
                input(" - Please enter a valid integer. Press Enter to continue.")

        elif command == "2":
            try:
                item = int(input("\nEnter item to remove: "))
                removed = linked_list.remove(item)
                if not removed:
                    input(" - No matching item found.\n - Press Enter to continue.")
            except ValueError:
                input(" - Please enter a valid integer.\n - Press Enter to continue.")

        elif command == "3":
            size = len(linked_list)
            word = "item" if size == 1 else "items"
            input(f"\n - The list contains {size} {word}.\n - Press Enter to continue.")

        elif command == "4":
            linked_list.sort_list()

        elif command == "5":
            reversed_list = linked_list.fetch_reversed_list()
            input(f"\n - Reversed list: {reversed_list}\n - Press Enter to continue.")

        elif command == "6":
            print("\n - Goodbye!\n")
            break

        else:
            input(" - Invalid command.\n - Press Enter to continue.")

        clear_screen()


def main() -> None:
    numbers = [4, 2, 7, 1, 9, 6, 5, 8, 3]
    linked_list = DoublyLinkedList(numbers)
    command_loop(linked_list)


if __name__ == "__main__":
    main()