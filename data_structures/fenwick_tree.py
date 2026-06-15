"""A Fenwick tree implementation."""


class FenwickTree:
    def __init__(self, size: int) -> None:
        self.tree = [0] * (size + 1)

    def add(self, index: int, value: int) -> None:
        index += 1
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

    def prefix_sum(self, stop: int) -> int:
        total = 0
        while stop > 0:
            total += self.tree[stop]
            stop -= stop & -stop
        return total

    def range_sum(self, start: int, stop: int) -> int:
        return self.prefix_sum(stop) - self.prefix_sum(start)


def main() -> None:
    values = [4, 2, 7, 1, 9, 6, 5, 8, 3]
    fenwick_tree = FenwickTree(len(values))
    for index, value in enumerate(values):
        fenwick_tree.add(index, value)

    print("Original values:")
    print(values)

    print("\nPrefix sum for values[:5]:")
    print(fenwick_tree.prefix_sum(5))

    print("\nRange sum for values[3:6]:")
    print(fenwick_tree.range_sum(3, 6))

    fenwick_tree.add(4, 10)
    print("\nRange sum for values[3:6] after increasing index 4 by 10:")
    print(fenwick_tree.range_sum(3, 6))


if __name__ == "__main__":
    main()