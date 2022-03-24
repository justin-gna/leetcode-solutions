# LeetCode Problem 2. Add Two Numbers (https://leetcode.com/problems/add-two-numbers/)
# approach explanation:
# uses the helper function linked_list_to_num() to turn a reverse order number stored in a linked list into an normal number.
# this is done by traversing through the linked list and adding each digit to a string and finally reversing that string and returning it as an integer.
# the solution function takes in the two lists and turns them into numbers and adds them together.
# the number is then converted into a string and reversed and turned into a linked list and finally returned.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def linked_list_to_num(lst: ListNode) -> int:
    number = ''
    curr = lst
    while curr is not None:
        number += str(curr.val)
        curr = curr.next
        
    return int(number[::-1])

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = linked_list_to_num(l1)
        num2 = linked_list_to_num(l2)
        summed_nums = str(num1 + num2)[::-1]
        return_lst = ListNode(int(summed_nums[0]))
        curr = return_lst
        for i in range(1, len(summed_nums)):
            curr.next = ListNode(int(summed_nums[i]))
            curr = curr.next
            
        return return_lst
