class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is Empty")
            return

        itr = self.head
        ll = ""
        while itr:
            ll = ll + str(itr.data) +"-->"
            itr = itr.next
        print(ll)

    def insert_at_start(self,data):
        node = Node(data,self.head)  
        self.head = node 

    def insert_at_end(self , data):
        if self.head is None:
            node = Node(data,None)
            self.head=node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def insert_values(self , data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def length(self):
        cnt = 0
        itr = self.head
        while itr:
            cnt+=1
            itr = itr.next
        return cnt

    def remove_at(self,index):
        if index >= self.length() or index<0:
            raise Exception("Invalid index")

        if index==0:
            self.head = self.head.next
            return
        
        itr = self.head
        cnt = 0
        while itr:
            if cnt == index-1:
                itr.next = itr.next.next
                break
            cnt+=1
            itr = itr.next

ll = LinkedList()
ll.insert_values(["banana" , "cherry" , "mango" , "apple"])
ll.remove_at(2)
ll.print()




