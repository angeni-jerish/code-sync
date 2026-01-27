# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        next_node = head.next
        cnt=1
        cur=head
        while(next_node):
            cnt+=1
            next_node = next_node.next
        
        move=cnt-n-1

        if(cnt ==n):
            head = head.next
        else:
            for i in range(move):
                cur = cur.next
            
            connection = cur.next.next
            cur.next=connection

        return head