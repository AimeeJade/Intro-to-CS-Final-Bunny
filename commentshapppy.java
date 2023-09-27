/**
 * Maze.java
 * A class for loading and printing mazes from files.
 *
 * @author ANIKA RAJBHANDARY and AIMEE YUAN
 */
import java.util.*;
import java.io.*;

public class Maze {
    private ArrayList<ArrayList<MazeSquare>> rowList;
    private int w;
    private int h;
    private int startColumn;
    private int startRow;
    private int finishColumn;
    private int finishRow;
    
    /**
     * Constructor for the Maze class
     */
    public Maze() {
        rowList = new ArrayList<ArrayList<MazeSquare>>();
    }

    public void makeEmptyGrid(int h){

        //making an EmptyGrid with number of columns equal to h and number of rows equal to w
        int r = 0;
        while(r<h){
            r += 1;
            
            ArrayList<MazeSquare> row = new ArrayList<MazeSquare>();
            for(int c= 0; c<=h; c += 1){
                row.add( new MazeSquare() );
            }

            rowList.add(row);
        }
        System.out.print("\n"+rowList+"\n");

    }

     // This returns the MazeSquare in position row, col of our grid
     public String getData(int row, int col){
        MazeSquare temp = rowList.get(row).get(col);
        return temp.getData();
    }

    // This changes the MazeSquare in position row, col of our grid
    public void setData(int row, int col, String s){
        MazeSquare temp = rowList.get(row).get(col);
        temp.setData(s);
    }

    //scanning the maze.txt based on the command line and parsing the integers
    public void load(String fileName) {
        // Create a scanner for the given file
        //System.out.print("hello");
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

        // First we read in the size and create an empty grid
        makeEmptyGrid(h);

        lineParams = scanner.nextLine().split(" ");

        startColumn = Integer.parseInt(lineParams[0]);
        startRow = Integer.parseInt(lineParams[1]);
        
        lineParams = scanner.nextLine().split(" ");

        finishColumn = Integer.parseInt(lineParams[0]);
        finishRow = Integer.parseInt(lineParams[1]);

        //scanning symbols for maze structure
        for(int row = 0; row < h; row += 1){
            lineParams = scanner.nextLine().split("");

            for(int col=0; col < w; col += 1){
                setData(row, col, lineParams[col]);
            }
        }
        
   
    }


    //Print the Maze to System.out
    public void print(){
        // for each column, print out top wall
        for (int loop = 0; loop <= h; loop++){
            System.out.print("+-----");
        }
        // print final + in top wall
        System.out.print("+");

        // for each row in grid of maze squares
        for(int row = 0; row < h; row += 1){
            //print new line for each row
            System.out.print("\n");
            int x = 0;

            // iterating over all 4 lines of each maze square
            while (x<= 3){
                //iterating over first three lines of each maze square 
                if (x<=2){
                    //iterating over each column in given row
                    for(int col =0; col < w; col +=1){
                        //Creater "joiner" and add strings line by line between maze squares in a row together
                        StringJoiner joiner = new StringJoiner("");
                        //depending on symbol imput, print out different Strings
                        if (getData(row, col).equals("L")){
                            //If the column and row corresponds to the given start coordinates, print S on the second line
                            if (col == startColumn && row == startRow && x == 1){
                                joiner.add("|  S  ");
                                //If the maze square is on the last column, add a "|" to build a right wall
                                if (col ==h){
                                    joiner.add("|");
                                }
                            }
                            //If the column and row corresponds to the given finish coordinates, print F on the second line
                            else if (col == finishColumn && row == finishRow && x == 1){
                                joiner.add("|  F  ");
                                if (col ==h){
                                    joiner.add("|");
                                }
                            }
                            else{
                                joiner.add("|     ");
                                if (col == h)
                                {
                                    joiner.add("|");
                                }
                            }

                        }
                        if (getData(row, col).equals("_")){
                            if (col == startColumn && row == startRow && x == 1){
                                joiner.add("|  S  ");
                                if (col ==h){
                                    joiner.add("|");
                                }
                            }
                            else if (col == finishColumn && row == finishRow && x == 1){
                                joiner.add("   F  ");
                                if (col ==h){
                                    joiner.add("|");
                                }
                            }
                            else{
                            joiner.add("      ");
                            if (col == h)
                            {
                                joiner.add("|");
                            }
                        }
                    }
                        if (getData(row, col).equals("-")){
                            if (col == startColumn && row == startRow && x == 1){
                                joiner.add("|  S  ");
                                if (col ==h){
                                    joiner.add("|");
                                }
                            }
                            else if (col == finishColumn && row == finishRow && x == 1){
                                joiner.add("   F  ");
                                if (col ==h){
                                    joiner.add("|");
                                }
                            }
                            else{
                            joiner.add("      ");
                            if (col == h)
                            {
                                joiner.add("|");
                            }
                        }
                    }
                        if (getData(row, col).equals("|")){
                            if (col == startColumn && row == startRow && x == 1){
                                joiner.add("|  S  ");
                                if (col ==h){
                                    joiner.add("|");
                                }
                            }
                            else if (col == finishColumn && row == finishRow && x == 1){
                                joiner.add("|  F  ");
                                if (col ==h){
                                    joiner.add("|");
                                }
                            }
                            else{
                            joiner.add("|     ");
                            if (col == h)
                            {
                                joiner.add("|");
                            }
                        }
                    }
                        //print out string joiner for each line in series of maze squares in given row
                        System.out.print(joiner.toString() );
                   
                    }

                x++;
                System.out.print("\n");
                }
                
                //On the 4th line of the maze squares in a row, add/don't add a bottom wall depending on symbol input from maze.txt file
                else if (x == 3){
                    for(int col =0; col < w; col +=1){
                        StringJoiner joiner2 = new StringJoiner("");
                        if (getData(row, col).equals("L")){
                            joiner2.add("+-----");
                            if (col == h)
                            {
                                joiner2.add("+");
                            }
                        }
                        if (getData(row, col).equals("_")){
                            joiner2.add("+-----");
                            if (col == h)
                            {
                                joiner2.add("+");
                            }
                        }
                        if (getData(row, col).equals("-")){
                            joiner2.add("+     ");
                            if (col == h)
                            {
                                joiner2.add("+");
                            }
                        }
                        if (getData(row, col).equals("|")){
                            joiner2.add("+     ");
                            if (col == h)
                            {
                                joiner2.add("+");
                            }
                        }
                    System.out.print(joiner2.toString() );
                }
                x++;
            }
            }
    }
    }

    //main function which takes in command line arguments that contain file name
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
