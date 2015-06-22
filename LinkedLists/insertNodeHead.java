package LinkedLists;

public class insertNodeHead {

    public static Node Insert(Node head,int x) {
        Node n = new Node();
        n.data = x;
        if (head == null) {
            n.next = null;
            return n;
        } else {
            n.next = head;
        }
        return n;
    }

    public static void main(String args[]) {
        Node n = Insert(null, 1);
        Node n2 = Insert(n, 2);
        Node n3 = Insert(n2, 3);
    }

}
