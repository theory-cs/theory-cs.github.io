public class List {
  int first;
  List tail;

  public List (int firstArg) {
    first =  firstArg;
    tail = null;
  }

  public List (int firstArg, List tailArg) {
    first =  firstArg;
    tail = tailArg;
  }

  public String toString() {
    if (tail == null) {
      return "("+first+",[])";
    }
    else {
      return "("+first+","+tail.toString()+")";
    }
  }

  public static long toNum(List list) {
    if (list == null) {
      return 0;
    }
    else {
      return Math.round(Math.pow(2,list.first)*Math.pow(3,toNum(list.tail)));
    }
  }

  public static String testDec(int length, int delta) {
    List[] lists = new List[length+1];
    lists[1] = new List(delta);
    for (int i = 2; i <= length; i ++) {
      lists[i] = new List(delta*i, lists[i-1]);
    }
    return ("Number for "+lists[length].toString()+": "+toNum(lists[length]));
  }

  public static String testInc(int length, int delta) {
    List[] lists = new List[length+1];
    int max = delta*(length+1);
    lists[1] = new List(max);
    for (int i = 2; i <= length; i ++) {
      lists[i] = new List(max - delta*i, lists[i-1]);
    }
    return ("Number for "+lists[length].toString()+": "+toNum(lists[length]));
  }

  public static void main (String[] args) {
    System.out.println("Printing lists...");
    for (int j = 0; j < 4; j++) {
      System.out.println(testDec(1,j));
    }
    for (int i = 2; i < 6; i++) {
      System.out.println(testDec(i,0));
      for (int j = 1;  j < 4; j++) {
        System.out.println(testInc(i,j));
        System.out.println(testDec(i,j));
      }
    }

  }
}
