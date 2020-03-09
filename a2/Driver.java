package ca.bcit.comp2522.assignments.a2;
import java.util.Scanner;

/**
 * Drives the program.
 *
 * @author james
 * @version 2020
 */
public class Driver {

    /**
     * Main method to test this module.
     *
     * @param args unused command line arguments.
     */
    public static void main(String[] args) {

        Ecosystem ecosystem = new Ecosystem();
        System.out.println("How many weeks do you want to simulate?");
        Scanner input = new Scanner(System.in);
        int numberOfWeeks = input.nextInt();

        ecosystem.simulate(numberOfWeeks);
    }

}
