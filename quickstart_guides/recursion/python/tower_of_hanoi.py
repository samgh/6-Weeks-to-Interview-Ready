"""
Title: Tower of Hanoi

Problem:
    Tower of Hanoi is a mathematical puzzle where we have three rods and n
    disks. The objective of the puzzle is to move the entire stack to another
    rod, obeying the following simple rules:

    1) Only one disk can be moved at a time.
    2) Each move consists of taking the upper disk from one of the stacks and
       placing it on top of another stack i.e. a disk can only be moved if it
       is the uppermost disk on a stack.
    3) No disk may be placed on top of a smaller disk.

Execution: python tower_of_hanoi.py
"""
import unittest


def tower_of_hanoi(n: int, from_rod: str, to_rod: str, aux_rod: str):
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    tower_of_hanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    tower_of_hanoi(n - 1, aux_rod, to_rod, from_rod)


class TestTowerOfHanoi(unittest.TestCase):
    """Unit tests for tower_of_hanoi."""

    def test_1(self):
        n = 4
        tower_of_hanoi(n, "A", "C", "B")


if __name__ == "__main__":
    unittest.main()
