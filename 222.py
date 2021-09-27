import Queue
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        queue = Queue.Queue()
        node = root
        queue.put(node)
        count = 0
        for i in range(0, 5 * 10**4):
            if queue.empty():
                break
            node = queue.get()
            count = count + 1
            if node.left != None:
                queue.put(node.left)
            if node.right != None:
                queue.put(node.right)
            
                
        return count

print(Solution().countNodes([1,2,3,4,5,6]))