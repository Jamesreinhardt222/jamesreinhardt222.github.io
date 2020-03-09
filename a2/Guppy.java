package ca.bcit.comp2522.assignments.a2;

import java.util.ArrayList;
import java.util.Random;

/**
 * Guppy.
 *
 * @author James
 * @version 2020
 */
public class Guppy {
    /**
     * The age at which a fry becomes a young Guppy.
     */
    public static final int YOUNG_FISH_AGE_IN_WEEKS = 10;

    /**
     * The age at which a young Guppy becomes a mature Guppy.
     */
    public static final int MATURE_FISH_AGE_IN_WEEKS = 30;

    /**
     * The maximum age in weeks.
     */
    public static final int MAXIMUM_AGE_IN_WEEKS = 50;

    /**
     * Minimum volume mL to support a Guppy.
     */
    public static final double MINIMUM_WATER_VOLUME_ML = 250.0;

    /**
     * Default genus of Guppy.
     */
    public static final String DEFAULT_GENUS = "Poecilia";

    /**
     * Default species of Guppy.
     */
    public static final String DEFAULT_SPECIES = "reticulata";

    /**
     * Default health coefficient.
     */
    public static final double DEFAULT_HEALTH_COEFFICIENT = 0.5;

    /**
     * Minimum health coefficient.
     */
    public static final double MINIMUM_HEALTH_COEFFICIENT = 0.0;

    /**
     * Maximum health coefficient.
     */
    public static final double MAXIMUM_HEALTH_COEFFICIENT = 1.0;

    // Tracks number of Guppies born during program lifetime.
    private static int numberOfGuppiesBorn = 0;

    private String genus;
    private String species;
    private int ageInWeeks;
    private boolean isFemale;
    private int generationNumber;
    private boolean isAlive;
    private double healthCoefficient;
    private int identificationNumber;

    /**
     * Zero-parameter constructor for objects of class Guppy.
     */
    public Guppy() {
        genus = DEFAULT_GENUS;
        species = DEFAULT_SPECIES;
        ageInWeeks = 0;
        isFemale = true;
        generationNumber = 0;
        isAlive = true;
        healthCoefficient = DEFAULT_HEALTH_COEFFICIENT;
        identificationNumber = ++numberOfGuppiesBorn;
    }

    /**
     * Multi-parameter constructor for objects of class Guppy. Invalid arguments
     * will generate IllegalArgumentExceptions.
     *
     * @param newGenus             cannot be null, empty, or a String of whitespace
     * @param newSpecies           cannot be null, empty, or a String of whitespace
     * @param newAgeInWeeks        must be between 0 and MAXIMUM_AGE_IN_WEEKS
     * @param newIsFemale          true if female, else false
     * @param newGenerationNumber  must be positive
     * @param newHealthCoefficient must be between MINIMUM_HEALTH_COEFFICIENT or
     *                             MAXIMUM_HEALTH_COEFFICIENT
     * @throws IllegalArgumentException if newGenus is invalid
     * @throws IllegalArgumentException if newSpecies is invalid
     */
    public Guppy(final String newGenus,
                 final String newSpecies,
                 int newAgeInWeeks,
                 boolean newIsFemale,
                 int newGenerationNumber,
                 double newHealthCoefficient) throws IllegalArgumentException {
        if (newGenus != null && newGenus.trim().length() > 0) {
            genus = formatNameTitleCase(newGenus.trim());
        } else {
            throw new IllegalArgumentException("Genus cannot be empty!");
        }

        if (newSpecies != null && newSpecies.trim().length() > 0) {
            species = newSpecies.trim().toLowerCase();
        } else {
            throw new IllegalArgumentException("Species cannot be empty!");
        }

        if (newAgeInWeeks < 0 || newAgeInWeeks >= MAXIMUM_AGE_IN_WEEKS) {
            throw new IllegalArgumentException("Age must be between 0 and 49 inclusive!");
        } else {
            ageInWeeks = newAgeInWeeks;
        }

        isFemale = newIsFemale;

        if (newGenerationNumber < 0) {
            throw new IllegalArgumentException("Generation must be positive!");
        } else {
            generationNumber = newGenerationNumber;
        }

        if (newHealthCoefficient < MINIMUM_HEALTH_COEFFICIENT
                || newHealthCoefficient > MAXIMUM_HEALTH_COEFFICIENT) {
            throw new IllegalArgumentException("Health coefficient must be in range [0,1.0]!");
        } else {
            healthCoefficient = newHealthCoefficient;
        }

        isAlive = true;
        identificationNumber = ++numberOfGuppiesBorn;
    }

