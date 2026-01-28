# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if(head==None):
            return None
        
        cur_node=head  
        old_list=None
        
        while(cur_node !=None and cur_node.next!=None):
            
            next_node=cur_node.next
            next_next_nodes=cur_node.next.next   
                
                
            next_node.next= cur_node
            cur_node.next=old_list
            old_list=next_node
            
            cur_node = next_next_nodes
            
        if(cur_node!=None):
            cur_node.next = old_list
        else:
            cur_node=old_list
        
        return cur_node