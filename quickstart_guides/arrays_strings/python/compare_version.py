"""
Title: Compare version

Problem:
    Compare two version numbers version1 and version2.  If version1 > version2
    return 1; if version1 < version2 return -1;otherwise return 0.

    You may assume that the version strings are non-empty and contain only
    digits and the . character.

    The . character does not represent a decimal point and is used to separate
    number sequences.

    For instance, 2.5 is not "two and a half" or "half way to version three",
    it is the fifth second-level revision of the second first-level revision.

    You may assume the default revision number for each level of a version
    number to be 0. For example, version number 3.4 has a revision number of 3
    and 4 for its first and second level revision number. Its third and fourth
    level revision number are both 0.

Execution: python compare_version.py
"""
import unittest


def compare_version(version1: str, version2: str) -> int:
    v1 = version1.split(".")
    v2 = version2.split(".")
    v = max(len(v1), len(v2))
    v1 = (v1 + ["0"] * v)[:v]
    v2 = (v2 + [0] * v)[:v]
    for i in range(0, v):
        if int(v1[i]) > int(v2[i]):
            return 1
        elif int(v1[i]) < int(v2[i]):
            return -1
        else:
            continue
    return 0


class TestCompareVersion(unittest.TestCase):
    """Unit tests for compare_version."""

    def test_1(self):
        self.assertEqual(compare_version("0.1", "1.1"), -1)

    def test_2(self):
        self.assertEqual(compare_version("1.0.1", "1"), 1)

    def test_3(self):
        self.assertEqual(compare_version("7.5.2.4", "7.5.3"), -1)

    def test_4(self):
        self.assertEqual(compare_version("1.01", "1.001"), 0)

    def test_5(self):
        self.assertEqual(compare_version("1.0", "1.0.0"), 0)


if __name__ == "__main__":
    unittest.main()
