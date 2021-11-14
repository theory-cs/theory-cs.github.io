public class RNAStrand {

    // Helper method which recursively prints all RNA strands of given length, in alphabetical order
    private static void alphOrderStrandsFixedLength(int length, String prefix) {
        if (length == 1) {
            System.out.print(prefix + "A, ");
            System.out.print(prefix + "C, ");
            System.out.print(prefix + "G, ");
            System.out.print(prefix + "U, ");
        }
        if (length > 1) {
            alphOrderStrandsFixedLength(length - 1, prefix + "A");
            alphOrderStrandsFixedLength(length - 1, prefix + "C");
            alphOrderStrandsFixedLength(length - 1, prefix + "G");
            alphOrderStrandsFixedLength(length - 1, prefix + "U");
        }
    }

    // Prints all RNA strands of length up to and including bound, in length-lexicographic order
    public static void alphOrderStrands(int bound) {
        for (int i=1; i <= bound; i++) {
            alphOrderStrandsFixedLength(i, "");
        }
    }

    // Returns the (natural number) index of RNA strand s based on the length-lexicographic order
    public static int integerInverse(String s) {
        int firstLengthS = 0;
        int lengthS = s.length();
        for (int i = 1; i < lengthS; i++) {
            firstLengthS += Math.pow(4,i);
        }
        //System.out.println("The index of the first length " + s.length() + " strand is " + firstLengthS);
        int index = firstLengthS;
        for (int i = 0; i < lengthS; i++) {
            switch(s.charAt(i)) {
                case 'A': index += 0*Math.pow(4,lengthS - i - 1); break;
                case 'C': index += 1*Math.pow(4,lengthS - i - 1); break;
                case 'G': index += 2*Math.pow(4,lengthS - i - 1); break;
                case 'U': index += 3*Math.pow(4,lengthS - i - 1); break;
            }
            //System.out.println("The " + i + "th character is " + s.charAt(i) + " and have updated index to " + index);
        }
        return index;
     }

     //Method implementing one-to-one function from set of positive integers to set of RNA strands
     public static String nextStrand(int n) {
         if (n == 1) {
             return "A";
         }
         else {
             return "A" + nextStrand(n-1);
         }
     }

    public static void main (String[] args) {
        System.out.println("Printing outputs of one-to-one function from set of positive integers to set of RNA strands");
        for (int i=1; i<=20; i++){
            System.out.print(nextStrand(i)+", ");
        }
        System.out.println();

        System.out.println("Printing RNA strands up to length 1 in alphabetical order");
        RNAStrand.alphOrderStrands(1);
        System.out.println();
        System.out.println("Printing RNA strands up to length 2 in alphabetical order");
        RNAStrand.alphOrderStrands(2);
        System.out.println();

        System.out.println("The natural number index of the RNA strand A is " + RNAStrand.integerInverse("A"));
        System.out.println("The natural number index of the RNA strand CC is " + RNAStrand.integerInverse("CC"));
        System.out.println("The natural number index of the RNA strand UG is " + RNAStrand.integerInverse("UG"));
    }
}