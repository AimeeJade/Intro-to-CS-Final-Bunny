/**
 * Maze.java
 * A class for loading and printing mazes from files.
 *
 * @author YOUR NAME AND YOUR PARTNER'S NAME
 */
import java.util.*;
import java.io.*;


public class Maze {
    //private ArrayList<ArrayList<MazeSquare>> rowList;
    private int numRows;
    private int numColumns;
    private int s1;
    private int s2;
    private int f1;
    private int f2;
    // OTHER INSTANCE VARIABLES IF YOU NEED THEM
    
    /**
     * Constructor for the Maze class
     */
    //public Maze(){
        //rowList = new ArrayList<ArrayList<MazeSquare>>();
        //creating an array of dimension w and dimention
        // MazeSquare[w][h];

    //}

    /**public void makeEmptyGrid(int numRows, int numColumns){
        rowList = new ArrayList<ArrayList<MazeSquare>>();

        int w = 0;
        int h = 0;
        while (w <= numRows){
            ArrayList<MazeSquare> row = new ArrayList<MazeSquare>();
            for (h = 0; h < numColumns; h++){
                row.add(new MazeSquare());
            }
            rowList.add(row);
            w++;
        }
    
    public ___ getData(int row, int col){ //what does it return? it should be the instance/objects right?
        Maze temp = rowList.get(row).get(col);
        temp.getData(varName); //figure our what the variable is

    }

    public void setData(int row, int col, String square){
        Maze temp = rowList.get(row).get(col);
        temp.setData(square);
    }

    public void print(){
        int numRows = rowList.width();

        for(int row = 0; row < numRows; row ++){
            for (int col = 0; col < numColumns; col++) {
                System.out.print(getData(row, col));
            }
            System.out.println();
        }
    }
        

    }*/



    /**
     * Load in a Maze from a given file
     *
     * @param fileName the name of the file containing the maze
     */
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
        numRows = Integer.parseInt(lineParams[0]);
        numColumns = Integer.parseInt(lineParams[1]);
        //makeEmptyGrid(numRows, numColumns);
        
        lineParams = scanner.nextLine().split(" ");

        s1 = Integer.parseInt(lineParams[0]);
        s2 = Integer.parseInt(lineParams[1]);
        
        lineParams = scanner.nextLine().split(" ");

        f1 = Integer.parseInt(lineParams[0]);
        f2 = Integer.parseInt(lineParams[1]);

        ArrayList<ArrayList<String>> inputList = new ArrayList<>();
        for(int i = 1; i <= numColumns; i++){
            lineParams = scanner.nextLine().split("");
            ArrayList<String> strList = new ArrayList<String>(Arrays.asList(lineParams));
            inputList.add(strList);
        }

    }



    /**
     * Print the Maze to System.out
     */
    public void print() {
        
    }

    // This main program acts as a simple unit test for the
    // load-from-file and print-to-System.out Maze capabilities.

    public static void main(String[] args){
        Maze test_maze = new Maze();
        test_maze.load("maze.txt");
        System.out.print(inputList[0][0]);
        test_maze.print();
/** 
        for (int row = 0; row < numRows; row++) {
            for (int col = 0; col < numColumns, col ++) {
                Maze[row][column] = new MazeSquare()

            }
        }*/
        
    }
}

//create an array with the symbols
