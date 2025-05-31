class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        // code here
             List<Integer> list = new ArrayList<>();
        
        for (int[] row : matrix) {
            for (int val : row) {
                list.add(val);
            }
        }

        Collections.sort(list);
        return list.get(k - 1); // k-th smallest
    }
    }
