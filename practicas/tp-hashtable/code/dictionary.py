from linkedlist import LinkedList, add as LLAdd, search_key, to_string, length

#Ejercicio 2
class Dictionary:
    def __init__(self, size):
        self.size = size
        self.dictionary = [None] * size


def hash_function(k, m):
    return hash(k) % m

def insert(D: Dictionary, key, value):
    index = hash_function(key, D.size)
    if D.dictionary[index] is None:
        D.dictionary[index] = LinkedList()

    LLAdd(D.dictionary[index], (key, value))
    return D

def search(D: Dictionary, key):
    index = hash_function(key, D.size)
    linkedlist = D.dictionary[index]
    if linkedlist is None:
        return None
    
    node = search_key(linkedlist, key)
    if node is not None:
        return node.value[1] 
    else:
        return None

def delete(D: Dictionary, key) -> Dictionary:
    index = hash_function(key, D.size)
    linkedlist = D.dictionary[index]
    if linkedlist is None:
        return D
    
    currentNode = linkedlist.head
    previousNode = None
    while currentNode is not None:
        if currentNode.value[0] == key:
            if previousNode is None:
                linkedlist.head = currentNode.nextNode
            else:
                previousNode.nextNode = currentNode.nextNode
            return D
        
        previousNode = currentNode
        currentNode = currentNode.nextNode
    
    return D


def print_dictionary(D: Dictionary):
    for i, linkedlist in enumerate(D.dictionary):
        print(f"Index {i}: {to_string(linkedlist)}")

#Ejercicio 4
def permutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    D = Dictionary(len(s1))
    
    for k in s1:
        count = search(D, k)
        if count is None:
            insert(D, k, 1)
        else:
            insert(D, k, count + 1)

    for k in s2:
        count = search(D, k)
        if count is None or count == 0:
            return False
        else:
            insert(D, k, count - 1)

    return True

#Ejercicio 5
def unique_elements(L: list) -> bool:
    D = Dictionary(len(L))
    
    for element in L:
        if search(D, element) is not None:
            return False
        insert(D, element, True)
    
    return True


#Ejercicio 6
def hash_codigo_postal(cp: str, m: int) -> int:
    if len(cp) != 8:
        print("Código postal inválido")
        return -1

    c1 = ord(cp[0])
    d = int(cp[1:5])
    c2 = ord(cp[5])
    c3 = ord(cp[6])
    c4 = ord(cp[7])

    return (c1 * 31**5 + d * 31**4 + c2 * 31**3 + c3 * 31**2 + c4 * 31) % m

#Ejercicio 7
def compress_string(s: str) -> str:
    D = Dictionary(len(s))
    last_index = 0

    for i in range(len(s)):
        if s[i] != s[i-1]:
            last_index = i
        insert(D, last_index, s[i])
        result = _compress(D)

    return result if result is not None else s

def _compress(D: Dictionary) -> str | None:
    compressed = ""
    is_equal = True
    for i in range(D.size):
        linkedlist = D.dictionary[i]
        if linkedlist is not None:
            if length(linkedlist) > 1:
                is_equal = False
                compressed += f"{linkedlist.head.value[1]}{length(linkedlist)}"
    return None if is_equal else compressed

#Ejercicio 8
def find_substring(a: str, p: str) -> int:
    n = len(a)
    m = len(p)
    if m > n:
        return -1

    base = 31
    mod = 10**9 + 7

    highest_power = pow(base, m - 1, mod)

    p_hash = 0
    window_hash = 0

    for i in range(m):
        p_hash = (p_hash * base + ord(p[i])) % mod
        window_hash = (window_hash * base + ord(a[i])) % mod

    for i in range(n - m + 1):
        if p_hash == window_hash:
            if a[i:i + m] == p:
                return i

        if i < n - m:
            window_hash = (window_hash - ord(a[i]) * highest_power) % mod
            window_hash = (window_hash * base + ord(a[i + m])) % mod
            window_hash = (window_hash + mod) % mod

    return -1

#Ejercicio 9

def is_subset(S: list, T: list) -> bool:
    D = Dictionary(len(T))
    for element in T:
        insert(D, element, True)

    for element in S:
        if search(D, element) is None:
            return False

    return True


if __name__ == "__main__":
    D = Dictionary(9)
    keys_to_insert = [5, 28, 19, 15, 20, 33, 12, 17, 10]
    for key in keys_to_insert:
        insert(D, key, key)
    print_dictionary(D)
    print(search(D, 15))
    print(search(D, 100))
    print_dictionary(delete(D, 15))

    print(permutation("jamon", "monja"))
    print(unique_elements([1, 2, 3, 4, 5]))
    print(unique_elements([1, 2, 3, 4, 4]))

    print(compress_string("aabcccccaaa"))

    print(find_substring("ababcabcabababd", "ababd"))
    print(is_subset([2, 4, 3], [1, 2, 3, 4, 5]))