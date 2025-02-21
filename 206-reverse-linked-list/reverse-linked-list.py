# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp1 = head
        while temp1:
            arr.append(temp1.val)
            temp1 = temp1.next
        

        j = len(arr) - 1
        
        temp2 = head

        while j >= 0:
            temp2.val = arr[j]
            temp2 = temp2.next
            j -= 1
        return head            