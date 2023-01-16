# Que: Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1 = []

        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            l1.append(root.val)
            inorder(root.right)
        inorder(root1)
        inorder(root2)

        l1.sort()
        return l1
