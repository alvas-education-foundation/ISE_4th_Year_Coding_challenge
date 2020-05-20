# program to insert a new node at the end of the Circular Linked List

class Node:    
  def __init__(self,data):    
    self.data = data;    
    self.next = None;    
     
class CreateList:    
   
  def __init__(self):    
    self.head = Node(None);    
    self.tail = Node(None);    
    self.head.next = self.tail;    
    self.tail.next = self.head;    
        
      
  def addAtEnd(self,data):    
    newNode = Node(data);    
        
    if self.head.data is None:    
      #If list is empty, both head and tail would point to new node.    
      self.head = newNode;    
      self.tail = newNode;    
      newNode.next = self.head;    
    else:    
     
      self.tail.next = newNode;    
         
      self.tail = newNode;    
      
      self.tail.next = self.head;    
     
     
  def display(self):    
    current = self.head;    
    if self.head is None:    
      print("List is empty");    
      return;    
    else:    
        print("Adding nodes to the end of the list: ");    
        
        print(current.data),    
        while(current.next != self.head):    
            current = current.next;    
            print(current.data),    
        print("\n");    
     
class CircularLinkedList:    
    cl = CreateList();    
       
    cl.addAtEnd(1);    
    cl.display();    
     
    cl.addAtEnd(2);    
    cl.display();    
      
    cl.addAtEnd(3);    
    cl.display();    
       
    cl.addAtEnd(4);    
    cl.display();    