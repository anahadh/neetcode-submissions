# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        track_1, track_2 = list1, list2
        prev = None

        while (track_1 != None or track_2 != None):
            node = ListNode()

            if (track_2 == None or (track_1 and track_1.val < track_2.val)):
                node.val = track_1.val
                track_1 = track_1.next
            else:
                node.val = track_2.val
                track_2 = track_2.next
            
            if (prev == None):
                head = node
                prev = head
            else:
                prev.next = node
                prev = node
        
        return head
