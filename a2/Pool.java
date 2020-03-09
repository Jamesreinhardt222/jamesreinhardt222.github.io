package ca.bcit.comp2522.assignments.a2;

import java.util.Random;
import java.util.Collections;
import java.util.Objects;
import java.util.Iterator;
import java.util.ArrayList;
import java.util.Comparator;

/**
 * Pool.
 *
 * @author james
 * @version 2020
 */
public class Pool {
    /**
     * The name of the pool.
     */
    public static final String DEFAULT_POOL_NAME = " Unnamed";
    /**
     * The default pool temperature in degrees celsius.
     */
    public static final double DEFAULT_POOL_TEMP_CELSIUS = 40.0;
    /**
     * The minumum acceptable pool temperature in degrees celsius.
     */
    public static final double MINIMUM_POOL_TEMP_CELSIUS = 0.0;
    /**
     * The maximum acceptable pool temperature in degrees celsius.
     */
    public static final double MAXIMUM_POOL_TEMP_CELSIUS = 100.0;
    /**
     * The value of a neutral pH.
     */
    public static final double NEUTRAL_PH = 7.0;
    /**
     * The default nutrient coefficient for the pool.
     */
    public static final double DEFAULT_NUTRIENT_COEFFICIENT = 0.50;
    /**
     * The minimum possible nutrient coefficient for the pool.
     */
    public static final double MINIMUM_NUTRIENT_COEFFICIENT = 0.0;
    /**
     * The maximum possible nutrient coefficient for the pool.
     */
    public static final double MAXIMUM_NUTRIENT_COEFFICIENT = 1.0;

    private static int numberOfPools = 0;
    /*
    The name of the pool
     */
    private final String name;
    /*
    The volume of the pool in litres.
     */
    private double volumeLitres;
    /*
    The pool temperature in degrees celsius.
     */
    private double temperatureCelsius;
    /*
    The pool pH level on a 14-point scale.
     */
    private double pH;
    /*
    The nutrient coefficient for the pool between zero and one.
     */
    private double nutrientCoefficient;
    /*
   The unique id of the instance of the pool.
    */
    private final int identificationNumber;
    /*
    All the guppies in the pool.
     */
    private final ArrayList<Guppy> guppiesInPool;
    /*
    Random number generator for the pool.
     */
    private final Random randomNumberGenerator;
    /*
    Number of pools that have been created.
     */

    /**
     * Zero-parameter constructor for objects of class pool.
     */
    public Pool() {
        this.volumeLitres = 0.0;
        this.name = DEFAULT_POOL_NAME;
        this.temperatureCelsius = DEFAULT_POOL_TEMP_CELSIUS;
        this.pH = NEUTRAL_PH;
        this.nutrientCoefficient = DEFAULT_NUTRIENT_COEFFICIENT;
        this.guppiesInPool = new ArrayList<>();
        this.randomNumberGenerator = new Random();
        numberOfPools++;
        identificationNumber = numberOfPools;
    }

    /**
     * Multi-parameter constructor for objects of the pool class.
     * Invalid arguments will generate IllegalArgumentException.
     *
     * @param newVolumeLitres           must be greater than zero.
     * @param newName                   cannot be null, empty, or a string of whitespace.
     * @param newTemperatureCelsius     must be between MINIMUM_POOL_TEMP_CELSIUS and
     *                                  MAXIMUM_POOL_TEMP_CELSIUS
     * @param newPH                     must be between 0.0 and 14.0.
     * @param newNutrientCoefficient    must be between MINIMUM_NUTRIENT_COEFFICIENT and
     *                                  MAXIMUM_NUTRIENT_COEFFICIENT
     * @throws IllegalArgumentException if name is invalid.
     */
    public Pool(final String newName, final double newVolumeLitres,
                final double newTemperatureCelsius, final double newPH,
                final double newNutrientCoefficient) throws IllegalArgumentException {
        final double maxPH = 14.0;
        if (newName != null && newName.trim().length() > 0) {
            name = newName.trim().substring(0, 1).toUpperCase()
                    + newName.trim().substring(1).toLowerCase();
        } else {
            throw new IllegalArgumentException("Name cannot be empty!");
        }

        if (newVolumeLitres <= 0) {
            volumeLitres = 0;
        } else {
            volumeLitres = newVolumeLitres;
        }

        if (newTemperatureCelsius < MINIMUM_POOL_TEMP_CELSIUS
                || newTemperatureCelsius > MAXIMUM_POOL_TEMP_CELSIUS) {
            temperatureCelsius = DEFAULT_POOL_TEMP_CELSIUS;
        } else {
            temperatureCelsius = newTemperatureCelsius;
        }

        if (newPH < 0.0 || newPH > maxPH) {
            pH = NEUTRAL_PH;
        } else {
            pH = newPH;
        }

        if (newNutrientCoefficient < 0.0 || newNutrientCoefficient > 1.0) {
            nutrientCoefficient = DEFAULT_NUTRIENT_COEFFICIENT;
        } else {
            nutrientCoefficient = newNutrientCoefficient;
        }
        guppiesInPool = new ArrayList<>();
        randomNumberGenerator = new Random();
        numberOfPools++;
        identificationNumber = numberOfPools;
    }