    /**
     * Increments the age of the Guppy by 1 week. If after incrementing the age
     * getAge() > MAXIMUM_AGE_IN_WEEKS then isAlive() = false.
     */
    public void incrementAge() {
        if (isAlive) {
            ++ageInWeeks;
        }
        if (getAgeInWeeks() > MAXIMUM_AGE_IN_WEEKS) {
            setIsAlive(false);
        }
    }

    /**
     * Returns genus.
     *
     * @return genus as a String
     */
    public String getGenus() {
        return genus;
    }

    /**
     * Returns species.
     *
     * @return species as a String
     */
    public String getSpecies() {
        return species;
    }

    /**
     * Returns age in weeks.
     *
     * @return ageInWeeks as an int
     */
    public int getAgeInWeeks() {
        return ageInWeeks;
    }

    /**
     * Returns true if the Guppy is female, else false.
     *
     * @return isFemale as a boolean
     */
    public boolean getIsFemale() {
        return isFemale;
    }

    /**
     * Returns generation number.
     *
     * @return generationNumber as an int
     */
    public int getGenerationNumber() {
        return generationNumber;
    }

    /**
     * Returns true if the Guppy is alive, else false.
     *
     * @return isAlive as a boolean
     */
    public boolean getIsAlive() {
        return isAlive;
    }

    /**
     * Returns the health coefficient. A health coefficient of 0 means the Guppy
     * is dead. A health coefficient of 1.0 means the Guppy is in perfect
     * health.
     *
     * @return healthCoefficient as a double
     */
    public double getHealthCoefficient() {
        return healthCoefficient;
    }

    /**
     * Returns the identification number.
     *
     * @return identificationNumber as an int
     */
    public int getIdentificationNumber() {
        return identificationNumber;
    }

    /**
     * Returns the number of Guppy objects created.
     *
     * @return numberOfGuppiesBorn as an int
     */
    public static int getNumberOfGuppiesBorn() {
        return numberOfGuppiesBorn;
    }

    /**
     * Sets the age in weeks. Ignores values < 0 and > MAXIMUM_AGE_IN_WEEKS.
     *
     * @param newAgeInWeeks an int
     */
    public void setAgeInWeeks(int newAgeInWeeks) {
        if (newAgeInWeeks >= 0 && newAgeInWeeks <= MAXIMUM_AGE_IN_WEEKS) {
            ageInWeeks = newAgeInWeeks;
        }
    }

    /**
     * Sets whether the Guppy is alive.
     *
     * @param newIsAlive true if alive, else false
     */
    public void setIsAlive(boolean newIsAlive) {
        isAlive = newIsAlive;
    }

    /**
     * Sets the health coefficient. Ignores values < MINIMUM_HEALTH_COEFFICIENT
     * and ignores values > MAXIMUM_HEALTH_COEFFICIENT.
     *
     * @param newHealthCoefficient a double
     */
    public void setHealthCoefficient(double newHealthCoefficient) {
        if (newHealthCoefficient >= MINIMUM_HEALTH_COEFFICIENT
                && newHealthCoefficient <= MAXIMUM_HEALTH_COEFFICIENT) {
            healthCoefficient = newHealthCoefficient;
        }
    }

    /**
     * Returns the volume of water needed by this Guppy in millilitres.
     *
     * @return volume in mL
     */
    public double getVolumeNeeded() {
        if (getAgeInWeeks() < YOUNG_FISH_AGE_IN_WEEKS) {
            return MINIMUM_WATER_VOLUME_ML;
        } else if (getAgeInWeeks() <= MATURE_FISH_AGE_IN_WEEKS) {
            return MINIMUM_WATER_VOLUME_ML * getAgeInWeeks() / YOUNG_FISH_AGE_IN_WEEKS;
        } else if (getAgeInWeeks() <= MAXIMUM_AGE_IN_WEEKS) {
            final double matureFishMultiplier = 1.5;
            return MINIMUM_WATER_VOLUME_ML * matureFishMultiplier;
        } else {
            return 0;
        }
    }

