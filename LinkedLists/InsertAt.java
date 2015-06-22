package LinkedLists;

/**
 * https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list
 */

//3 0
//5 1
//4 2
//2 4
//10 1
public class InsertAt {

    public static Node InsertNth(Node head, int data, int position) {
        if (head == null) {
            Node n = new Node();
            n.data = data;
            n.next = null;
            head = n;
        } else {
            if (position == 0) {
                Node n = new Node();
                n.data = data;
                n.next = head;
                head = n;
            } else {
                head.next = InsertNth(head.next, data, position - 1);
            }
        }
        return head;
    }

    public static void main(String args[]) {
        Node n1 = InsertNth(null, 3, 0);
        Node n2 = InsertNth(n1, 5, 1);
        Node n3 = InsertNth(n2, 4, 2);
        Node n4 = InsertNth(n3, 2, 4);
        Node n5 = InsertNth(n4, 10, 1);
    }
}
