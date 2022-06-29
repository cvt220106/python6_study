# @Author : 杨佳杰
# @Time   : 2022/6/13 16:03
# @File   : 4-红黑树.py
RED = 0
BLACK = 1


class RedBlackTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.p = None  # 指向父节点
        self.color = RED


def left_rotate(tree, node: RedBlackTreeNode):
    # 传递tree对象是为了防止node是树根的情况出现
    if not node.right:
        return False
    node_right = node.right
    node_right.p = node.p  # 1
    if not node.p:  # node结点无父节点时,说明node为根
        tree.root = node_right  # 2
    elif node == node.p.left:
        node.p.left = node_right  # 2
    else:
        node.p.right = node_right  # 2
    if node_right.left:
        node_right.left.p = node  # 3
    node.right = node_right.left  # 4
    node_right.left = node  # 5
    node.p = node_right  # 6


def right_rotate(tree, node: RedBlackTreeNode):
    if not node.left:
        return False
    node_left = node.left
    node_left.p = node.p  # 1
    if not node.p:
        tree.root = node_left  # 2
    elif node == node.p.left:
        node.p.left = node_left  # 2
    else:
        node.p.right = node_left  # 2
    if node_left.right:
        node_left.right.p = node  # 3
    node.left = node_left.right  # 4
    node_left.right = node  # 5
    node.p = node_left  # 6


# key就是父亲的值，direction是左边还是右边
def rbtree_print(node, key, direction):
    if node:
        if direction == 0:  # tree是根节点
            print("%2d(B) is root" % node.value)
        else:  # tree是分支节点
            print("%2d(%s) is %2d's %6s child" % (
                node.value, ("B" if node.color == 1 else "R"),
                key, ("right" if direction == 1 else "left")))
        rbtree_print(node.left, node.value, -1)
        rbtree_print(node.right, node.value, 1)


class RedBlackTree:
    def __init__(self):
        self.root: RedBlackTreeNode = None

    def __insert_fixup(self, node):  # 红黑树插入后的调整策略
        parent: RedBlackTreeNode = node.p  # 记录父节点
        while parent and parent.color == 0:  # 父节点存在且父节点为红时,才需要调整!
            gparent: RedBlackTreeNode = parent.p  # 因为父节点存在且为红,因此一定不为根节点,所以爷结点一定存在
            if parent is gparent.left:  # 左半区调整策略
                uncle: RedBlackTreeNode = gparent.right  # 记录叔结点
                # 情形三：红叔，叔父爷变色，爷为新节点继续调整
                if uncle and uncle.color == RED:
                    parent.color = BLACK
                    uncle.color = BLACK
                    gparent.color = RED
                    node = gparent
                    parent = node.p
                    continue
                # 情形4，黑叔或叔叔不存在，LR型，先做R型单左旋，再借情形5做L型单右旋
                if node is parent.right:
                    left_rotate(self, parent)
                    parent, node = node, parent
                # 情形五LL型，单右旋
                right_rotate(self, gparent)
                parent.color = BLACK
                gparent.color = RED
            else:  # 右半区
                uncle: RedBlackTreeNode = gparent.left
                # 情形三：红叔，叔父爷变色，爷为新节点
                if uncle and uncle.color == RED:
                    parent.color = BLACK
                    uncle.color = BLACK
                    gparent.color = RED
                    node = gparent
                    parent = node.p
                    continue
                # 情形4，黑叔或叔叔不存在，RL型，先做L型单右旋，再借情形5做R型单左旋
                if node is parent.left:
                    right_rotate(self, parent)
                    parent, node = node, parent
                # 情形五RR型，单左旋
                left_rotate(self, gparent)
                parent.color = BLACK
                gparent.color = RED
        self.root.color = BLACK  # 统一置根为黑色,可以覆盖情形1为根节点,以及情形3递推至根节点时导致根节点为红的情况

    def insert(self, node: RedBlackTreeNode):
        # 第一步，放入节点，二分查找
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node:  # 不断下沉循环找到元素插入所对应的父节点位置
                parent = current_node
                if current_node.value > node.value:
                    current_node = current_node.left
                else:
                    current_node = current_node.right
            node.p = parent  # 插入
            if parent.value > node.value:  # 连接
                parent.left = node
            else:
                parent.right = node
        # 插入后开始调整,使整棵树满足红黑树的特性
        self.__insert_fixup(node)


def main():
    number_list = (7, 4, 1, 8, 5, 2, 9, 6, 3)
    tree = RedBlackTree()
    for number in number_list:
        node = RedBlackTreeNode(number)
        tree.insert(node)
        # rbtree_print(tree.root, 0, 0)  #如果树不对，就每一个结点放进去就打一下
    rbtree_print(tree.root, 0, 0)


if __name__ == '__main__':
    main()
