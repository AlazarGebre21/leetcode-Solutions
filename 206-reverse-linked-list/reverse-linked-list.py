# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None

        def display(head2):
            temp = head2
            while temp:
                print(temp.val, end='->')
                temp = temp.next

        while temp:
            storedir = temp.next
            temp.next = prev
            prev = temp
            temp = storedir
        display(prev)
        display(head)
        return prev
            
        
        # arr = []
        # temp1 = head
        # while temp1:
        #     arr.append(temp1.val)
        #     temp1 = temp1.next
        

        # j = len(arr) - 1
        
        # temp2 = head

        # while j >= 0:
        #     temp2.val = arr[j]
        #     temp2 = temp2.next
        #     j -= 1
        # return head            