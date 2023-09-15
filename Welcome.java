//Aimee Yuan, Welcome App

import java.util.Scanner;
import java.lang.StringBuilder;

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

        //Printing name backwards

        //need to split the string into characters and append these characters into an array?????

        //finding the length of the username for a for loop
        int lengthOfUsername = username.length();
        System.out.println(lengthOfUsername);
        /**StringBuilder charUsername = new StringBuilder();
        for (int i = 0; i <= lengthOfUsername; i++){
            charUsername.append(username.charAt(i));
        }
        */
        for (int i = 0; i < lengthOfUsername; i++){
            System.out.println(username.charAt(i));
            insert(int 0, charAt(i));
        }

        
        //System.out.println(istilldk);
        //StringBuilder nameBackwards = username.reverse(); //only for character sequence
        //System.out.println("Your name backwards is" + nameBackwards);

    } 
}
