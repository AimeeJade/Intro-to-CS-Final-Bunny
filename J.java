import java.io.*;
import java.util.*;

public class J {
    public static void main(String[] args){
        System.out.println("Give me an instruction please");
        Scanner scan = new Scanner(System.in);
        String inin = scan.nextLine();
        if (inin.equals("L")) {
            System.out.print("|" + "\n" + "|" + "\n" + "|" + "\n" + "+" + "-----" + "+");
        }
        else {
            System.out.println("idk");
        }
        scan.close();
    }
}
