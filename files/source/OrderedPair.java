public class OrderedPair {
  int first;
  int second;

  public OrderedPair (int firstArg, int secondArg) {
    first =  firstArg;
    second = secondArg;
  }

  public String toString() {
    return "("+first+", "+second+")";
  }

  public long toNum() {
    return Math.round(Math.pow(2,this.first)*Math.pow(3,this.second));
  }

  public static String test(int firstArg, int secondArg) {
    OrderedPair testPair = new OrderedPair(firstArg,secondArg);
    return ("Number for "+testPair.toString()+": "+testPair.toNum());
  }

  public static void main (String[] args) {
    System.out.println("Printing pairs...");
    for (int i = 1; i < 5; i++) {
      for (int j = 1;  j < 5; j++) {
        System.out.println(test(i,j));
      }
    }

  }
}