    /**
     * Returns the name of this pool.
     *
     * @return name as a string.
     */
    public String getName() {
        return name;
    }

    /**
     * Returns the volume of the pool in litres.
     *
     * @return volumeLitres as a double.
     */
    public double getVolumeLitres() {
        return volumeLitres;
    }

    /**
     * Returns the temperature of the pool.
     *
     * @return temperatureCelsius as a double.
     */
    public double getTemperatureCelsius() {
        return temperatureCelsius;
    }

    /**
     * Returns the pH of the pool.
     *
     * @return the pH as a double.
     */
    public double getPH() {
        return pH;
    }

    /**
     * Returns the nutrient coefficient of the pool.
     *
     * @return te nutrient coefficient as a double.
     */
    public double getNutrientCoefficient() {
        return nutrientCoefficient;
    }

    /**
     * Returns the identification number for the pool.
     *
     * @return identificationNumber as an int.
     */
    public int getIdentificationNumber() {
        return identificationNumber;
    }

    /**
     * Set the colume of the pool in litres.
     *
     * @param volumeLitres a double.
     */
    public void setVolumeLitres(final double volumeLitres) {
        if (volumeLitres < 0) {
            this.volumeLitres = 0.0;
        } else {
            this.volumeLitres = volumeLitres;
        }
    }

    /**
     * Returns the temperature of the pool in degrees celsius.
     *
     * @param temperatureCelsius a double.
     */
    public void setTemperatureCelsius(final double temperatureCelsius) {
        if (temperatureCelsius < MINIMUM_POOL_TEMP_CELSIUS
                || temperatureCelsius > MAXIMUM_POOL_TEMP_CELSIUS) {
            this.temperatureCelsius = DEFAULT_POOL_TEMP_CELSIUS;
        } else {
            this.temperatureCelsius = temperatureCelsius;
        }
    }

    public void setPH(final double newPH) {
        final double maxPH = 14.0;
        if (newPH < 0.0 || newPH > maxPH) {
            this.pH = NEUTRAL_PH;
        } else {
            this.pH = newPH;
        }
    }

    /**
     * Sets the Nutrient coefficient. ignores values less than 0.0 or greater than 1.0.
     *
     * @param nutrientCoefficient a double.
     */
    public void setNutrientCoefficient(final double nutrientCoefficient) {
        if (nutrientCoefficient < 0.0 || nutrientCoefficient > 1.0) {
            this.nutrientCoefficient = DEFAULT_NUTRIENT_COEFFICIENT;
        } else {
            this.nutrientCoefficient = nutrientCoefficient;
        }
    }

    public void changeNutrientCoefficient(final double delta) {
        nutrientCoefficient += delta;
        if (nutrientCoefficient < MINIMUM_NUTRIENT_COEFFICIENT) {
            nutrientCoefficient = MINIMUM_NUTRIENT_COEFFICIENT;
        }
        if (nutrientCoefficient > MAXIMUM_NUTRIENT_COEFFICIENT) {
            nutrientCoefficient = MAXIMUM_NUTRIENT_COEFFICIENT;
        }
    }

    /**
     * Change the temperature by a given amount.
     *
     * @param delta must be a double.
     */
    public void changeTemperature(final double delta) {
        temperatureCelsius += delta;
        if (temperatureCelsius < MINIMUM_POOL_TEMP_CELSIUS) {
            temperatureCelsius = MINIMUM_POOL_TEMP_CELSIUS;
        }
        if (temperatureCelsius > MAXIMUM_POOL_TEMP_CELSIUS) {
            temperatureCelsius = MAXIMUM_POOL_TEMP_CELSIUS;
        }
    }

