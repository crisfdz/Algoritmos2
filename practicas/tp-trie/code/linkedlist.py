class LinkedList:
    head = None

class Node:
    value = None
    nextNode = None


def add(L: LinkedList, element):
    currentNode = Node()
    currentNode.value = element
    currentNode.nextNode = L.head
    L.head = currentNode
    return


def search(L: LinkedList, element) -> int | None:
    currentNode = L.head
    i = 0
    while currentNode:
        if currentNode.value == element:
            return i
        
        currentNode = currentNode.nextNode
        i += 1
    
    return None


def getNodeValue(L: LinkedList, element) -> Node | None:
    currentNode = L.head

    while currentNode:
        if currentNode.value.key == element:
            return currentNode.value

        currentNode = currentNode.nextNode

    return None


def insert(L: LinkedList, element, position: int) -> int | None:
    if position <= length(L) and position > 0:
        currentNode = L.head
        i = 0
        while currentNode:
            if position-1 == i:
                newNode = Node()
                newNode.value = element
                siguiente = currentNode.nextNode
                currentNode.nextNode = newNode
                newNode.nextNode = siguiente

                return position-1

            currentNode = currentNode.nextNode
            i += 1

    elif position == 0:
        add(L, element)
    else:
        return None
    

def delete(L: LinkedList, element) -> int | None:
    currentNode = L.head
    i = 0

    if length(L) == 1:
        L.head = None

    while currentNode.nextNode is not None:
        if currentNode.value == element:
            L.head = currentNode.nextNode
            return i
        
        if currentNode.nextNode.value == element:
            currentNode.nextNode = currentNode.nextNode.nextNode
            return i+1
        
        currentNode = currentNode.nextNode
        i += 1

    return None

def length(L: LinkedList) -> int:
    currentNode = L.head
    i = 0
    while currentNode:
        currentNode = currentNode.nextNode
        i += 1

    return i


def access(L: LinkedList, position: int):
    currentNode = L.head

    if position > length(L)-1:
        return None
    
    for i in range(position):
        currentNode = currentNode.nextNode
    
    return currentNode.value
    

def update(L: LinkedList, element, position: int) -> int | None:
    currentNode = L.head
    i = 0

    if position > length(L)-1:
        return None
    
    while i < position:
        currentNode = currentNode.nextNode
        i += 1

    currentNode.value = element
    return i