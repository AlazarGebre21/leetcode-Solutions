# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if head == None:
            return head

        temp = head 

        while temp.next:
            
            if temp.next.val == val:
                delete_node = temp.next
                temp.next = delete_node.next
                delete_node.next = None
            else:
                temp = temp.next
        
        if head != None and head.val == val:
            head = head.next
        
        return head
            

