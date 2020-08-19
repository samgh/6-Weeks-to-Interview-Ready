"""
Title: Network delay time

Problem:
    There are N network nodes, labelled 1 to N.

    Given times, a list of travel times as directed edges times[i] = (u, v, w),
    where u is the source node, v is the target node, and w is the time it takes
    for a signal to travel from source to target.

    Now, we send a signal from a certain node K. How long will it take for all
    nodes to receive the signal? If it is impossible, return -1.

Execution: python network_delay.py
"""
from typing import List, Optional
import unittest
from collections import defaultdict


def network_delay(times: List[List[int]], n_val: int, k_val: int) -> float:
    """Calculate the network delay."""
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((w, v))

    dist = {node: float("inf") for node in range(1, n_val + 1)}

    def dfs(node: int, elapsed: int) -> Optional[float]:
        if elapsed >= dist[node]:
            return
        dist[node] = elapsed
        for time, nei in sorted(graph[node]):
            dfs(nei, elapsed + time)

    dfs(k_val, 0)
    ans = max(dist.values())
    return ans if ans < float("inf") else -1


class TestNetworkDelay(unittest.TestCase):
    """Unit tests for network_delay."""

    def test_1(self):
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        n_val = 4
        k_val = 2
        self.assertEqual(network_delay(times, n_val, k_val), 2)


if __name__ == "__main__":
    unittest.main()
