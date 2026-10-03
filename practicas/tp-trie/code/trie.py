from linkedlist import LinkedList, add as LLadd, getNodeValue as LLgetNode, delete as LLdelete, length

class Trie:
    root = None

class TrieNode:
    parent = None
    children = LinkedList()
    key = None
    isEndOfWord = False


#Ejercicio 1
def insert(T: Trie, element):
    currentNode = T.root

    for i in element:
        node = LLgetNode(currentNode.children, i)

        if node:
            currentNode = node
        else:
            newNode = TrieNode()
            newNode.parent = currentNode
            newNode.key = i

            LLadd(currentNode.children, newNode)

            currentNode = newNode

    currentNode.isEndOfWord = True
    return


def search(T: Trie, element) -> bool:
    currentNode = T.root

    for i in element:
        node = LLgetNode(currentNode.children, i)

        if node is None:
            return False

        currentNode = node

    return currentNode.isEndOfWord


#Ejercicio 3
def delete(T: Trie, element) -> bool:
    currentNode = T.root

    for i in element:
        node = LLgetNode(currentNode.children, i)

        if node is None:
            return False

        currentNode = node

    if not currentNode.isEndOfWord:
        return False

    currentNode.isEndOfWord = False

    if currentNode.children.head is not None: # Si el nodo tiene hijos no podemos eliminarlo.
        return True
    
    while currentNode != T.root:
        parent = currentNode.parent

        LLdelete(parent.children, currentNode)

        currentNode = parent

        # Verificamos si recorriendo hacia arriba los nodos tienen hijos o son otras palabras.
        if currentNode.children.head is not None:
            break

        if currentNode.isEndOfWord:
            break

    return True

#Ejercicio 4
def findPrefix(T: Trie, p: str, n: int):
    currentNode = T.root
    if len(p) > n:
        print("El prefijo debe ser más corto que la longitud de la palabra.")
        return False

    for i in p:
        node = LLgetNode(currentNode.children, i)

        if node is None:
            print("No existen palabras con ese prefijo.")
            return False

        currentNode = node

    _findPrefixImpl(currentNode, p, n-len(p))

#Ejercicio 5
def compareTrie(T1: Trie, T2: Trie) -> bool:
    words = []
    _compareTrieImpl(T1.root, "", words)
    
    for word in words:
        if not search(T2, word):
            return False
    
    return True

def _compareTrieImpl(node, currentWord, words):
    if node.isEndOfWord:
        words.append(currentWord)

    i = node.children.head
    while i:
        _compareTrieImpl(i.value, currentWord + i.value.key, words)
        i = i.nextNode
    

def _findPrefixImpl(currentNode: TrieNode, word: str, n: int):
    if n == 0:
        if currentNode.isEndOfWord:
            print(word)
        return

    current = currentNode.children.head

    while current is not None:
        j = current.value
        _findPrefixImpl(j, word + j.key, n-1)
        current  = current.nextNode

#Ejercicio 6
def inverted(T: Trie) -> bool:
    word = ""
    return _invertedImpl(T, T.root, word)

def _invertedImpl(T: Trie, node: TrieNode, word: str):
    if node.isEndOfWord:
        if LLgetNode(T.root.children, node.key):
            if search(T, word[::-1]):
                return True
    
    i = node.children.head
    while i:
        if _invertedImpl(T, i.value, word + i.value.key):
            return True
        i = i.nextNode

    return False


#Ejercicio 7
def autoComplete(T: Trie, s: str):
    currentNode = T.root

    for i in s:
        node = LLgetNode(currentNode.children, i)

        if node is None:
            return None

        currentNode = node

    match = ""
    return _autoCompleteImpl(T, currentNode, match)
    
def _autoCompleteImpl(T: Trie, node: TrieNode, match: str):
    nextNode = node.children.head
    
    if length(node.children) > 1 or nextNode is None:
        return match
        
    return _autoCompleteImpl(T, nextNode.value, match + nextNode.value.key)
            