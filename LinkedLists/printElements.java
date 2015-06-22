/**
 * https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list
 */
package LinkedLists;


public class printElements {

    public static void Print(Node head) {
        if (head == null) {
            return;
        } else {
            System.out.println(head.data);
            Print(head.next);
        }
    }

    public static void main(String args[]) {
        Node n3 = new Node(4, null);
        Node n2 = new Node(3, n3);
        Node n1 = new Node(2, n2);
        Node n = new Node(1, n1);
        Print(n);
    }
}
