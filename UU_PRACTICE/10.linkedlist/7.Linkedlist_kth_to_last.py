from algorithms.linkedlist.kth_to_last import Node,print_linked_list

a1 = Node("A")
a2 = Node("A")
b = Node("B")
c1 = Node("C")
d = Node("D")
c2 = Node("C")
f = Node("F")
g = Node("G")
a1.next = a2
a2.next = b
b.next = c1
c1.next = d
d.next = c2
c2.next = f
f.next = g
print_linked_list(a1)