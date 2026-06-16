"""A union-find implementation."""


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, first: int, second: int) -> None:
        root_first = self.find(first)
        root_second = self.find(second)
        if root_first != root_second:
            self.parent[root_second] = root_first

    def connected(self, first: int, second: int) -> bool:
        return self.find(first) == self.find(second)


def main() -> None:
    union_find = UnionFind(9)

    print("Each item in its own group:")
    print(union_find.parent)

    union_find.union(0, 1)
    union_find.union(1, 2)

    print("\nAfter connecting 0-1 and 1-2:")
    print("0, 1, and 2 now belong to the same group.")
    print(union_find.parent)

    union_find.union(3, 4)

    print("\nAfter connecting 3-4:")
    print("3 and 4 now belong to another group.")
    print(union_find.parent)

    print("\nIs 0 connected to 2?")
    print(union_find.connected(0, 2))

    print("\nIs 0 connected to 4?")
    print(union_find.connected(0, 4))

    union_find.union(2, 4)

    print("\nAfter connecting 2-4:")
    print("The groups {0, 1, 2} and {3, 4} are now merged.")
    print(union_find.parent)

    print("\nIs 0 connected to 4 now?")
    print(union_find.connected(0, 4))


if __name__ == "__main__":
    main()