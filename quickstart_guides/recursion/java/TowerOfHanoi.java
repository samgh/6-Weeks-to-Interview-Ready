/*
 *   Title: Towers of Hanoi
 *
 * Problem:
 *   Tower of Hanoi is a mathematical puzzle where we have three rods and n
 *   disks. The objective of the puzzle is to move the entire stack to another
 *   rod, obeying the following simple rules:
 *
 *   1) Only one disk can be moved at a time.
 *   2) Each move consists of taking the upper disk from one of the stacks and
 *      placing it on top of another stack i.e. a disk can only be moved if it
 *      is the uppermost disk on a stack.
 *   3) No disk may be placed on top of a smaller disk.
 *
 *   Execution: javac TowerOfHanoi.java && java TowerOfHanoi
 */
import java.util.Arrays;


public class TowerOfHanoi {
    public static void towerOfHanoi(int n, char from_rod, char to_rod, char aux_rod) {
        if (n == 1) {
            System.out.println("Move disk 1 from rod " +  from_rod + " to rod " + to_rod);
            return;
        }
        towerOfHanoi(n-1, from_rod, aux_rod, to_rod);
        System.out.println("Move disk " + n + " from rod " +  from_rod + " to rod " + to_rod);
        towerOfHanoi(n-1, aux_rod, to_rod, from_rod);
    }

    public static void main(String[] args) {
        int n = 4;
        towerOfHanoi(n, 'A', 'C', 'B');
    }

}