    /**
     * Returns the number of pools created.
     *
     * @return numberOfPools as an integer.
     */
    public static int getNumberCreated() {
        return numberOfPools;
    }

    public boolean addGuppy(final Guppy guppy) {
        if (guppy == null) {
            return false;
        }
        guppiesInPool.add(guppy);
        return true;
    }

    /**
     * Returns the number of guppies in the pool.
     *
     * @return the size of the guppiesInPool arrayList as an int.
     */
    public int getPopulation() {
        int population = 0;
        for (Guppy guppy : guppiesInPool) {
            if (guppy.getIsAlive()) {
            population++;
            }
        }
        return population;
    }

    /**
     * Randomly kill off guppies by starvation.
     *
     * @return the number of guppies that die from starvation as an integer.
     */
    public int applyNutrientCoefficient() {
        int numberOfGuppiesThatDied = 0;
        for (Guppy guppy: guppiesInPool) {
            double hungerScore = randomNumberGenerator.nextDouble();
            if (hungerScore > this.nutrientCoefficient) {
                guppy.setIsAlive(false);
                numberOfGuppiesThatDied++;
            }
        }
        return numberOfGuppiesThatDied;
    }

    /**
     * Remove the dead guppies from this pool.
     *
     * @return number of guppies removed as an integer.
     */
    public int removeDeadGuppies() {
        int numberOfDeadGuppiesRemovedFromPool = 0;
        Iterator<Guppy> it = guppiesInPool.iterator();
        while (it.hasNext()) {
            Guppy guppy = it.next();
            if (!guppy.getIsAlive()) {
                it.remove();
                numberOfDeadGuppiesRemovedFromPool++;
            }
        }
        return numberOfDeadGuppiesRemovedFromPool;
    }

    /**
     * Calculate the volume requirements for the guppies in this pool.
     *
     * @return the volume of water needed as a double.
     */
    public double getGuppyVolumeRequirementInLitres() {
        final double numberofMilitresInLitre = 1000;
        double volumeOfWaterNeededinMl = 0.0;
        for (Guppy guppy: guppiesInPool) {
            if (guppy.getIsAlive()) {
                    volumeOfWaterNeededinMl += guppy.getVolumeNeeded();
            }
        }
        return (volumeOfWaterNeededinMl / numberofMilitresInLitre);
    }

    /**
     * Calculate the average age in weeks of the guppies in this pool.
     *
     * @return the average age in weeks as a double.
     */
    public double getAverageAgeInWeeks() {
            double sumOfAllGuppiesAges = 0.0;
            for (Guppy guppy: guppiesInPool) {
                sumOfAllGuppiesAges += guppy.getAgeInWeeks();
            }
            if (guppiesInPool.size() == 0) {
                return 0;
            }
            return sumOfAllGuppiesAges / guppiesInPool.size();
        }

    /**
     * Calculate the average health coefficient of the guppies in the pool.
     *
     * @return the average health coefficient as a double.
     */
    public double getAverageHealthCoefficient() {
            double sumOfAllGuupyHealthCoefficients = 0.0;
            for (Guppy guppy: guppiesInPool) {
                if (guppy.getIsAlive()) {
                    sumOfAllGuupyHealthCoefficients += guppy.getHealthCoefficient();
                }
            }
            return sumOfAllGuupyHealthCoefficients / guppiesInPool.size();
        }

    /**
     * Calculated the percentage of guppies in the pool that are female.
     *
     * @return the percentage of females as a double.
     */
    public double getFemalePercentage() {
            int size;
            double numberOfFemales = 0;
            for (Guppy guppy: guppiesInPool) {
                if (guppy.getIsFemale()) {
                    numberOfFemales += 1;
                }
            }
            if (guppiesInPool.size() > 0) {
                size = guppiesInPool.size();
            } else {
                return 0;
            }
            return (numberOfFemales / size);
        }

    /**
     * Determines the median age of guppies in the pool.
     *
     * @return the median age as a double.
     */
    public double getMedianAge() {
        ArrayList<Integer> ages = new ArrayList<>();
        if (guppiesInPool.size() == 0) {
            return 0.0;
        }
        for (Guppy guppy: guppiesInPool) {
            ages.add(guppy.getAgeInWeeks());
        }
        Collections.sort(ages);
        if (ages.size() % 2 == 0) {
            double ageRightBeforeMiddle = (double) ages.get((ages.size() / 2) - 1);
            double ageRightAfterMiddle = (double) ages.get(ages.size() / 2);
            return ((ageRightBeforeMiddle + ageRightAfterMiddle) / 2);
        } else if (ages.size() == 1) {
            return ages.get(0);
        } else {
                return (double) ages.get(ages.size() / 2);
            }
        }

