/**
 * MazeSquare.java
 * A helper class for maze solving assignment.
 * Represents a single square within a rectangular maze.
 *
 * @author ANIKA RAJBHANDARY and AIMEE YUAN
 */
public class MazeSquare {
    String data;

    public String getData(){
        return data;
    }

    //This changes the maze square that is stored in the MazeSquare object
    public void setData( String x){
        //one symbol each from the file that represents a maze square
        if(x.length() != 1){
            System.out.println("Error in Letter setData method");
            System.out.println("Attempt to store more than one character");
            System.exit(1);
        }
        else{
            data = x;
        }
    }
    // constructor, set data equal to null by default before maze square object is stored
    public MazeSquare(){
        data = null;
    }
}
