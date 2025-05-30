class Solution {
    public List<Integer> findDuplicates(int[] arr) {
        // code here
        ArrayList<Integer>l=new ArrayList<>();
        HashSet<Integer>dup=new HashSet<>();
        for(int i:arr){
            if(dup.contains(i)){
                l.add(i);
            }
            else{
                dup.add(i);
            }
        }
        return l;
    }
}