    /**
     * Completes a cycle of spawning and adds the new guppies to the pool.
     *
     * @return the number of new guppies added as an integer.
     */
    public int spawn() {
        int numberOfGuppiesAddedToPool = 0;
        ArrayList<Guppy> currentBabies;
        ArrayList<Guppy> newBabies = new ArrayList<>();
        for (Guppy guppy : guppiesInPool) {
            currentBabies = guppy.spawn();
            if (currentBabies != null) {
                newBabies.addAll(currentBabies);
            }
        }
            guppiesInPool.addAll(newBabies);

            numberOfGuppiesAddedToPool += newBabies.size();
        return numberOfGuppiesAddedToPool;
    }

    /**
     * Increment the ages of all the guppies in this pool by one.
     *
     * @return the number of guppies that die from old-age by one.
     */
    public int incrementAges() {
        int numberDead = 0;
        for (Guppy guppy: guppiesInPool) {
            guppy.incrementAge();
            if (!guppy.getIsAlive()) {
                numberDead++;
            }
        }
        return numberDead;
    }


    /**
     * Reduced the population of guppies in the pool in response to overcrowding.
     *
     * @return the number of guppies killed by overcrowding as an integer.
     */
    public int adjustForCrowding() {
        final int numberOfMillilitresInALitre = 1000;
        double volumeRequired = this.getGuppyVolumeRequirementInLitres();
        if (volumeRequired < volumeLitres) {
            return 0;
        }
        int numberOfGuppiesDiedDueToCrowding = 0;
        Collections.sort(this.guppiesInPool, new Comparator<Guppy>() {
            @Override
            public int compare(Guppy guppy1, Guppy guppy2) {
                return Double.compare(guppy1.getHealthCoefficient(),
                        guppy2.getHealthCoefficient());
            }
        });
        for (Guppy guppy: guppiesInPool) {
            volumeRequired -= (guppy.getVolumeNeeded() / numberOfMillilitresInALitre);
            guppy.setIsAlive(false);
            numberOfGuppiesDiedDueToCrowding++;
            if (volumeRequired < volumeLitres) {
                return numberOfGuppiesDiedDueToCrowding;
            }
        }
        return numberOfGuppiesDiedDueToCrowding;
    }


    /**
     * Returns a String representation of this pool.
     *
     * @return toString a String representation.
     */
    @Override
    public String toString() {
        return "Pool{"
                + "name='" + name + '\''
                + ", volumeLitres=" + volumeLitres
                + ", temperatureCelsius="
                + temperatureCelsius + ", pH=" + pH
                + ", nutrientCoefficient=" + nutrientCoefficient
                + ", identificationNumber=" + identificationNumber
                + ", guppiesInPool=" + guppiesInPool
                + ", randomNumberGenerator=" + randomNumberGenerator
                + '}';
    }

    /**
     * Compares the specified object to this Pool.
     *
     * @param other the other object
     * @return true if this equals other, else false.
     */
    @Override
    public boolean equals(final Object other) {
        if (this == other) {
            return true;
        }
        if (!(other instanceof Pool)) {
            return false;
        }

        if (other == null || getClass() != other.getClass()) {
            return false;
        }
        Pool pool = (Pool) other;
        return Double.compare(pool.getVolumeLitres(), getVolumeLitres()) == 0
                && Double.compare(pool.getTemperatureCelsius(), getTemperatureCelsius()) == 0
                && Double.compare(pool.getPH(), getPH()) == 0
                && Double.compare(pool.getNutrientCoefficient(), getNutrientCoefficient()) == 0
                && getName().equals(pool.getName())
                && guppiesInPool.equals(pool.guppiesInPool);
    }

    /**
     * Returns a hashcode.
     *
     * @return int representing the state of this pool.
     */
    @Override
    public int hashCode() {
        return Objects.hash(getName(), getVolumeLitres(),
                getTemperatureCelsius(), getPH(), getNutrientCoefficient(), guppiesInPool);
    }
}
