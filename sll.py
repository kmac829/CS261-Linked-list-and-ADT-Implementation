# Name: Katie Schaumleffle
# OSU Email:schaumlk@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 10/25/2021
# Description: This file is used to implement the methods of the Deque and
#               Bag ADT interfaces with a Singly Linked List.



class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self._next = None
        self._value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)
        self._tail = SLNode(None)
        self._head._next = self._tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self._head._next != self._tail:
            cur = self._head._next._next
            out = out + str(self._head._next._value)
            while cur != self._tail:
                out = out + ' -> ' + str(cur._value)
                cur = cur._next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self._head
        while cur._next != self._tail:
            cur = cur._next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head._next == self._tail

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        This method adds a new node at the beginning of the list, after the front
        sentinel
        """
        #if list is empty, add node to list and move tail to the end
        if self.is_empty() == True:
            self._head._next = SLNode(value)
            self._head._next._next = self._tail 
            return
        #initialize current head of list, add in the node, and move current head over one
        else:
            temp = self._head._next 
            self._head._next = SLNode(value)
            self._head._next._next = temp
            return

        
    def add_back(self, value: object) -> None:
        """
        This method adds a new node at the end of the list, before the back sentinel
        """
        current = self._head
        temp_node = SLNode(value)
        temp_node._next = self._tail
        #traverse to the end of the list
        while current._next != self._tail:
            current = current._next
        #update nodes value
        current._next = temp_node
        return


    def insert_at_index(self, index: int, value: object) -> None:
        """
        This methods adds a new value at the specified index in the LL.
        """
        temp_node = self._head  #create a temp so we can iterate without losing data
        #If the index isn't valid, raise exception
        if index > self.length() or index < 0:
            raise SLLException

        #If list is empty, add value
        elif self.is_empty() == True:
            self._head._next = SLNode(value)
            self._head._next._next = self._tail 
            return
        #Traverse the list 
        while index > 0:
            temp_node = temp_node._next
            index -= 1
        #update value of nodes
        replacement = SLNode(value)
        replacement._next = temp_node._next
        temp_node._next = replacement

    def remove_front(self) -> None:
        """
        This method removes the first node from the list.
        """
        #If list is exmpty, raise exception
        if self.is_empty() == True:
            raise SLLException
        #Remove the first node
        else:
            self._head._next = self._head._next._next


    def remove_back(self) -> None:
        """
        This method removes the last node from the list.
        """
        current = self._head
        prev = None
        #raise exception if list is empty
        if self.is_empty() == True:
            raise SLLException
        #traverse until we get to the last node
        while current._next != self._tail:
            prev = current
            current = current._next
        #remove last node by pointing previous node to back sentinel
        prev._next = self._tail
        return
        

    def remove_at_index(self, index: int) -> None:
        """
        This method removes a node form the list at a specific index.
        """
        prev = self._head
        current = self._head._next
        #Raise exception if list is empty or index is not valid
        if self.is_empty() or index < 0:
            raise SLLException

        #iterate through the list to find given index
        for i in range(index):
            if current._next == self._tail:
                raise SLLException

            #update pointers
            prev = current
            current = current._next
        #remove node
        prev._next = current._next  
        return

    def get_front(self) -> object:
        """
        This method returns the value from the first node without removing it.
        """
        #Raise exception if list is empty
        if self.is_empty() == True:
            raise SLLException
        return self._head._next._value

    def get_back(self) -> object:
        """
        This method returns the value from the last node in the list without removing it.
        """
        #raise exception if list is empty
        if self.is_empty() == True:
            raise SLLException
        
        current = self._head._next
        #iterate through the list to find the value
        while current._next != self._tail:
            current = current._next

        return current._value

    def remove(self, value: object) -> bool:
        """
        This method traverses the list from the beginning to the end and removes the 
        first node in the list that matches the "value" object. Returns True if a node
        was removed, otherwise returns false.
        """
        current = self._head
        #iterate through the list to find matching values
        while current != self._tail:
            #If values match, remove that node by adjusting pointers
            if current._next._value == value:
                current._next = current._next._next     
                return True
            #Traverse through list 
            else:
                current = current._next
            
        return False

    def count(self, value: object) -> int:
        """
        This method counts the number of elements in the list that matches the "value"
        """
        num = 0
        current = self._head
        #return 0 if list is empty
        if self.is_empty() == True:
            return 0
        #iterate through list adding 1 each time value is found
        while current != self._tail:
            if current._value == value:
                num += 1
            current = current._next

        return num

    def slice(self, start_index: int, size: int) -> object:
        """
        This method returns a new Linked List object that contains the requested
        number of nodes from the original list starting with the node located at 
        the requested start index. Implemented in O(n) runtime complexity.
        """
        length = self.length()
        new_list = LinkedList()     #initialize new list
        node = self._head
        #Raise exception if start index, size, start index or start index + size are not valid
        if start_index < 0 or start_index >= length or size < 0 or start_index + size > length:
            raise SLLException

        #Find the correct starting location
        for i in range(start_index + 1):
            node = node._next
        #iterate through list, adding value to the back of the list to the new list
        for i in range(size):
            new_list.add_back(node._value)
            node = node._next

        return new_list





if __name__ == '__main__':
    pass

    print('\n# add_front example 1')
    list = LinkedList()
    print(list)
    list.add_front('A')
    list.add_front('B')
    list.add_front('C')
    print(list)
    
    
    print('\n# add_back example 1')
    list = LinkedList()
    print(list)
    list.add_back('C')
    list.add_back('B')
    list.add_back('A')
    print(list)
    
    
    print('\n# insert_at_index example 1')
    list = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            list.insert_at_index(index, value)
            print(list)
        except Exception as e:
            print(type(e))
    
    
    print('\n# remove_front example 1')
    list = LinkedList([1, 2])
    print(list)
    for i in range(3):
        try:
            list.remove_front()
            print('Successful removal', list)
        except Exception as e:
            print(type(e))
    
    
    print('\n# remove_back example 1')
    list = LinkedList()
    try:
        list.remove_back()
    except Exception as e:
        print(type(e))
    list.add_front('Z')
    list.remove_back()
    print(list)
    list.add_front('Y')
    list.add_back('Z')
    list.add_front('X')
    print(list)
    list.remove_back()
    print(list)
    
    
    print('\n# remove_at_index example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6])
    print(list)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            list.remove_at_index(index)
            print(list)
        except Exception as e:
            print(type(e))
    print(list)
    
    
    print('\n# get_front example 1')
    list = LinkedList(['A', 'B'])
    print(list.get_front())
    print(list.get_front())
    list.remove_front()
    print(list.get_front())
    list.remove_back()
    try:
        print(list.get_front())
    except Exception as e:
        print(type(e))
    
    
    print('\n# get_back example 1')
    list = LinkedList([1, 2, 3])
    list.add_back(4)
    print(list.get_back())
    list.remove_back()
    print(list)
    print(list.get_back())
    
    
    print('\n# remove example 1')
    list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(list)
    for value in [7, 3, 3, 3, 3]:
        print(list.remove(value), list.length(), list)
    
    
    print('\n# count example 1')
    list = LinkedList([1, 2, 3, 1, 2, 2])
    print(list, list.count(1), list.count(2), list.count(3), list.count(4))
    
    
    print('\n# slice example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = list.slice(1, 3)
    print(list, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(list, ll_slice, sep="\n")
    
    
    print('\n# slice example 2')
    list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", list)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", list.slice(index, size))
        except:
            print(" --- exception occurred.")

