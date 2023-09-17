/**
 * Loops.java
 * Jeff Ondich, 2014-01-05
 * Modified: Anna Rafferty, 2016-08-24
 * Modified: Sneha Narayan, Eric Alexander 2019-04-02
 * Modified: Anika Rajbhandary, Aimee Yuan 2023-09-17
 *
 * Demonstrates a few simple loops.
 *
 * Try a few things:
 * 1) Modify the while-loop so that it counts down from 10 to 0, printing the final 0.
 *
 * 2) Make a for-loop that counts out multiples of 3.
 *
 * 3) Explore what happens if you change the value of k or j within the corresponding for
 *    loop. How does this differ from the similar loop in Python? What happens if you try
 *    to access k inside of the loop about j? Explain in less than 3 sentences the rules for where you
 *    can access the different variables.
 * For loops in Java require three parameters in the paraentheses, with the instiantor, comparison variable, and the incrementer/decrementer. 
 * This comparison variable allows the for loop to be run until a condition is met, making similar to Python while loops.
 * Cannot access k inside of the loop about j because they are local variables and can only be accessed within their respective loops.
 * Local variables cannot be access outside of their block. 
 * This is the Java half of a pair of parallel examples in Python and Java.
 * See loops.py.
 */
import java.util.Scanner;
public class Loops {
    public static void main(String[] args) {
        System.out.println("Counting down with a while-loop");
        int m = 0;
        while (m <= 10) {
            System.out.println(10 - m);
            m++;
        }

        System.out.println("Counting up with a for-loop");
        for (int k = 0; k < 6; k++) {
            System.out.println(k);
        }
    

        System.out.println("Counting down with a for-loop");
        for (int j = 9; j > 0; j--) {
            System.out.println(j);
            //System.out.println(k); Error message
        }

        Scanner input = new Scanner(System.in);
        System.out.println("Please input a number to print that many multiples of 3");
        int inputNum = input.nextInt();
        System.out.println("Counting in multiples of 3");
        for (int t = 1; t <= inputNum; t++){
            System.out.println(3*t);
        }
    }
}
