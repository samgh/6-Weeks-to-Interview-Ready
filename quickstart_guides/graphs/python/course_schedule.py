"""
Title: Course schedule

Problem:
    There are a total of numCourses courses you have to take, labeled from 0 to
    numCourses-1.

    Some courses may have prerequisites, for example to take course 0 you have
    to first take course 1, which is expressed as a pair: [0,1]

    Given the total number of courses and a list of prerequisite pairs, is it
    possible for you to finish all courses?

Execution: python course_schedule.py
"""
from typing import List
import unittest


def course_schedule(num_courses: int, pre_reqs: List[List[int]]) -> bool:
    """Determines if course schedule is feasible."""
    if len(pre_reqs) == 0:
        return True
    visited = [0 for _ in range(num_courses)]
    adj_list = make_graph(pre_reqs)
    for i in range(num_courses):
        if not visited[i]:
            if not has_cycle(adj_list, visited, i):
                return False
    return True


def has_cycle(adj_list: dict, visited: List[int], current_node: int = 0) -> bool:
    """Check if graph contains cycle."""
    if visited[current_node] == -1:
        return False
    if visited[current_node] == 1:
        return True
    visited[current_node] = -1
    if current_node in adj_list:
        for i in adj_list[current_node]:
            if not has_cycle(adj_list, visited, i):
                return False
    visited[current_node] = 1
    return True


def make_graph(array):
    """Construct adjacency list for graph."""
    adj_list = {}
    for i in array:
        if i[1] in adj_list:
            adj_list[i[1]].append(i[0])
        else:
            adj_list[i[1]] = [i[0]]
    return adj_list


class TestCourseSchedule(unittest.TestCase):
    """Unit tests for course_schedule."""

    def test_1(self):
        self.assertEqual(course_schedule(2, [[1, 0]]), True)


if __name__ == "__main__":
    unittest.main()
