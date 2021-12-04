class Node:

    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None  #if list is blank and  last of link list will point to None

    def insert_at_begining(self,data):
        node=Node(data,self.head) #at first it was blank,we added the data so we should change the (head of list= None) to
                                # the last node next attribute
        self.head=node    #since now list is not blank , head of list points to the first node

    def insert_at_end(self,data):
        if self.head is None:  #if linkedlist is empty
            self.head=Node(data,None)
            return

        itr=self.head
        while itr.next:  #iterate to next until the last since last next is None continues fails and goes outward
            itr=itr.next
        itr.next=Node(data,None)
        

    def insert_values(self,data_list):
        self.head=None

        for data in data_list:
            self.insert_at_end(data)

    def get_count(self):
        count=0
        itr=self.head
        while itr:  #dont write itr.next here, because if list is empty head will be None, so None will not have an attribute next
            count+=1
            itr=itr.next
        return str(count)

    def remove_at(self,index): #remove  element at  particular index

        if index<0 or index >=int(self.get_count()):
            raise Exception('Invalid Index')

        if index==0:
            self.head = self.head.next

        count=0
        itr=self.head 
           #['apple','iphone','cherry']  1
        while itr:
            
            if (count) == index-1:
                itr.next=itr.next.next
                
                break
                
            itr=itr.next
            print(itr.data)
            count+=1
        

    def insert_at(self,index,data):
        if index<0 or index>int(self.get_count()):
            raise Exception('Invalid Index')

        if index ==0:
            self.insert_at_begining(data)
            return

        count=0
        itr=self.head
        while itr:
            if (count+1) == index:
                node=Node(data,itr.next)
                itr.next=node
                break
            
            itr=itr.next
            count +=1


    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return 
        
        itr=self.head   #itr points to the node and next of node is node as next attribute of node stores node
        llstr=''
        while itr:
            llstr+=str(itr.data)+'-->'
            itr=itr.next

        print(llstr)



if __name__ == '__main__':
    ll=LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(89)
    ll.insert_at_end(789)
    ll.print()
    print('Length of LinkedList =>'+ll.get_count())
    
    
    linked_list_of_list=LinkedList()
    linked_list_of_list.insert_values(['apple','iphone','cherry'])
    linked_list_of_list.print()
    linked_list_of_list.remove_at(1)  #remove element of linkedlist at particular index
    linked_list_of_list.insert_at(1,'ji')  #insert at given index
    linked_list_of_list.print()

    lla=LinkedList()
    print('Length of LinkedList =>'+lla.get_count())

    
    
    