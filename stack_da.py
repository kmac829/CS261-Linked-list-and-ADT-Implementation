# Name: Katie Schaumleffle
# OSU Email: schaumlk@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 10/25/2021
# Description: This assignment implements a Stack ADT class. This assignment
#               uses the Dynamic Array data structure that was implemented from
#               the previous assignment.

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da_val = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self._da_val.length()) + " elements. ["
        out += ', '.join([str(self._da_val[i]) for i in range(self._da_val.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da_val.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da_val.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        This method adds a new element to the top of the stack implemented with
        O(1) amortized runtime complexity
        """
        self._da_val.append(value)
        
    def pop(self) -> object:
        """
        This method removes the top element from the stack and returns its value
        using O(1) amortized runtime complexity.
        """
        #raise exception if stack is empty
        if self.size() <= 0:
            raise StackException
        
        value = self._da_val.get_at_index(self.size() - 1)
        #remove last element
        self._da_val.remove_at_index(self.size() - 1)
        #return value
        return value

    def top(self) -> object:
        """
        This method returns the value of the top element without removing it. Implemented
        with O(1) runtime complexity.
        """
        #If list is empty, raise exception
        if self.size() <= 0:
            raise StackException

        #value of the last element
        value = self._da_val.get_at_index(self.size() - 1)
        #return value of the last element
        return value

    


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)


    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))


    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
