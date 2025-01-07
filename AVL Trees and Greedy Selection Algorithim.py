# AVL tree algorithims
# AVL Insert: O(logn)
# AVL Delete: O(logn)
# AVL Rebalance: O(logn)
# AVL Rotations: O(1)
# AVL Search: O(logn)
# AVl Successor: O(logn)

class Node:
    def __init__(self, key: int, p = None, l = None, r = None, h = 1):
        self.left = l
        self.right = r
        self.parent = p
        self.value = key
        self.height = h
        
class Tree:
    def __init__(self, key):
        self.root = Node(key)
        
def left_rotate(T: Tree, x: Node):
    y = x.right
    x.right = y.left
    if y.left:
        y.left.parent = x
        y.parent = x.parent
    if not x.parent:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y
    
def right_rotate(T: Tree, y: Node):
    x = y.left
    y.left = x.right
    if x.right:
        x.right.parent = y
    x.parent = y.parent
    if not y.parent:
        T.root = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x
    x.right = y
    y.parent = x


def avl_insert(T: Tree, key: int):
    cur, cur_p = T.root, None
    while cur:
        cur_p = cur
        if key == cur.value:
            print("The given key already exists:", key)
            return
        elif key < cur.value:
            cur = cur.left
        else:
            cur = cur.right
    new_node = Node(key, cur_p)
    if not cur_p:
        T.root = new_node
    elif key < cur_p.value:
        cur_p.left = new_node
    else:
        cur_p.right = new_node
    avl_fixup(T, new_node)

def avl_fixup(T: Tree, z: Node):
    while z:
        z.height = 1 + max(height(z.left), height(z.right))
        bf = balance_factor(z)
        # Create Case for left/right heavy AVL trees
        # Right Heavy:
        if bf > 1:
            if balance_factor(z.left) >= 0:
                return right_rotate(T, z)
            else:
                z.left = left_rotate(T, z.left)
                return right_rotate(T, z)
            #Left Heavy (Mirror right heavy fix)
            if bf < -1:
                if balance_factor(z.right) <= 0:
                    return left_rotate(T, z)
                else:
                    z.right = right_rotate(T, z.right)
                    return left_rotate(T, z)
        z = z.parent
        if height(z) > height(T.root):
            break
        
def height(Node):
    if Node is None:
        return 0
    return Node.height

def balance_factor(Node):
    if Node is None:
        return 0
    return height(Node.left)- height(Node.right)


def search_tree(Node, key: int):
    if Node is None:
        return None
    if Node.value == key:
        return Node
    if key < Node.value:
        return search_tree(Node.left, key)
    if key > Node.value:
        return search_tree(Node.right, key)
    
def delete_node(T, Node):
    if Node.left is None:
        child = Node.right
    elif Node.right is None:
        child = Node.left
    else:
        successor = find_successor(Node)
        Node.value = successor.value
        delete_node(T, successor)
        return
    if Node.parent is None:
        T.root = child
    elif Node == Node.parent.left:
        Node.parent.left = child
    else:
        Node.parent.right = child
    if child is not None:
        child.parent = Node.parent

def find_successor(Node):
    current = Node.right
    while current.left:
        current = current.left
    return current

def avl_delete(T: Tree, key: int):
    removal = search_tree(T.root, key)
    if removal is None:
        return print("Key doesn't exist")
    delete_node(T, removal)
    avl_fixup(T, removal)
      
    
def printBST(tree: Tree):
    print_helper(tree.root, 1)
    
def print_helper(root: Node, depth: int):
    tab = " "*(depth*5)
    if not root:
        print(tab, "None")
        return
    print_helper(root.right, depth + 1)
    print(tab + str(root.value) + "(" + str(root.height) + ")")
    print_helper(root.left, depth + 1)
    
def arrayToBST(nums: list[int]):
    tree = Tree(nums[0])
    for n in nums[1:]:
        avl_insert(tree, n)
        printBST(tree)
        print("-----------------------------------------------")
    return tree

# Test:

tree = arrayToBST([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
avl_delete(tree, 3)
printBST(tree)
print("-----------------------------------------------")
avl_delete(tree, 1)
printBST(tree)
print("-----------------------------------------------")
avl_delete(tree, 10)
printBST(tree)


# Greedy Algorithim for activity optimization: O(nlogn)

def minimumRemoval(n):
    act_list = []
    rem_list = []
    act_list.append(n[0])
    for k in range(1, len(n)):
        z = len(act_list) - 1
        if n[k][0] < act_list[z][1]:
            rem_list.append(n[k])
        else:
            act_list.append(n[k])
    return len(rem_list)
        
# Test:

print(minimumRemoval([(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11),
(8, 12), (2, 14), (12, 16)]))
print(minimumRemoval([(1,2),(2,3),(3,4),(1,3)]))
print(minimumRemoval([(1,2),(1,2),(1,2)]))
print(minimumRemoval([(1,2),(2,3)]))
print(minimumRemoval([(0,1),(0,1),(0,1)]))
print(minimumRemoval([(0,1),(1,2)]))

    
    


        

