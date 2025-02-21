# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def length():
            temp = head
            count = 0
            while temp:
                temp = temp.next
                count += 1
            return count
        
        
        
        hold = length()//2
        temp = head
       
            
        while hold:
            temp = temp.next
            hold -= 1
            
        return temp


        
