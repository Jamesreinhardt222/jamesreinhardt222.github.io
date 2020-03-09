package ca.bcit.comp2522.assignments.a2;

import java.util.ArrayList;
import java.util.Objects;
import java.util.Random;

/**
 * Ecosystem.
 *
 * @author James
 * @version 2020
 */
public class Ecosystem {
    /*
    A collection of the pool objects in this instance of an Ecosystem.
     */
    private ArrayList<Pool> pools;

    /**
     * Zero-parameter for objects of this class.
     */
    public Ecosystem() {
        pools = new ArrayList<>();
    }

    /**
     * Adds a new pool to the pool array for this class.
     *
     * @param newPool a Pool object.
     */
    public void addPool(final Pool newPool) {
        if (newPool != null) {
            pools.add(newPool);
        }
    }

    /**
     * Removes all the pools from this ecosystem.
     */
    public void reset() {
        pools.clear();
    }

    /**
     * Returns the population of guppies in this ecosystem.
     *
     * @return an int.
     */
    public int getGuppyPopulation() {
        int guppyPopulation = 0;
        for (Pool guppyPool : pools) {
            guppyPopulation += guppyPool.getPopulation();
        }
        return guppyPopulation;
    }

    /**
     * Calls the adjust for overcrowding method on each pool in this ecosystem.
     *
     * Adjusts the number of guppies in each pool in the ecosystem to prevent overcrowding.
     * @return the number of guppies that died from overcrowding as an integer.
     */
    public int adjustForCrowding() {
        int totalNumberOfGuppiesCrowdedOut = 0;
        for (Pool poolsInEcosystem : pools) {
            totalNumberOfGuppiesCrowdedOut += poolsInEcosystem.adjustForCrowding();
        }
        return totalNumberOfGuppiesCrowdedOut;
    }

    /**
     * Creates guppies to populate each pool.
     * 
     * @param numberOfNewGuppies the number of new guppies being born into the pool as an int.
     * @param ageTopRange the range of ages as an int.
     * @param ageShift the youngest possible guppy as an int.
     * @param healthCoefficientRange the difference between the maximum and minumum
     * allowable health coefficients as a double.
     * @param healthCoefficientShift The minimum allowable health coefficient as a double.
     * @param femaleLikelihood the chance of a guppy being female out of a hundred as an integer.
     * @param pool the pool that the guppies are being added to as a Pool object.
     */
    private void guppyLoop(int numberOfNewGuppies, int ageTopRange, int ageShift,
                          double healthCoefficientRange, double healthCoefficientShift,
                          int femaleLikelihood, Pool pool) {
        final int percentageLimit = 100;
        for (int i = 0; i < numberOfNewGuppies; i++) {
            Random random = new Random();
            String genus = "Poecilia";
            String species = "reticulata";
            int age = random.nextInt(ageTopRange) + ageShift;
            double healthCoefficient = random.nextDouble() * healthCoefficientRange
                    + healthCoefficientShift;
            int isGuppyFemale = random.nextInt(percentageLimit);
            int generationNumber = 0;
            boolean isfemale = isGuppyFemale <= femaleLikelihood;
            Guppy guppy = new Guppy(genus, species, age, isfemale,
                    generationNumber, healthCoefficient);
            pool.addGuppy(guppy);
        }
    }

    /**
     * Adds guppies to each pool in the simulation.
     *
     * @param firstPool a Pool
     * @param secondPool a Pool
     * @param thirdPool a Pool
     */
    private void addGuppies(Pool firstPool, Pool secondPool, Pool thirdPool) {
        final int firstPoolNewNumberOfGuppies = 300;
        final int firstPoolAgeRange = 15;
        final int firstPoolMinimumAge = 10;
        final double firstPoolHealthCoefficientRange = 0.3;
        final double firstPoolminimumHealthCoefficient = 0.5;
        final int firstPoolFemaleLikelihood = 75;

        final int secondPoolNewNumberOfGuppies = 100;
        final int secondPoolAgeRange = 5;
        final int secondPoolMinimumAge = 10;
        final double secondPoolHealthCoefficientRange = 0.2;
        final double secondPoolminimumHealthCoefficient = 0.8;
        final int secondPoolFemaleLikelihood = 75;

        final int thirdPoolNewNumberOfGuppies = 200;
        final int thirdPoolAgeRange = 34;
        final int thirdPoolMinimumAge = 15;
        final double thirdPoolHealthCoefficientRange = 1.0;
        final double thirdPoolminimumHealthCoefficient = 0;
        final int thirdPoolFemaleLikelihood = 35;

        guppyLoop(firstPoolNewNumberOfGuppies, firstPoolAgeRange, firstPoolMinimumAge,
                firstPoolHealthCoefficientRange, firstPoolminimumHealthCoefficient,
                firstPoolFemaleLikelihood, firstPool);
        guppyLoop(secondPoolNewNumberOfGuppies, secondPoolAgeRange, secondPoolMinimumAge,
                secondPoolHealthCoefficientRange, secondPoolminimumHealthCoefficient,
                secondPoolFemaleLikelihood, secondPool);
        guppyLoop(thirdPoolNewNumberOfGuppies, thirdPoolAgeRange, thirdPoolMinimumAge,
                thirdPoolHealthCoefficientRange, thirdPoolminimumHealthCoefficient,
                thirdPoolFemaleLikelihood, thirdPool);

    }

