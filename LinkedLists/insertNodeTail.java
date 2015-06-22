package LinkedLists;

/**
 * https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list
 */

public class insertNodeTail {

    private static Node Insert(Node head, int x) {
        if (head == null) {
            head = new Node();
            head.next = null;
            head.data = x;
        } else {
            if (head.next == null) {
                Node aux = new Node();
                aux.data = x;
                aux.next = null;
                head.next = aux;
            } else {
                head.next = Insert(head.next, x);
            }
        }
        return head;
    }

    public static void main (String args[]) {
        Node n = Insert(null, 2);
        Node n2 = Insert(n, 3);
        Node n3 = Insert(n2, 4);
    }
}
