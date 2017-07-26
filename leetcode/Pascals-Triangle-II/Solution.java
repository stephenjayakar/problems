import java.util.List;
import java.util.ArrayList;

public class Solution {
    // The row replaces itself rather than saving all the rows
    public List<Integer> getRow(int rowIndex) {
	ArrayList<Integer> row = new ArrayList<>();
	// The initial config
	row.add(1);
	if (rowIndex == 0) {
	    return row;
	}
	row.add(1);
	for (int i = 1; i < rowIndex; i++) {
	    row = nextRow(row);
	}
	return row;
    }

    private ArrayList<Integer> nextRow(List<Integer> row) {
	ArrayList<Integer> returnRow = new ArrayList<>();
	// Seeding first value
	returnRow.add(1);
	for (int i = 1; i < row.size(); i++) {
	    int newValue = (row.get(i - 1) + row.get(i));
	    returnRow.add(newValue);
	}
	// Seeding last value
	returnRow.add(1);
	return returnRow;
    }

    public static void main(String[] args) {
	System.out.println(getRow(3));
    }
}
