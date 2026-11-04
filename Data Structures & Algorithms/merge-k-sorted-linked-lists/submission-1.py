# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
from typing import List, Optional

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        dummy = ListNode()
        tail = dummy

        while heap:
            val, i, node = heapq.heappop(heap)   # smallest front of all lists
            tail.next = node
            tail = tail.next

            # That list's next node is its new front.
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next

        