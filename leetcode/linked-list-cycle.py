# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        #Floyd's Cycle Detection Algorithm -initial try
        '''
        s=head
        if s==None:
                return False
        f=head.next
        if f==None:
            return False
        while s!=f:
            if f==None or f.next==None:
                return False
            else:
                f = f.next.next
                s= s.next
        return True
        '''

        #FCDA - second try
        s=head
        f=head

        while f and f.next:
            f=f.next.next
            s=s.next
            if s==f:
                return True
        return False