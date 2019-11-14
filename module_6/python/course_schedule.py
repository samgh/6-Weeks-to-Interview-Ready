"""
Title: Course schedule

Problem:
    There are a total of n courses you have to take, labeled from 0 to n-1.

    Some courses may have prerequisites, for example to take course 0 you have to
    first take course 1, which is expressed as a pair: [0,1]

    Given the total number of courses and a list of prerequisite pairs, is it
    possible for you to finish all courses?

Execution: python course_scheule.py
"""
import unittest
from collections import defaultdict
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """Determines if it is possible to finish all courses."""
    def DFS(start, my_dict, course_state):
        course_state[start] = 1
        for pre_course in my_dict[start]:
            if course_state[pre_course] == 1:
                return True
            if course_state[pre_course] == 0:
                if DFS(pre_course, my_dict, course_state):
                    return True
        course_state[start] = 2
        return False
    
    if not num_courses or not prerequisites:
        # Assume no course to take returns True
        return True
    
    my_dict = defaultdict(list)
    for p in prerequisites:
        my_dict[p[0]].append(p[1])

    # Init states for all courses
    course_state = [0] * num_courses

    for n in range(num_courses):
        if course_state[n] == 0: # Call DFS from this node and look for a loop
            loop = DFS(n, my_dict, course_state)
            if loop:
                return False
    return True  


class TestCourseSchedule(unittest.TestCase):
    """Unit test for can_finish for course schedule."""

    def test_1(self):
        self.assertEqual(can_finish(2, [[1, 0]]), True)
        print("Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.")

    def test_2(self):
        self.assertEqual(can_finish(2, [[1,0],[0,1]]), False)
        print("Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.")


if __name__ == '__main__':
    unittest.main()
