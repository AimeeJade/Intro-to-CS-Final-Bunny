/**
 * An implementation of the List ADT using
 * a linked list.  Specifically, this implementation
 * only allows a List to contain Comparable items.
 *
 * @author Layla Oesper 
 * @author Eric Alexander
 * @author Aimee Yuan
 */

/* Note <E extends Comparable<E> means this container
 * can only old objects of type E that are Comparable.
 */
public class RecursiveLinkedList<E extends Comparable<E>>{

    /* Internal Node class used for creating linked objects.
     */
    private class Node<E> {
        private E data;
        private Node<E> next;

        private Node(E dataItem) {
            data = dataItem;
            next = null;
        }

        private Node(E dataItem, Node<E> nextNode) {
            data = dataItem;
            next = nextNode;
        }

    } // End Node class

    //Instance variables for RecursiveLinkedList
    private Node<E> head;
    private int numItems;

    /**
     * Creates an empty RecursiveLinkedList
     */
    public RecursiveLinkedList() {
        head = null;
        numItems = 0;
    }

    /**
     * Returns the data stored at positon index.
     * @param index
     * @return The data stored at position index. 
     */
    public E get(int index) {
        if (index < 0 || index >= numItems) {
            throw new IndexOutOfBoundsException(Integer.toString(index));
        }
        Node<E> node = getNode(index);
        return node.data;
    }

    /*
     * Helper method that retrieves the Node<E> stored at
     * the specified index.
     */
    private Node<E> getNode(int index) {
        Node<E> node = head;
        for (int i = 0; i < index && node != null; i++) {
            node = node.next;
        }
        return node;
    }

    /**
     * Removes and returns the data stored at the specified index.
     * @param index The position of the data to remove.
     * @return The data previously stored at index position.
     */
    public E remove(int index) {
        if (index < 0 || index >= numItems) {
            throw new IndexOutOfBoundsException(Integer.toString(index));
        }

        if (index == 0){
            return removeFirst();
        } else {
            Node<E> before = getNode(index - 1);
            return removeAfter(before);
        }
    }

    /*
     * Helper method that removes the Node<E> after the
     * specified Node<E>. Returns the data that was
     * stored in the removed node.
     */
    private E removeAfter(Node<E> node) {
        Node<E> temp = node.next;
        if (temp != null) {
            node.next = temp.next;
            numItems--;
            return temp.data;
        } else {
            return null;
        }
    }

    /*
     * Helper method that removes the first Node<E> in
     * the Linked List.  Returns the data that was
     * stored in the removed node.
     */
    private E removeFirst() {
        Node<E> temp = head;
        if (head != null) {
            head = head.next;
        }

        if (temp != null) {
            numItems--;
            return temp.data;
        } else {
            return null;
        }
    }

    /**
     * Adds the data to the list at the specified index.
     * @param index The position to add the data.
     * @param anEntry The particular data to add to the list.
     */
    public void add(int index, E anEntry) {
        if (index < 0 || index > numItems) {
            throw new IndexOutOfBoundsException(Integer.toString(index));
        }
        if (index == 0) {
            addFirst(anEntry);
        } else {
            Node<E> node = getNode(index - 1);
            addAfter(node, anEntry);
        }
    }

    /*
     * Helper method that adds anEntry to the first
     * position in the list.
     */
    private void addFirst(E anEntry) {
        head = new Node<E>(anEntry, head);
        numItems++;
    }

    /*
     * Helper method that adds anEntry after the
     * specified Node<E> in the linked list.
     */
    private void addAfter(Node<E> before, E anEntry) {
        before.next = new Node<E>(anEntry, before.next);
        numItems++;
    }

    /**
     * Add the specified data to the end of the list.
     * @param anEntry The data to add to this list.
     */
    public boolean add(E anEntry) {
        add(numItems, anEntry);
        return true;
    }

