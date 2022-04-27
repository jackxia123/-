class Node(object):
    def __init__(self, data, nxt = None):
        self.data = data
        self.next = nxt
        
def solution(head):
  dummy = head
  while head:
    while head.next and head.data ==head.next.data:
      head.next=head.next.next
    head= head.next
  return dummy
 
node1 =Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(3)
node5 =Node(None)
node1.next =node2
node2.next = node3
node3.next = node4
node4.next = node5
head = node1
def display_linklist(node):
  while((node!= None)):
    print(node.data,end=' ')
    node = node.next
  print("")
display_linklist(solution(head))
