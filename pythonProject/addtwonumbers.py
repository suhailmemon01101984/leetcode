#https://leetcode.com/problems/add-two-numbers/description/
class ListNode:
    def __init__(self,value=0):
        self.val=value
        self.next=None

class Solution:
    def addTwoNumbers(self,l1:ListNode,l2:ListNode)->ListNode:
        head=ListNode()
        current=head
        carry=0

        while(l1!=None or l2!=None or carry!=0):

            total=0
            value1=0
            value2=0

            if l1!=None:
                value1=l1.val
            else:
                value1=0

            if l2!=None:
                value2=l2.val
            else:
                value2=0

            total=value1 + value2 + carry
            current.next=ListNode(total%10)
            carry=total//10

            if l1:
                l1=l1.next

            if l2:
                l2=l2.next

            current=current.next
        return head.next


n11=ListNode(9)
n12=ListNode(9)
n13=ListNode(9)
n14=ListNode(9)
n15=ListNode(9)
n16=ListNode(9)
n17=ListNode(9)

n11.next=n12
n12.next=n13
n13.next=n14
n14.next=n15
n15.next=n16
n16.next=n17

n21=ListNode(9)
n22=ListNode(9)
n23=ListNode(9)
n24=ListNode(9)

n21.next=n22
n22.next=n23
n23.next=n24

# print(n11.val)
# print(n11.next.val)
#
#
# print(n21.val)
# print(n21.next.val)
# print(n21.next.next.val)

#l=ListNode()
#print(l.val)
#print(l.next)

#print(n11)
#print(n21)

s=Solution()
r=s.addTwoNumbers(n11,n21)
print(r)
print(r.val)
print(r.next.val)
print(r.next.next.val)
print(r.next.next.next.val)
print(r.next.next.next.next.val)
print(r.next.next.next.next.next.val)
print(r.next.next.next.next.next.next.val)
print(r.next.next.next.next.next.next.next.val)
#print(r.next.next.next.next.next.next.next.next.val)

