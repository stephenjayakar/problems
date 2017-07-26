import java.io.*;
import java.util.*;

// Try to make solution that doesn't actually rotate, but is one operation
public class Solution {
    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int N = scanner.nextInt();
	int D = scanner.nextInt();
	
	int[] original = new int[N];
	for(int i = 0; i < N; i++) {
	    original[i] = scanner.nextInt();
	}

	int[] returnArr = new int[N];
	System.arraycopy(original, D, returnArr, 0, N - D);
	System.arraycopy(original, 0, returnArr, N - D, D);

	// print the return array
	for(int element : returnArr) {
	    System.out.print("%d ", element);
	}
    }
}