    /**
     * Sets up three pool objects for a simulation of this ecosystem.
     *
     * Calls on helper functions to specify the pool attributes and the range of
     * attributes for the guppies that populate them.
     * Creates three instances of the pool class.
     */
    private void setUpSimulation() {
        final int firstPoolVolume = 3000;
        final int firstPoolTemperature = 42;
        final double firstPoolPH = 7.9;
        final double firstPoolNutrientCoefficient = 0.9;

        final int secondPoolVolume = 15000;
        final int secondPoolTemperature = 39;
        final double secondPoolPH = 7.7;
        final double secondPoolNutrientCoefficient = 0.85;

        final int thirdPoolVolume = 4500;
        final int thirdPoolTemperature = 37;
        final double thirdPoolPH = 7.5;
        final double thirdPoolNutrientCoefficient = 1.0;
        Pool firstPool = new Pool("Skookumchuk", firstPoolVolume,
                firstPoolTemperature, firstPoolPH, firstPoolNutrientCoefficient);
        Pool secondPool = new Pool("Squamish", secondPoolVolume, secondPoolTemperature,
                secondPoolPH, secondPoolNutrientCoefficient);
        Pool thirdPool = new Pool("Semiahmoo", thirdPoolVolume, thirdPoolTemperature,
                thirdPoolPH, thirdPoolNutrientCoefficient);

        addGuppies(firstPool, secondPool, thirdPool);

        this.addPool(firstPool);
        this.addPool(secondPool);
        this.addPool(thirdPool);
    }

    /**
     * Run a simulation of a single week in this ecosystem.
     *
     * Will be called multiple times and the week number parameter
     * keeps track of which week this method is simulating.
     * This method goes through each pool and adjusts the guppy populations accordingly.
     * @param weekNumber the week number as an integer.
     */
    public void simulateOneWeek(final int weekNumber) {
        int dieOfOldAge = 0;
        int numberRemoved = 0;
        int starvedToDeath = 0;
        int newFry = 0;
        int crowdedOut = 0;
        for (Pool pool : pools) {
            dieOfOldAge += pool.incrementAges();
            numberRemoved += pool.removeDeadGuppies();
            starvedToDeath += pool.applyNutrientCoefficient();
            numberRemoved += pool.removeDeadGuppies();
            newFry += pool.spawn();
            crowdedOut += pool.adjustForCrowding();
            numberRemoved += pool.removeDeadGuppies();
            if (dieOfOldAge + starvedToDeath + crowdedOut != numberRemoved) {
                System.out.println("You have a logic error.\n");
            }
        }
            System.out.println("During week " + (weekNumber + 1)
                    + ", the following happened inside the " + pools.size()
                    + " pools in this ecosystem:\n" + dieOfOldAge + " guppies died of old age."
                    + "\n" + starvedToDeath + " guppies starved to death. "
                    + "\n" + crowdedOut +  " guppies were crowded out "
                    + "\n" + newFry + " new fry were born."
                    + "\nAll " + numberRemoved + " of the "
                    + "dead guppies were removed from the ecosystem.\n"
                    + "The remaining population in the ecosystem is "
                    + this.getGuppyPopulation() + " guppies.");
                    for (Pool pool: this.pools) {
                        System.out.println("Population of the " + pool.getName()
                                + "pool: " + pool.getPopulation());
                    }

    }

    /**
     * Simulates the ecosystem of various pools filled with guppies.
     *
     * @param numberOfWeeks The number of weeks the simulated as an integer.
     */
    public void simulate(final int numberOfWeeks) {
        this.setUpSimulation();
        for (int i = 0; i < numberOfWeeks; i++) {
            System.out.println("\n------------ Week " + (i + 1) + " ------------------\n");
            simulateOneWeek(i);
        }
    }

    /**
     * Returns a String representation of this ecosystem.
     *
     * @return toString a String representation.
     */
    @Override
    public String toString() {
        return "Ecosystem{" + "pools=" + pools + '}';
    }

    /**
     * Compares the specified object to this Ecosystem.
     *
     * @param other the other object
     * @return true if this equals other, else false.
     */
    @Override
    public boolean equals(Object other) {
        if (this == other) {
            return true;
        }
        if (!(other instanceof Ecosystem)) {
            return false;
        }

        if (other == null || getClass() != other.getClass()) {
            return false;
        }
        Ecosystem ecosystem = (Ecosystem) other;
        return this.pools == ecosystem.pools;
    }

    /**
     * Returns a hashcode.
     *
     * @return int representing the state of this ecosystem.
     */
    @Override
    public int hashCode() {
        return Objects.hash(pools);
    }
}
