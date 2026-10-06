class AVLTree:
    root = None

class AVLNode:
    parent = None
    leftNode = None
    rightNode = None
    key = None
    value = None
    bf = None

def printTree(T: AVLTree):
    if T.root:
        printNode(T.root, 0)

def printNode(node: AVLNode, level: int):
    if node:
        printNode(node.rightNode, level + 1)
        print(' ' * 4 * level + '->', node.key)
        printNode(node.leftNode, level + 1)

def searchByValue(node: AVLNode, value) -> int:
    if node is None:
        return None
    if node.value == value:
        return node.key
    leftSearch = searchByValue(node.leftNode, value)
    if leftSearch is not None:
        return leftSearch
    rightSearch = searchByValue(node.rightNode, value)
    return rightSearch

#Ejercicio 1
def rotateLeft(T: AVLTree, node: AVLNode) -> AVLNode:
    newRoot = node.rightNode
    node.rightNode = newRoot.leftNode
    if newRoot.leftNode:
        newRoot.leftNode.parent = node
    newRoot.parent = node.parent
    if node.parent == None:
        T.root = newRoot
    elif node == node.parent.leftNode:
        node.parent.leftNode = newRoot
    else:
        node.parent.rightNode = newRoot

    newRoot.leftNode = node
    node.parent = newRoot
    return newRoot

def rotateRight(T: AVLTree, node: AVLNode) -> AVLNode:
    newRoot = node.leftNode
    node.leftNode = newRoot.rightNode
    if newRoot.rightNode:
        newRoot.rightNode.parent = node
    newRoot.parent = node.parent
    if node.parent == None:
        T.root = newRoot
    elif node == node.parent.leftNode:
        node.parent.leftNode = newRoot
    else:
        node.parent.rightNode = newRoot        

    newRoot.rightNode = node
    node.parent = newRoot
    return newRoot

#Ejercicio 2
def calculateBalance(T: AVLTree, node: AVLNode):
    if node is None:
        return 0
    leftHeight = calculateBalance(T, node.leftNode)
    rightHeight = calculateBalance(T, node.rightNode)
    node.bf = leftHeight - rightHeight
    print(f"Node: {node.key}, Balance Factor: {node.bf}")
    return max(leftHeight, rightHeight) + 1


def updateBalanceFactors(T: AVLTree):
    calculateBalance(T, T.root)

#Ejercicio 3
def rebalance(T: AVLTree) -> AVLTree:
    T.root = rebalanceNode(T, T.root)
    return T

def rebalanceNode(T: AVLTree, node: AVLNode) -> AVLNode:
    if node is None:
        return None

    node.leftNode = rebalanceNode(T, node.leftNode)
    node.rightNode = rebalanceNode(T, node.rightNode)
    updateBalanceFactors(T)

    if node.bf < -1:
        if node.rightNode and node.rightNode.bf > 0:
            node.rightNode = rotateRight(T, node.rightNode)
        return rotateLeft(T, node)
    elif node.bf > 1:
        if node.leftNode and node.leftNode.bf < 0:
            node.leftNode = rotateLeft(T, node.leftNode)
        return rotateRight(T, node)

    return node

#Ejercicio 4
def insert(T: AVLTree, key, value):
    newNode = AVLNode()
    newNode.key = key
    newNode.value = value
    newNode.bf = 0
    if T.root == None:
        T.root = newNode
        return

    currentNode = T.root
    parent = None
    while currentNode:
        parent = currentNode
        if key < currentNode.key:
            currentNode = currentNode.leftNode
        elif key > currentNode.key:
            currentNode = currentNode.rightNode
        else:
            print("La clave ya existe")
            return
        
    newNode.parent = parent
    if key < parent.key:
        parent.leftNode = newNode
    else:
        parent.rightNode = newNode

    currentNode = newNode
    while currentNode.parent:
        p = currentNode.parent
        if currentNode == p.leftNode:
            p.bf += 1
        else:
            p.bf -= 1

        if p.bf == 0:
            break

        if p.bf == 2:
            if currentNode.bf < 0:
                child = currentNode.rightNode
                rotateLeft(T, currentNode)
                rotateRight(T, p)
                if child.bf == 1:
                    p.bf = -1
                    currentNode.bf = 0
                elif child.bf == -1:
                    p.bf = 0
                    currentNode.bf = 1
                else:
                    p.bf = 0
                    currentNode.bf = 0
                child.bf = 0 
            else:
                rotateRight(T,p)
                p.bf = 0
                currentNode.bf = 0
            break
        elif p.bf == -2:
            if currentNode.bf > 0:
                child = currentNode.leftNode
                rotateRight(T, currentNode)
                rotateLeft(T, p)
                if child.bf == -1:
                    p.bf = 1
                    currentNode.bf = 0
                elif child.bf == 1:
                    p.bf = 0
                    currentNode.bf = -1
                else:
                    p.bf = 0
                    currentNode.bf = 0
                child.bf = 0 
            else:
                rotateLeft(T,p)
                p.bf = 0
                currentNode.bf = 0
            break
        currentNode = p

#Ejercicio 5
def delete(T: AVLTree, key):
    if T.root == None:
        return
    currentNode = T.root
    while currentNode and currentNode.key != key:
        if key < currentNode.key:
            currentNode = currentNode.leftNode
        else:
            currentNode = currentNode.rightNode

    if currentNode == None:
        print("No se encontró el elemento a eliminar")
        return None
    if currentNode.leftNode and currentNode.rightNode:
        pass



if __name__ == "__main__":
    T = AVLTree()
    T.root = AVLNode()
    T.root.key = 10
    T.root.value = "A"
    T.root.bf = 0

    node2 = AVLNode()
    node2.key = 5
    node2.value = "B"
    node2.bf = 0
    node2.parent = T.root
    T.root.leftNode = node2

    node3 = AVLNode()
    node3.key = 15
    node3.value = "C"
    node3.bf = 0
    node3.parent = T.root
    T.root.rightNode = node3

    # Adding more nodes to create imbalance
    node4 = AVLNode()
    node4.key = 3
    node4.value = "D"
    node4.bf = 0
    node4.parent = node2
    node2.leftNode = node4

    node5 = AVLNode()
    node5.key = 7
    node5.value = "E"
    node5.bf = 0
    node5.parent = node4
    node4.leftNode = node5

    printTree(T)

    calculateBalance(T, T.root)

    T = rebalance(T)
    print("\nAfter rebalancing:")
    printTree(T)

    insert(T, 20, "F")
    insert(T, 25, "G")
    print("\nAfter inserting 20, 25:")
    printTree(T)