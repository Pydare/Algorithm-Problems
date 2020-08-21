class Codec:

    def serialize(self, root):

        if not root:
            return ""

        res = []

        Q = collections.deque()
        Q.append(root)

        while Q:
            node = Q.popleft()
            if node:
                res.append(str(node.val))
                Q.append(node.left)
                Q.append(node.right)
            else:
                res.append('null')

        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if len(data) == 0:
            return None

        data = data.split(',')

        Q = collections.deque()
        root = TreeNode(data[0])
        Q.append(root)
        idx = 1

        while(Q):
            node = Q.popleft()

            if data[idx] != 'null':
                node.left = TreeNode(data[idx])            
                Q.append(node.left)

            idx += 1

            if data[idx] != 'null':
                node.right = TreeNode(data[idx])            
                Q.append(node.right)

            idx += 1        
        return root
#DFS

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ""

        data = []

        def helper(root):

            if not root:
                data.append('null')
                return

            data.append(str(root.val))
            helper(root.left)
            helper(root.right)

        helper(root)
        return ",".join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if len(data) == 0:
            return None

        data = data.split(',')

        def decoder(idx):
            if data[idx] != 'null':

                root = TreeNode(data[idx])

                left, idx = decoder(idx + 1)
                right, idx = decoder(idx + 1)

                root.left = left
                root.right = right
            else:
                root = None

            return root, idx

        return decoder(0)[0]

