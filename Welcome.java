//Aimee Yuan, Welcome App

import java.util.Scanner;
import java.lang.StringBuilder;
import java.util.StringJoiner;


public class Welcome {
    public static void main(String[] args){
        System.out.println("Welcome to CS 201: Data Structures");
        
        //asking for user's name
        System.out.println("What is your name?");
        Scanner idkfornow = new Scanner(System.in);
        String username = idkfornow.nextLine();
        
        //asking for an integer
        System.out.println("Please enter an integer");
        int number = idkfornow.nextInt();

        //Printing user's name
        System.out.println("Welcome " + username);

        //Printing name backwards using a for loop over the length of the name
        int lengthOfUsername = username.length();

        StringBuilder nameBackwards = new StringBuilder();
        for (int i = 1; i <= lengthOfUsername; i++){
            nameBackwards.append(username.charAt(lengthOfUsername - i));
        }

        System.out.println("Your name backwards is " + nameBackwards);
        
        //Triangle of numbers
        String delimiter = ", ";
        StringJoiner triangle = new StringJoiner(delimiter);
        for (int i = 1; i <= number; i++){
            triangle.add(i);
        }
        System.out.println(triangle);
        
        //if (number > 0) {
            //for (int i = 1; i <= number; i++){
                //System.out.println(i);
                //for (int n = 1; n <= number; n++){
                    //System.out.println(n);
                //}
            //}
        //}

    } 
}
