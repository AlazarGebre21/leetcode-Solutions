# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # creating a comparison function since python does not have a built in function for comparing linkedlists
        def changeToArray(pointer):
            temp = pointer
            arr = [] 
            while temp:
                arr.append(temp.val)
                temp = temp.next
            return arr

    
        # Finding the reverse of the linked list
        prev = None
        temp = head

        arr1 = changeToArray(head)

        while temp:
            storedir = temp.next
            temp.next = prev
            prev = temp
            temp = storedir
        reverse = prev

        arr2 = changeToArray(reverse)
        
        
        # Comparing it With the original linked list

        return arr1 == arr2