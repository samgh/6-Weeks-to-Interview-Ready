"""
Title: Convert string into integer

Problem:
    Implement atoi which converts a string to an integer.

    The function first discards as many whitespace characters as necessary until
    the first non-whitespace character is found. Then, starting from this
    character, takes an optional initial plus or minus sign followed by as many
    numerical digits as possible, and interprets them as a numerical value.

    The string can contain additional characters after those that form the
    integral number, which are ignored and have no effect on the behavior of
    this function.

    If the first sequence of non-whitespace characters in str is not a valid
    integral number, or if no such sequence exists because either str is empty
    or it contains only whitespace characters, no conversion is performed.

    If no valid conversion could be performed, a zero value is returned.

    Note:

    Only the space character ' ' is considered as whitespace character.  Assume
    we are dealing with an environment which could only store integers within
    the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is
    out of the range of representable values, INT_MAX (231 − 1) or INT_MIN
    (−231) is returned.

Execution: python string_to_int.py
"""
import unittest


def string_to_int(s: str) -> int:
    """Convert string input to integer without `int` function."""

    # 0 positive: 1 negative
    sign = 0
    value = 0
    if len(s) == 0:
        return 0
    word = s.lstrip().split(" ")[0]
    if word == "":
        return 0
    if "0" <= word[0] <= "9" or word[0] == "-" or word[0] == "+":
        clean = word
    else:
        return 0

    if clean[0] == "-":
        unsigned = clean[1:]
        sign = 1
        if unsigned == "":
            return 0
        elif not unsigned[0] >= "0" and unsigned[0] <= "9":
            return 0

    elif clean[0] == "+":
        unsigned = clean[1:]
        sign = 0
        if unsigned == "":
            return 0
        elif not unsigned[0] >= "0" and unsigned[0] <= "9":
            return 0

    else:
        unsigned = clean

    # Truncate non-number part.
    for c in range(0, len(unsigned)):
        if unsigned[c] < "0" or unsigned[c] > "9":
            unsigned = unsigned[0:c]
            break

    # Truncate leading zeros.
    while unsigned != "":
        if unsigned[0] == "0":
            unsigned = unsigned[1:]
        else:
            break
    if unsigned == "":
        return 0
    if len(unsigned) > 10:
        if sign == 1:
            return -2147483648
        else:
            return 2147483647

    i = 0
    while i < len(unsigned):
        value = value * 10 + int(unsigned[i])
        if value > 2 ** 31 - 1 and sign == 0:
            return 2147483647
        elif value > 2 ** 31 and sign == 1:
            return -2147483648
        i += 1

    if sign == 1:
        value = 0 - value

    return value


class TestStringToInt(unittest.TestCase):
    """Unit tests for string_to_int."""

    def test_1(self):
        self.assertEqual(string_to_int("-42"), -42)

    def test_2(self):
        self.assertEqual(string_to_int("   -42"), -42)

    def test_3(self):
        self.assertEqual(string_to_int("4193 with words"), 4193)

    def test_4(self):
        self.assertEqual(string_to_int("words and 987"), 0)

    def test_5(self):
        self.assertEqual(string_to_int("-91283472332"), -2147483648)


if __name__ == "__main__":
    unittest.main()
