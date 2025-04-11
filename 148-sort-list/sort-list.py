# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge(left_side, right_side):

            dummy_node = ListNode()
            curr = dummy_node
            l = left_side
            r = right_side

            while l and r:
                if l.val <= r.val:
                    curr.next = l
                    l = l.next
                else:
                    curr.next = r
                    r = r.next
                curr = curr.next

            curr.next = l if l else r
            
            return dummy_node.next
            



        def mid_finder(temp):
            
            slow = temp
            fast = temp.next

            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            

            
            return slow

        def merge_sort(temp):
            
            if not temp or not temp.next:
                return temp

            mid = mid_finder(temp)

            right = mid.next
            mid.next = None

            left_side = merge_sort(temp)
            right_side = merge_sort(right)
            
            return merge(left_side, right_side)
        
        return merge_sort(head)
