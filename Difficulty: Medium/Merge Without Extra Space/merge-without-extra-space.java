import java.util.Arrays;

class Solution {
    // Function to merge the arrays
    public void mergeArrays(int a[], int b[]) {
        int n = a.length;
        int m = b.length;

        int i = n - 1;
        int j = 0;

        // Step 1: Swap largest of 'a' with smallest of 'b' if needed
        while (i >= 0 && j < m) {
            if (a[i] > b[j]) {
                // swap a[i] and b[j]
                int temp = a[i];
                a[i] = b[j];
                b[j] = temp;
            }
            i--;
            j++;
        }

        // Step 2: Sort both arrays to finalize order
        Arrays.sort(a);
        Arrays.sort(b);
    }
}
