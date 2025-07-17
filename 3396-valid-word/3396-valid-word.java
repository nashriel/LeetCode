class Solution {
    public boolean isValid(String word) {
        if (word.length() < 3)
           return false;
        String vowels = "aeeiouAEIOU";
        boolean hasVowels = false;
        boolean hasCons = false;
        for (char c: word.toCharArray()){
            if (!Character.isLetterOrDigit(c))
             return false;
            if (Character.isLetter(c)){
                if (vowels.indexOf(c) != -1){
                     hasVowels = true;
                }else{
                    hasCons = true;
                }
               
            }
        }
        return hasVowels && hasCons;
    }
}