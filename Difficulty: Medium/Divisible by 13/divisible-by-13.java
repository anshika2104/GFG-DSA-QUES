class Solution {
    public boolean divby13(String s) {
        // code here
        // int n=Integer.parseInt(s);
        // if (n%13==0){
        //     return true;
        // }
        // return false;
        int r=0;
        for(int i=0;i<s.length();i++){
            int dig=s.charAt(i)-'0';
            r=(r*10+dig)%13;
        }
        return r==0;
    }
}