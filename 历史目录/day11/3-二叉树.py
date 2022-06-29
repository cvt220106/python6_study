# @Author : 杨佳杰
# @Time   : 2022/6/10 10:50
# @File   : 3-二叉树.py
class TreeNode:
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    def __init__(self):
        self.root = None
        self.queue = []

    def insert(self, ele):
        """
        插入新节点
        :param ele:
        :return:
        """
        new_node = TreeNode(ele)
        # 新元素入队
        self.queue.append(new_node)
        # 新结点入树
        if self.root is None:
            self.root = new_node  # 树为空,则作为根结点
        else:
            if self.queue[0].lchild is None:  # 先判别左节点
                self.queue[0].lchild = new_node
            elif self.queue[0].rchild is None:
                self.queue[0].rchild = new_node
                self.queue.pop(0)  # 左右结点均不空时,弹出该节点

    def perorder_digui(self, root: TreeNode):
        """
        前序遍历
        :param TreeNode:
        :return:
        """
        if root is None:
            return
        print(root.elem, end='')
        self.perorder_digui(root.lchild)
        self.perorder_digui(root.rchild)

    def inorder_digui(self, root: TreeNode):
        """
        中序遍历
        :param TreeNode:
        :return:
        """
        if root is None:
            return
        self.inorder_digui(root.lchild)
        print(root.elem, end='')
        self.inorder_digui(root.rchild)

    def postorder_digui(self, root: TreeNode):
        """
        后序遍历
        :param TreeNode:
        :return:
        """
        if root is None:
            return
        self.postorder_digui(root.lchild)
        self.postorder_digui(root.rchild)
        print(root.elem, end='')

    def levelorder(self, root: TreeNode):
        """
        层序遍历
        :param root:
        :return:
        """
        if root is None:
            return
        myQueue = []  # 辅助队列
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.elem, end='')
            if node.lchild is not None:
                myQueue.append(node.lchild)
            if node.rchild is not None:
                myQueue.append(node.rchild)

    def perorder_while(self, root: TreeNode):
        if root is None:
            return
        mystack = []
        node = root
        while node or mystack:
            while node:
                print(node.elem, end='')
                mystack.append(node)
                node = node.lchild
            node = mystack.pop()
            node = node.rchild


if __name__ == '__main__':
    t = Tree()
    for i in 'abcdefghij':
        t.insert(i)
    t.inorder_digui(t.root)
    print()
    t.perorder_digui(t.root)
    print()
    t.postorder_digui(t.root)
    print()
    t.levelorder(t.root)
    print()
    t.perorder_while(t.root)
