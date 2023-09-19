//Welcome App, Homework 2 for Data Structures
//@author Aimee Yuan

import java.util.Scanner;
import java.lang.StringBuilder;
import java.util.StringJoiner;


public class Welcome {
    public static void main(String[] args){
        System.out.println("Welcome to CS 201: Data Structures");
        
        //asking for user's name
        System.out.println("What is your name?");
        Scanner scan = new Scanner(System.in);
        String username = scan.nextLine();
        
        //asking for an integer
        System.out.println("Please enter an integer");
        int number = scan.nextInt();
        int x = Integer.signum(number);
        System.out.println(x);

        //Printing user's name
        System.out.println("Welcome " + username);

        //Printing name backwards using a for loop over the length of the name
        int lengthOfUsername = username.length();

        StringBuilder nameBackwards = new StringBuilder();
        for (int i = 1; i <= lengthOfUsername; i++){
            nameBackwards.append(username.charAt(lengthOfUsername - i));
        }

        System.out.println("Your name backwards is " + nameBackwards);
        
        //Printing out a triangle from the integer
/**
        for (int j = 1; j <= number; j++){
            for (int k = 1; k <= j; k++){
                if (k < j){
                    System.out.print(j + ", ");
            }
            else {
                System.out.println(j);
            }
        }
    }*/
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
}
