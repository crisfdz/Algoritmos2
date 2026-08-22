class LinkedList:
    head = None

class Node:
    value = None
    nextNode = None

def ContieneSuma(L: LinkedList, n: int) -> bool:
    if L.head is None or L.head.nextNode is None:
        return False
    
    current = L.head
    while current:
        target = n - current.value
        p = current.nextNode
        while p:
            if p.value == target:
                return True
            p = p.nextNode
        current = current.nextNode
    return False