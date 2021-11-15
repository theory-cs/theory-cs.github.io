public class CountablyInfinite {

  // Returns the ith positive integer, where i is a natural number
  public static int positives(int i) {
    return i + 1;
  }

  // Returns the ith negative integer, where i is a natural number
  public static int negatives(int i) {
    return -i - 1;
  }

  // Returns the ith integer, where i is a natural number
  // Note that this is also the function q from 7-warmup 
  // Domain: set of natural numbers; Codomain: set of integers
  public static int integers(int i) {
    if (i % 2 == 0) {
      return i/2;
    }
    else {
      return -(i+1)/2;
    }
  }

  // Returns the (natural number) index of integer x
  // Note that this is also the function f from 7-warmup 
  // Domain: set of integers; Codomain: set of natural numbers
  public static int integerInverse(int x) {
    if (x >= 0) {
      return 2*x;
    }
    else {
      return -2*x - 1;
    }
  }

  // Returns the ith odd integer, where i is a natural number
  public static int oddNaturals(int i) {
    return 2*i + 1;
  }

  // The function g from 7-warmup 
  // Domain: set of integers; Codomain: set of natural numbers
  public static int g(int n) {
    if (n < 0) {
      return -n;
    }
    else {
      return n;
    }
  }

  // The function h from 7-warmup 
  // Domain: set of natural numbers; Codomain: set of integers
  public static int h(int n) {
    if (n % 2 == 0) {
      return (-2*n) + 1;
    }
    else {
      return 2*n;
    }
  }

  public static void main (String[] args) {
    final int LIST_SIZE = 20;
    final int MAX_NATURAL = 6;
    final int MAX_INT_ABS = 3;
    System.out.println("First "+ LIST_SIZE+" steps in enumeration.");
    System.out.println("Natural numbers");
    for (int i = 0; i < LIST_SIZE; i++) {
      System.out.print(i+ " ");
    }
    System.out.println();

    System.out.println("Positive integers");
    for (int i = 0; i < LIST_SIZE; i++) {
      System.out.print(CountablyInfinite.positives(i)+ " ");
    }
    System.out.println();

    System.out.println("Negative integers");
    for (int i = 0; i < LIST_SIZE; i++) {
      System.out.print(CountablyInfinite.negatives(i)+ " ");
    }
    System.out.println();

    System.out.println("Integers");
    for (int i = 0; i < LIST_SIZE; i++) {
      System.out.print(CountablyInfinite.integers(i)+ " ");
    }
    System.out.println();

    System.out.println("Sample function applications for f");
    for (int i = -1*MAX_INT_ABS; i < MAX_INT_ABS; i++) {
      System.out.println("f(" + i + ") = " + integerInverse(i));
    }
    System.out.println();

    System.out.println("Sample function applications for g");
    for (int i = -1*MAX_INT_ABS; i < MAX_INT_ABS; i++) {
      System.out.println("g(" + i + ") = " + g(i));
    }
    System.out.println();

    System.out.println("Sample function applications for h");
    for (int i = 0; i < MAX_NATURAL; i++) {
      System.out.println("h(" + i + ") = " + h(i));
    }
    System.out.println();

    System.out.println("Sample function applications for q");
    for (int i = 0; i < MAX_NATURAL; i++) {
      System.out.println("q(" + i + ") = " + integers(i));
    }
    System.out.println();

    System.out.println("Odd natural numbers");
    for (int i = 0; i < LIST_SIZE; i++) {
      System.out.print(CountablyInfinite.oddNaturals(i)+ " ");
    }
    System.out.println();
  }
}
