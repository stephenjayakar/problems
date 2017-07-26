import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int Q = scanner.nextInt();
        ArrayList<ArrayList<Integer>> seqList = new ArrayList<>(N);
        // Initializing the arraylists
        for (int i = 0; i < N; i++) {
            seqList.add(new ArrayList<Integer>());
        }
        int lastAnswer = 0;

        for (int i = 0; i < Q; i++) {
            int choice = scanner.nextInt();
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            int index = ((x ^ lastAnswer) % N);
            ArrayList<Integer> seq = seqList.get(index);
            
            if (choice == 1) {
                seq.add(y);
            } else {
                lastAnswer = seq.get(y % seq.size());
                System.out.println(lastAnswer);
            }
        }
    }
}
