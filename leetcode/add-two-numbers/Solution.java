/* You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
*/


// Please rewrite this this is garbage
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
	// It's fine to lose the original two pointers, but not for solution
	ListNode solution = new ListNode(0);
	ListNode pointer = solution;
	ListNode lastPointer = solution;
	int carry = 0;
	while (l1 != null && l2 != null) {
	    int sum = l1.val + l2.val + carry;
	    pointer.val = sum % 10;
	    carry = (sum / 10);
	    l1 = l1.next;
	    l2 = l2.next;
	    pointer.next = new ListNode(0);
	    lastPointer = pointer;
	    pointer = pointer.next;
	}
	// Copy the not null linked list + carry to the solution
	ListNode l3 = notNullSwitch(l1, l2);
	while (l3 != null) {
	    int sum = l3.val + carry;
	    pointer.val = sum % 10;
	    carry = (sum / 10);
	    l3 = l3.next;
	    pointer.next = new ListNode(0);
	    lastPointer = pointer;
	    pointer = pointer.next;
	}

	if (carry != 0) {
	    pointer.val = carry;
	} else {
	    lastPointer.next = null;
	}
	return solution;
    }

    // A null switch that returns the pointer that is not null, or null if both
    private static ListNode notNullSwitch(ListNode o1, ListNode o2) {
	if (o1 != null) {
	    return o1;
	} else if (o2 != null) {
	    return o2;
	} else {
	    return null;
	}
    }
}
