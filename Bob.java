import java.util.*;
import java.io.*;

public class Bob {
    //int w;
    //int y;
    public static void main(String[] args) {

        if (args.length == 0) {
             System.err.println("Usage: java CommandLine inputFilePath");
             System.exit(1);
         }
        String inputFilePath = args[0];

        File inputFile = new File(inputFilePath);

    Scanner scanner = null;
    try {
        scanner = new Scanner(new File(inputFilePath));
        //String[] lineParams = scanner.nextLine().split(" ");
        //w = Integer.parseInt(lineParams[0]);
        //h = Integer.parseInt(lineParams[1]);
        //System.out.println(w);
        String bb = scanner.nextLine();
        System.out.print(bb);

    } catch (FileNotFoundException e) {
        System.err.println(e);
        System.exit(1);
    }

        // First line of file is "w h"
    //String[] lineParams = scanner.nextLine().split(" ");
    //w = Integer.parseInt(lineParams[0]);
    //h = Integer.parseInt(lineParams[1]);
    //System.out.println(w);
    //System.out.println(h);

    scanner.close();
    
}
}

//public static void main(String [] args){
        //System.out.print("|" + "\n" + "|" + "\n" + "|" + "\n" + "+" + "-----" + "+");
    //}
