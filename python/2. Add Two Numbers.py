# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 1. straight forward
        # l3 = ListNode((l1.val + l2.val) % 10)
        # cur = l3
        # carry = 1 if l1.val + l2.val >= 10 else 0
        # while l1.next != None or l2.next !=None:
        #     if l1.next == None:
        #         l2 = l2.next
        #         nextNode = ListNode((l2.val + carry) % 10) 
        #         carry = 1 if l2.val + carry >= 10 else 0
        #     elif l2.next ==None:
        #         l1 = l1.next
        #         nextNode = ListNode((l1.val + carry) % 10)    
        #         carry = 1 if l1.val + carry >= 10 else 0
        #     else:
        #         l1 = l1.next
        #         l2 = l2.next
        #         nextNode = ListNode((l1.val + l2.val + carry) % 10)
        #         carry = 1 if l1.val + l2.val + carry >= 10 else 0
        #     cur.next = nextNode
        #     cur = nextNode
        # if carry == 1:
        #     nextNode = ListNode(1)
        #     cur.next = nextNode
        # return l3
        
        # 2. another version of 1
        start = ListNode(0)
        cur = start
        carry = 0
        while l1 != None or l2 !=None:
            x = l1.val if l1  else 0
            y = l2.val if l2  else 0
            nextNode = ListNode((x+y+carry) % 10)
            cur.next = nextNode
            cur = nextNode
            carry = (x+y+carry) //10
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry:
            cur.next = ListNode(1)
        return start.next
