# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 ==None:
            return list2
        
        if list2 ==None:
            return list1

        new_list=None
        if list1.val<=list2.val:
            new_head = list1
            list1=list1.next
        else:
            new_head = list2
            list2=list2.next

        new_list = new_head

        while list1 or list2:
            if list1 ==None:
                new_list.next = list2
                list2 = list2.next
            elif list2 ==None:
                new_list.next = list1
                list1 = list1.next
            elif list1.val<=list2.val:
                new_list.next = list1
                list1 = list1.next
            else:
                new_list.next = list2
                list2 = list2.next
            new_list = new_list.next
        return new_head