//Welcome App, Homework 2 for Data Structures 201
//@author Aimee Yuan

import java.util.Scanner;
import java.lang.StringBuilder;
import java.util.StringJoiner;


public class Welcome {
    public static void main(String[] args){
        System.out.println("Welcome to CS 201: Data Structures!");
        
        //asking for a name
        System.out.println("What is your name?");
        Scanner scan = new Scanner(System.in);
        String username = scan.nextLine();
        
        //asking for an integer
        System.out.println("Please enter an integer");
        try {
            int number = scan.nextInt();
            int numValue = Integer.signum(number); //checking if the integer inputted is postive, negative, or 0

            //Printing user's name
            System.out.println("Welcome " + username);

            //Printing name backwards using a for loop over the length of the name
            int lengthOfUsername = username.length();

            StringBuilder nameBackwards = new StringBuilder();
            for (int i = 1; i <= lengthOfUsername; i++){
                nameBackwards.append(username.charAt(lengthOfUsername - i));
            }

            System.out.println("Your name backwards is " + nameBackwards);
        
            //Printing out a triangle made of integers
            if (numValue == 1){ //If the integer the user inputted is positive
                for (int j = 1; j <= number; j++){
                    for (int k = 1; k <= j; k++){
                        if (k < j){
                            System.out.print(j + ", ");
                    }
                    else {
                        System.out.println(j);
                    }
                }
            }

            }

            if (numValue == -1){ //If the integer the user inputted was negative
                for (int j = -1; j >= number; j--){
                    for (int k = -1; k >= j; k--){
                        if (k > j){
                            System.out.print(j + ", ");
                    }
                    else {
                        System.out.println(j);
                    }
                }
        }

            }
            if (numValue == 0){ //If the integer inputted was 0
                System.out.println("Cannot print a triangle of height 0");
            }
            }
            catch(Exception e) {
                System.out.println("You must enter an integer");
            }

    } 
}
