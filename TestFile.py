import unittest
from BinaryTree import BinaryTree, BinaryTreeNode

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree('TestTree', BinaryTreeNode(5))

    def test_insert_and_traversal(self):
        # Insert nodes
        self.tree.root.insertNode(3)
        self.tree.root.insertNode(7)
        self.tree.root.insertNode(1)
        self.tree.root.insertNode(4)

        # Capture prints
        import io
        import sys
        old_stdout = sys.stdout
        sys.stdout = capturedOutput = io.StringIO()

        # Perform in-order traversal
        self.tree.OrderTraversal(self.tree.root, 'inOrder')

        # Reset stdout
        sys.stdout = old_stdout

        self.assertEqual(capturedOutput.getvalue(), '1\n3\n4\n5\n7\n')

if __name__ == '__main__':
    unittest.main()