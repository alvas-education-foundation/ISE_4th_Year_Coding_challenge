#To create a Circular Linked List of N nodes and count the number of nodes
class Node:    
    def __init__(self,data):    
        self.data = data;    
        self.next = None;    
     
class CreateList:    
    
    def __init__(self):    
        self.count = 0;    
        self.head = Node(None);    
        self.tail = Node(None);    
        self.head.next = self.tail;    
        self.tail.next = self.head;    
        
     
    def add(self,data):    
        newNode = Node(data);    
           
        if self.head.data is None:    
                
            self.head = newNode;    
            self.tail = newNode;    
            newNode.next = self.head;    
        else:    
               
            self.tail.next = newNode;    
           .    
            self.tail = newNode;    
         
            self.tail.next = self.head;    
                
     
    def countNodes(self):    
        current = self.head;    
        self.count=self.count+1;    
        while(current.next != self.head):    
            self.count=self.count+1;    
            current = current.next;    
        print("Count of nodes present in circular linked list: "),    
        print(self.count);    
        
     
class CircularLinkedList:    
    cl = CreateList();    
     
    cl.add(1);    
    cl.add(2);    
    cl.add(4);    
    cl.add(1);    
    cl.add(2);    
    cl.add(3);    
    
    cl.countNodes();    