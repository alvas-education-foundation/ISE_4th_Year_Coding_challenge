# program to remove duplicate elements from a Circular Linked List
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
      
  def add(self,data):    
    newNode = Node(data);    
     
    if self.head.data is None:        
      self.head = newNode;    
      self.tail = newNode;    
      newNode.next = self.head;    
    else:    
      
      self.tail.next = newNode;    
      
      self.tail = newNode;    
          
      self.tail.next = self.head;    
       
  def removeDuplicate(self):        
    current = self.head;    
    if(self.head == None):    
      print("List is empty");    
    else:    
      while(True):    
        temp = current;    
        
        index = current.next;    
        while(index != self.head):    
            
          if(current.data == index.data):      
            temp.next = index.next;    
          else:    
             
            temp = index;    
          index= index.next;    
        current =current.next;    
        if(current.next == self.head):    
          break;    
                  
  def display(self):    
    current = self.head;    
    if self.head is None:    
      print("List is empty");    
      return;    
    else:    
        
      print(current.data);    
      while(current.next != self.head):    
        current = current.next;    
        print(current.data);    
    print("\n");    
          
class CircularLinkedList:    
  cl = CreateList();    
  cl.add(1);    
  cl.add(2);    
  cl.add(3);    
  cl.add(2);    
  cl.add(2);    
  cl.add(4);    
      
  print("Originals list: ");    
  cl.display();    
  cl.removeDuplicate();    
  print("List after removing duplicates: ");    
  cl.display();    