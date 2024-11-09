#Define the Node Class:
#Each node stores data and a next pointer.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Define the LinkedList Class:
#Manages the nodes and provides methods for common operations (insert, delete, traverse, etc.).

class LinkedList:
    def __init__(self):
        self.head = None

    # Method to insert a node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Method to traverse and print the list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


#COMMON OPERATİONS
#Insert at the Beginning:
        #Add a new node as the head of the list.
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

#Insert After a Specific Node:

    #Find a target node and insert a new node after it.

    def insert_after(self, prev_node_data, data):
        current = self.head
        while current and current.data != prev_node_data:
            current = current.next
        if current is None:
          print("Node not found")
          return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
#Delete a Node:

    #Remove a node with a specific value.
    def delete_node(self, key):
        current = self.head
        if current and current.data == key:  # Node to be deleted is the head
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            print("Node not found")
            return
        prev.next = current.next
        current = None

#Searching for a Node:

    #Traverse the list to see if a node with specific data exists.
    def search(self, key):
       current = self.head
       while current:
           if current.data == key:
               return True
           current = current.next
       return False



#testting the li,nked list

# Creating an empty linked list
ll = LinkedList()

# Adding elements to the linked list
ll.append(10)
ll.append(20)
ll.append(30)

ll.prepend(47)

ll.delete_node(20)

ll.insert_after(10,33)


#for serachıng 
i=int(input("What do you wnnna search")) 
a=ll.search(i)
if a:
    print("element found")
else:
    print("Not FOUND :/")

# Printing the linked list
ll.print_list() 
