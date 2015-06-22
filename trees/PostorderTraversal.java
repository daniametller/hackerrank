package Trees;

/**
 * https://www.hackerrank.com/challenges/tree-postorder-traversal
 */
public class PostorderTraversal {

    public static void Postorder(BinaryTreeNode root) {
        if (root == null) {
            return;
        }
        Postorder(root.left);
        Postorder(root.right);
        System.out.print(root.data + " ");
    }

    public static void main(String args[]) {
        BinaryTreeNode n1 = new BinaryTreeNode(1, null, null);
        BinaryTreeNode n2 = new BinaryTreeNode(4, null, null);
        BinaryTreeNode n3 = new BinaryTreeNode(6, null, null);
        BinaryTreeNode n4 = new BinaryTreeNode(5, n1, n2);
        BinaryTreeNode n5 = new BinaryTreeNode(2, n3, null);
        BinaryTreeNode tree = new BinaryTreeNode(3, n4, n5);
        Postorder(tree);
    }
}