    /**
     * Returns the size of the list in terms of items stored.
     * @returns the number of items in the list.
     */
    public int size() {
        return numItems;
    }

    /**
     * Modifies the list so the specified index now 
     * contains newValue (overwriting the old data).
     * @param index The position int he list to add data.
     * @param newValue The data to place in the list.
     * @return The previous data value stored at index.
     */
    public E set(int index, E newValue) {
        if (index < 0 || index >= numItems) {
            throw new IndexOutOfBoundsException(Integer.toString(index));
        }
        Node<E> node = getNode(index);
        E result = node.data;
        node.data = newValue;
        return result;
    }

    /**
     * A string representation of the List.
     * @returns A string representation of the list.
     */
    public String toString() {
        String s = "[";
        Node<E> temp = head;
        for (int i = 0; i < numItems; i++) {
            s = s + temp.data.toString();
            if (i < numItems - 1) {
                s = s + ", ";
            }
            temp = temp.next;
        }
        s = s + "]";
        return s;
    }

    //Returns the max element of the list
    public E max(){
        return maxHelper(head, null);
    }

    //Helper class with parameters of a node current and a max value
    private E maxHelper(Node<E> current, E max) {
        //If there are no items in the list, the max is null
        if (numItems == 0){
            return null;
        }
        //Make max equal to the first item in the list
        if (max == null){
            max = current.data;
        }
        //stop the recursion when you have travered through the entire list
        if (current == null){
            return max;
        }
        //compare max to the current node's data. If the data is larger, make it the new max
        if (current.data.compareTo(max) >= 0){
            max = current.data;
        }
        //recursive step 
        return maxHelper(current.next, max);
    }

    //Remove all nodes in the list with the same data as element
    public void removeAll(E element){
        removeHelper(head, element, 0);
    }
    //Helper class with parameters of a current node, element/data, and index
    private void removeHelper(Node<E> current, E element, int index) {
        //Stop the recursion after traversing through the entire list for nodes with this element as its data
        if (current == null){
            return;
        }
        //If the data of the current node is equal to the element, remove the node from the list
        if (current.data.equals(element)){
            remove(index);
            index--;
        }
        //increment the index to travers the list
        index++;
        //recursive step
        removeHelper(current.next, element, index);
    }
    
    //Duplicate each element of the list
    public void duplicate(){
        helperDuplicate(head, 0);
    }
    //Helper class with parameters of a current node and a index
    private void helperDuplicate(Node<E> current, int index){
        //If there are no items in the list, change nothing about the list
        if (numItems == 0){
            return;
        }
        //stop the recursion/traversing when you reach the end of the list
        if (current == null){
            return;
        }
        //While the index has not reached the end of the list, add a node after each of the original nodes that are its duplicate right after it
        if (index != numItems){
            add(index + 1, current.data);
            //Move to the next original node to duplicate it
            index = index + 2;
        }
        //recursize step
        helperDuplicate(current.next.next, index);
    }

    //Sample Test Cases
    public static void main(String[] args) {
        System.out.println("Test Cases"+ "\n");
        RecursiveLinkedList<String> list = new RecursiveLinkedList<String>();
        list.add("hello");
        list.add("world");
        list.add("zebra");
        list.add("apple");

        System.out.println("String list is: " + list);
        System.out.println("Max is: " + list.max());
        list.removeAll("zebra");
        System.out.println("Removed zebra: " + list);
        list.duplicate();
        System.out.println("Duplicated list: " + list);

        System.out.println();
        RecursiveLinkedList<Integer> list2 = new RecursiveLinkedList<Integer>();
        list2.add(2);
        list2.add(5);
        list2.add(1);
        list2.add(7);
        System.out.println("int list is: " + list2);
        System.out.println("Max is: " + list2.max());
        list2.removeAll(5);
        System.out.println("Removed 5: " + list2);
        list2.duplicate();
        System.out.println("Duplicated list: " + list2);
    }

}
