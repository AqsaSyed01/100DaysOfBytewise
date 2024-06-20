class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head =None
    
    #insert node in LL
    def insert(self, val):
        newnode = Node(val)
        
        if self.head is None:
            self.head = newnode
        else:
            ptr =self.head
            while ptr.next!=None:
                ptr=ptr.next
            ptr.next = newnode
    
    #display LL
    def display(self):
        ptr = self.head
        while ptr!=None:
            print(ptr.data, end="->")
            ptr = ptr.next
        print()
    
    def checkPalindrome(self):
        slow =self.head
        fast = self.head
        
        if self.head.next is None:
            return True
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        
        curr=slow
        nxt=None
        pre=None
        
        while curr!=None:
            nxt=curr.next
            curr.next=pre
            pre=curr
            curr=nxt
        
        slow=pre
        fast=self.head
        
        while slow!=None:
            if slow.data!=fast.data:
                return False
            slow=slow.next
            fast=fast.next
        
        return True
        
        
        
        
        
ll = Linkedlist()
print("Enter no. of nodes in linked list")
n = int(input())
lst=[]
print("Enter value of each node")

lst = list(map(int, input().split()))

for i in range(n):
    ll.insert(lst[i])
        
ll.display()

if ll.checkPalindrome():
    print("List is Palindrome")
else:
    print("List is not Palindrome")