    /**
     * Changes the health coefficient by the specified delta. If the new health
     * coefficient < MINIMUM_HEALTH_COEFFICIENT, the fish dies. The health
     * coefficient cannot exceed the bounds [0.0, 1.0]
     *
     * @param delta a double
     */
    public void changeHealthCoefficient(double delta) {
        double newHealthCoefficient = healthCoefficient + delta;
        if (newHealthCoefficient <= MINIMUM_HEALTH_COEFFICIENT) {
            setHealthCoefficient(MINIMUM_HEALTH_COEFFICIENT);
            setIsAlive(false);
        } else if (newHealthCoefficient > MAXIMUM_HEALTH_COEFFICIENT) {
            setHealthCoefficient(MAXIMUM_HEALTH_COEFFICIENT);
        } else {
            setHealthCoefficient(newHealthCoefficient);
        }
    }

    /**
     * Formats a name and returns it with the first letter in upper case and the
     * rest in lower case. If passed null, returns a null.
     *
     * @param name the name to format
     * @return the correctly formatted name, as a String
     */
    public static String formatNameTitleCase(String name) {
        if (name != null && name.trim().length() > 0) {
            String firstLetter = name.trim().toUpperCase().substring(0, 1);
            String theRest = name.trim().toLowerCase().substring(1);
            return firstLetter + theRest;
        } else {
            return null;
        }
    }

    /**
     * Creates an array of baby guppies, simulating a single female guppy spawning.
     *
     * Will only create baby guppies if the original guppy is female and over eight weeks old.
     * @return an array of guppies.
     */
    public ArrayList<Guppy> spawn() {
        final int reproductiveAge = 8;
        final double fiftyPercent = 0.50;
        final int maxNumberOfBabies = 100;
        Random random = new Random();
        if (ageInWeeks < reproductiveAge || !isFemale) {
            return null;
        }
        ArrayList<Guppy> babyGuppies = new ArrayList<>();
        double chanceOfSpawning = random.nextDouble();
        if (chanceOfSpawning < fiftyPercent) {
            int numberOfBabies = random.nextInt(maxNumberOfBabies + 1);
            for (int i = 0; i < numberOfBabies; i++) {
                Guppy guppy = new Guppy();
                babyGuppies.add(guppy);
            }
        }
        return babyGuppies;
    }

    /**
     * Returns a String representation of this Guppy.
     *
     * @return toString a String representation.
     */
    @Override
    public String toString() {
        return "Guppy{"
                + "genus='" + genus + '\''
                + ", species='" + species + '\''
                + ", ageInWeeks=" + ageInWeeks
                + ", isFemale=" + isFemale
                + ", generationNumber=" + generationNumber
                + ", isAlive=" + isAlive
                + ", healthCoefficient=" + healthCoefficient
                + ", identificationNumber=" + identificationNumber
                + '}';
    }

    /**
     * Compares the specified object to this Guppy.
     *
     * @param other the other object
     * @return true if this equals o, else false.
     */
    @Override
    public boolean equals(Object other) {
        if (this == other) {
            return true;
        }
        if (other == null || getClass() != other.getClass()) {
            return false;
        }

        Guppy guppy = (Guppy) other;

        if (ageInWeeks != guppy.ageInWeeks) {
            return false;
        }
        if (isFemale != guppy.isFemale) {
            return false;
        }
        if (generationNumber != guppy.generationNumber) {
            return false;
        }
        if (isAlive != guppy.isAlive) {
            return false;
        }
        if (Double.compare(guppy.healthCoefficient, healthCoefficient) != 0) {
            return false;
        }
        if (identificationNumber != guppy.identificationNumber) {
            return false;
        }
        if (!genus.equals(guppy.genus)) {
            return false;
        }
        return species.equals(guppy.species);
    }

    /**
     * Returns a hashcode.
     *
     * @return int representing the state of this Guppy.
     */
    @Override
    public int hashCode() {
        int result;
        long temp;
        final int prime = 31;
        result = genus.hashCode();
        result = prime * result + species.hashCode();
        result = prime * result + ageInWeeks;
        result = prime * result + (isFemale ? 1 : 0);
        result = prime * result + generationNumber;
        result = prime * result + (isAlive ? 1 : 0);
        temp = Double.doubleToLongBits(healthCoefficient);
        final int shift = 32;
        result = prime * result + (int) (temp ^ (temp >>> shift));
        result = prime * result + identificationNumber;
        return result;
    }

}
