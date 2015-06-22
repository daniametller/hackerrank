package Trees;

/**
 * https://www.hackerrank.com/challenges/tree-inorder-traversal
 */
public class InorderTraversal {

    public static void Inorder(BinaryTreeNode root) {
        if (root == null) {
            return;
        }
        Inorder(root.left);
        System.out.print(root.data + " ");
        Inorder(root.right);
    }

    public static void main(String args[]) {
        BinaryTreeNode n1 = new BinaryTreeNode(1, null, null);
        BinaryTreeNode n2 = new BinaryTreeNode(4, null, null);
        BinaryTreeNode n3 = new BinaryTreeNode(6, null, null);
        BinaryTreeNode n4 = new BinaryTreeNode(5, n1, n2);
        BinaryTreeNode n5 = new BinaryTreeNode(2, n3, null);
        BinaryTreeNode tree = new BinaryTreeNode(3, n4, n5);
        Inorder(tree);
    }

}
