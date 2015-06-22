package Trees;

/**
 * http://www.geeksforgeeks.org/diameter-of-a-binary-tree/
 */
public class TreeDiameter {

    public static int diameterOfTree(BinaryTreeNode root) {
        /* For your reference
           class Node {
               Node left, right;
               int data;
                       Node(int newData) {
                   left = right = null;
                   data = newData;
               }
           }
        */
        if (root == null) {
            return 0;
        }
        int lheight = height(root.left);
        int rheight = height(root.right);

        int ldiameter = diameterOfTree(root.left);
        int rdiameter = diameterOfTree(root.right);

        return Math.max(lheight + rheight + 1, Math.max(ldiameter, rdiameter));

    }

    private static int height(BinaryTreeNode root) {
        if (root == null) {
            return 0;
        }
        return Math.max(height(root.left), height(root.right)) +1;
    }

    public static void main(String args[]) {
        BinaryTreeNode n1 = new BinaryTreeNode(1, null, null);
        BinaryTreeNode n2 = new BinaryTreeNode(4, null, null);
        BinaryTreeNode n3 = new BinaryTreeNode(6, null, null);
        BinaryTreeNode n4 = new BinaryTreeNode(5, n1, n2);
        BinaryTreeNode n5 = new BinaryTreeNode(2, n3, null);
        BinaryTreeNode tree = new BinaryTreeNode(3, n4, n5);
        System.out.println(diameterOfTree(tree));
    }


}
