from collections import deque

# Nodo con un contador para valores repetidos
class Node:
    def __init__(self, key):
        self.key = key
        self.count = 1
        self.left = None
        self.right = None

# Función para insertar un nuevo nodo con una clave dada en el BST
def insert(node, key):
    # Si el árbol está vacío, retorna un nuevo nodo
    if node is None:
        return Node(key)

    # De otra manera, recurre por el árbol
    if key == node.key:
        node.count += 1
    elif key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

# Función de utilidad para buscar una clave en un BST
def search(root, key):
    # Casos base: root es null o la clave está en la raíz
    if root is None or root.key == key:
        return root

    # La clave es mayor que la clave de la raíz
    if root.key < key:
        return search(root.right, key)

    # La clave es menor que la clave de la raíz
    return search(root.left, key)

# Recorrido inorder del BST
def inorder(root):
    if root:
        inorder(root.left)
        for _ in range(root.count):
            print(root.key, end=" ")
        inorder(root.right)

# Recorrido preorder del BST
def preorder(root):
    if root:
        for _ in range(root.count):
            print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)

# Recorrido postorder del BST
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        for _ in range(root.count):
            print(root.key, end=" ")

# Devolver la altura del BST
def height(node):
    if node is None:
        return 0
    else:
        left_depth = height(node.left)
        right_depth = height(node.right)
        return max(left_depth, right_depth) + 1

# Imprimir nodos a un nivel dado
def print_given_level(root, level):
    if root is None:
        return
    if level == 1:
        for _ in range(root.count):
            print(root.key, end=" ")
    elif level > 1:
        print_given_level(root.left, level - 1)
        print_given_level(root.right, level - 1)

# Función para imprimir el orden de nivel del BST
def print_level_order(root):
    h = height(root)
    for i in range(1, h+1):
        print_given_level(root, i)
        print()

# Nodo con valor mínimo en el árbol
def min_value_node(node):
    current = node
    while current and current.left is not None:
        current = current.left
    return current

# Nodo con valor máximo en el árbol
def max_value_node(node):
    current = node
    while current and current.right is not None:
        current = current.right
    return current

# Función para eliminar un nodo
def delete_node(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.count > 1:
            root.count -= 1
            return root
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = max_value_node(root.left)
        root.key = temp.key
        root.count = temp.count
        temp.count = 1
        root.left = delete_node(root.left, temp.key)
    return root

# Driver Code
if __name__ == '__main__':
    """ 
    Let us create following BST 
         50 
        /	 \ 
    30	 70 
    / \ / \  
20 40 60 80 
/
10   
    """
    root = None

    # Inserting value 50
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    insert(root, 10)

    print("Search of 70 in tree:", search(root, 70).key)
    
    result = search(root, 100)
    if result is not None:
         print("Search of 100 in tree:", result.key)
    else:
        print("100 is not in the tree")

    # Print the BST
    print("Inorder Traversal:", end=" ")
    inorder(root)
    print()

    print("Preorder Traversal:", end=" ")
    preorder(root)
    print()

    print("Postorder Traversal:", end=" ")
    postorder(root)
    print()

    print(f"The height of the binary tree is {height(root)}")

    print("The binary tree by levels is the following:")
    print_level_order(root)

    print("\nDelete 50")
    root = delete_node(root, 50)
    print("Inorder Traversal after deletion of 50:", end=" ")
    inorder(root)

    print("\nDelete 10")
    root = delete_node(root, 10)
    print("Inorder Traversal after deletion of 10:", end=" ")
    inorder(root)
