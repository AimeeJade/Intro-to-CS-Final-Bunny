/**
 * Maze.java
 * A class for loading and printing mazes from files.
 *
 * @author ANIKA RAJBHANDARY and AIMEE YUAN
 */
import java.util.Scanner;
import java.util.ArrayList;
import java.io.FileNotFoundException;
import java.io.File;

public class Maze {
    private ArrayList<ArrayList<MazeSquare>> rowList;
    private int w;
    private int h;
    private int start_x;
    private int start_y;

    // OTHER INSTANCE VARIABLES IF YOU NEED THEM
    
    
    //Constructor for the Maze class
    public Maze() {
        rowList = new ArrayList<ArrayList<MazeSquare>>();
    }
    
    //Load in a Maze from a given file
    String fileName = "maze.txt";
    public void load(String fileName) {
        // Create a scanner for the given file
        Scanner scanner = null;
        try {
            scanner = new Scanner(new File(fileName));
        } catch (FileNotFoundException e) {
            System.err.println(e);
            System.exit(1);
        }

        // First line of file is "w h"
        String[] lineParams = scanner.nextLine().split(" ");
        w = Integer.parseInt(lineParams[0]);
        h = Integer.parseInt(lineParams[1]);
        
        // YOUR CODE TO FINISH LOADING FILE HERE
        String[] startBlock = scanner.nextLine().split(" ");
        start_x = Integer.parseInt(startBlock[0]);
        start_y = Integer.parseInt(startBlock[1]);
    }

    /**
     * Print the Maze to System.out
     */
    public void print() {
        // YOUR CODE HERE
    }

    // MORE METHODS AS YOU NEED THEM

public int calc_size(){
    return w * h;
}


    // This main program acts as a simple unit test for the
    // load-from-file and print-to-System.out Maze capabilities.
    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: java Maze mazeFile");
            System.exit(1);
        }

        Maze maze = new Maze();
        maze.load(args[0]);
        maze.print();
    }
}
