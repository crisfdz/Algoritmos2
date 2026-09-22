from linkedlist import LinkedList, add as LLadd, getNodeValue as LLgetNode, delete as LLdelete

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
            
if __name__ == "__main__":

    T = Trie()

    insert(T, "casa")
    insert(T, "caso")
    insert(T, "cama")
    insert(T, "camino")
    insert(T, "casamiento")
    insert(T, "perro")
    insert(T, "perla")

    print("Palabras con prefijo 'ca' y longitud 4:")
    findPrefix(T, "ca", 4)

    print("\nPalabras con prefijo 'ca' y longitud 5:")
    findPrefix(T, "ca", 5)

    print("\nPalabras con prefijo 'cas' y longitud 4:")
    findPrefix(T, "cas", 4)

    print("\nPalabras con prefijo 'per' y longitud 5:")
    findPrefix(T, "per", 5)
    

    T1 = Trie()

    insert(T1, "casa")
    insert(T1, "caso")
    insert(T1, "cama")
    insert(T1, "camino")
    insert(T1, "casamiento")
    insert(T1, "perro")
    insert(T1, "perla")

    T2 = Trie()
    
    insert(T2, "casa")
    insert(T2, "caso")
    insert(T2, "cama")
    insert(T2, "camino")
    insert(T2, "casamiento")
    insert(T2, "perro")
    insert(T2, "perla")

    T3 = Trie()
    
    insert(T3, "cama")
    insert(T3, "casamiento")
    insert(T3, "perro")
    insert(T3, "camino")
    insert(T3, "casa")
    insert(T3, "perla")
    insert(T3, "caso")

    T4 = Trie()
    
    insert(T4, "chanchito feliz")
    insert(T4, "felipe")
    insert(T4, "perro")
    insert(T4, "camino")
    insert(T4, "ramon")
    insert(T4, "marie")
    insert(T4, "caso")

    print(compareTrie(T1, T2))
    print(compareTrie(T1, T3))
    print(compareTrie(T1, T4))