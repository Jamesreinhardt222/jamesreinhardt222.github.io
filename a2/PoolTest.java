package ca.bcit.comp2522.assignments.a2;

import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.ExpectedException;

import java.util.Random;

import static org.junit.Assert.*;

public class PoolTest {

    private Pool defaultPool;
    private Pool testPool;

    @Rule
    public ExpectedException thrown = ExpectedException.none();

    @Before
    public void setUp() throws Exception {

        defaultPool = new Pool();
        testPool = new Pool("Skookumchuk",
                1000.0,
                40.0,
                7.0,
                0.5);
    }

    @Test
    public void containsConstantCalledDEFAULT_POOL_NAME() {
        assertTrue(Pool.DEFAULT_POOL_NAME.equals(Pool.DEFAULT_POOL_NAME));
    }

    @Test
    public void containsConstantCalledDEFAULT_POOL_TEMP_CELSIUS() {
        assertEquals(40.0, Pool.DEFAULT_POOL_TEMP_CELSIUS, 0.0);
    }

    @Test
    public void containsConstantCalledMINIMUM_POOL_TEMP_CELSIUS() {
        assertEquals(0.0, Pool.MINIMUM_POOL_TEMP_CELSIUS, 0.0);
    }

    @Test
    public void containsConstantCalledMAXIMUM_POOL_TEMP_CELSIUS() {
        assertEquals(100.0, Pool.MAXIMUM_POOL_TEMP_CELSIUS, 0.0);
    }

    @Test
    public void containsConstantCalledNEUTRAL_PH() {
        assertEquals(7.0, Pool.NEUTRAL_PH, 0.0);
    }

    @Test
    public void containsConstantCalledDEFAULT_NUTRIENT_COEFFICIENT() {
        assertEquals(0.5, Pool.DEFAULT_NUTRIENT_COEFFICIENT, 0.0);
    }

    @Test
    public void containsConstantCalledMINIMUM_NUTRIENT_COEFFICIENT() {
        assertEquals(0.0, Pool.MINIMUM_NUTRIENT_COEFFICIENT, 0.0);
    }

    @Test
    public void containsConstantCalledMAXIMUM_NUTRIENT_COEFFICIENT() {
        assertEquals(1.0, Pool.MAXIMUM_NUTRIENT_COEFFICIENT, 0.0);
    }

    @Test
    public void staticPoolCounterIsCorrectlyTrackingPoolsInDefaultConstructor() {
        final int numberAlreadyCreated = Pool.getNumberCreated();
        final int numberCreated = 100;
        for (int i = 0; i < numberCreated; ++i) {
            Pool aPool = new Pool();
        }
        assertEquals(numberAlreadyCreated + numberCreated, Pool.getNumberCreated());
    }

    @Test
    public void staticPoolCounterIsCorrectlyTrackingPoolsInMultiParamConstructor() {
        final int numberAlreadyCreated = Pool.getNumberCreated();
        final int numberCreated = 100;
        for (int i = 0; i < numberCreated; ++i)
            new Pool("Skookumchuk",
                    1000.0,
                    Pool.DEFAULT_POOL_TEMP_CELSIUS,
                    Pool.NEUTRAL_PH,
                    Pool.DEFAULT_NUTRIENT_COEFFICIENT);
        assertEquals(numberAlreadyCreated + numberCreated, Pool.getNumberCreated());
    }

    @Test
    public void defaultPoolIsSetToCorrectValues() {
        assertTrue(defaultPool.getName().equals(Pool.DEFAULT_POOL_NAME));
        assertEquals(0, defaultPool.getVolumeLitres(), 0.0);
        assertEquals(Pool.DEFAULT_POOL_TEMP_CELSIUS, defaultPool.getTemperatureCelsius(), 0.0);
        assertEquals(Pool.NEUTRAL_PH, defaultPool.getPH(), 0.0);
        assertEquals(Pool.DEFAULT_NUTRIENT_COEFFICIENT, defaultPool.getNutrientCoefficient(), 0.0);
    }

    @Test
    public void multiParamPoolIsSetToCorrectValues() {
        assertTrue(testPool.getName().equals("Skookumchuk"));
        assertEquals(1000.0, testPool.getVolumeLitres(), 0.0);
        assertEquals(Pool.DEFAULT_POOL_TEMP_CELSIUS, testPool.getTemperatureCelsius(), 0.0);
        assertEquals(Pool.NEUTRAL_PH, testPool.getPH(), 0.0);
        assertEquals(Pool.DEFAULT_NUTRIENT_COEFFICIENT, testPool.getNutrientCoefficient(), 0.0);
    }


    @Test
    public void identificationNumbersAreSequentialAndUniqueInDefaultConstruction() {
        Pool first = new Pool();
        int firstID = first.getIdentificationNumber() + 1;
        final int numberCreated = 100;
        for (int i = 0; i < numberCreated; ++i) {
            Pool littlePool = new Pool();
            assertEquals(firstID + i, littlePool.getIdentificationNumber());
        }
    }

    @Test
    public void identificationNumbersAreSequentialAndUniqueInMultiParamConstruction() {
        Pool first = new Pool();
        int firstID = first.getIdentificationNumber() + 1;
        int numberCreated = 100;
        for (int i = 0; i < numberCreated; ++i) {
            Pool newPool = new Pool("Skookumchuk",
                    1000.0,
                    Pool.DEFAULT_POOL_TEMP_CELSIUS,
                    Pool.NEUTRAL_PH,
                    Pool.DEFAULT_NUTRIENT_COEFFICIENT);
            assertEquals(firstID + i, newPool.getIdentificationNumber());
        }
    }

    @Test
    public void poolNameIsCorrectlyFormattedAndStored() {
        Pool newPool = new Pool("     ohmy     ",
                1000.0,
                Pool.DEFAULT_POOL_TEMP_CELSIUS,
                Pool.NEUTRAL_PH,
                Pool.DEFAULT_NUTRIENT_COEFFICIENT);
        assertTrue(newPool.getName().equals("Ohmy"));
    }

    @Test
    public void createExceptionWithWhitespaceName() {
        thrown.expect(IllegalArgumentException.class);
        Pool newPool = new Pool("           ",
                1000.0,
                Pool.DEFAULT_POOL_TEMP_CELSIUS,
                Pool.NEUTRAL_PH,
                Pool.DEFAULT_NUTRIENT_COEFFICIENT);
    }

    @Test
    public void multiParamConstructorSubsZeroForNegativeVolume() {
        Pool newPool = new Pool("Skookumchuk",
                -1.0,
                Pool.DEFAULT_POOL_TEMP_CELSIUS,
                Pool.NEUTRAL_PH,
                Pool.DEFAULT_NUTRIENT_COEFFICIENT);
        assertEquals(0.0, newPool.getVolumeLitres(), 0.0);
    }

    @Test
    public void multiParamConstructorSubsDEFAULTForNegativeTemperature() {
        Pool newPool = new Pool("Skookumchuk",
                0,
                -1.0,
                Pool.NEUTRAL_PH,
                Pool.DEFAULT_NUTRIENT_COEFFICIENT);
        assertEquals(Pool.DEFAULT_POOL_TEMP_CELSIUS, newPool.getTemperatureCelsius(), 0.0);
    }

    @Test
    public void multiParamConstructorSubDEFAULTForOverlyHighTemperature() {
        Pool newPool = new Pool("Skookumchuk",
                0,
                1000.0,
                Pool.NEUTRAL_PH,
                Pool.DEFAULT_NUTRIENT_COEFFICIENT);
        assertEquals(Pool.DEFAULT_POOL_TEMP_CELSIUS, newPool.getTemperatureCelsius(), 0.0);
    }

    @Test
    public void multiParamConstructorSubsNEUTRALForNegativePH() {
        Pool newPool = new Pool("Skookumchuk",
                0,
                Pool.DEFAULT_POOL_TEMP_CELSIUS,
                -1,
                Pool.DEFAULT_NUTRIENT_COEFFICIENT);
        assertEquals(Pool.NEUTRAL_PH, newPool.getPH(), 0.0);
    }

    @Test
    public void multiParamConstructorSubsNEUTRALForOverlargePH() {
        Pool newPool = new Pool("Skookumchuk",
                0,
                Pool.DEFAULT_POOL_TEMP_CELSIUS,
                15,
                Pool.DEFAULT_NUTRIENT_COEFFICIENT);
        assertEquals(Pool.NEUTRAL_PH, newPool.getPH(), 0.0);
    }

    @Test
    public void multiParamConstructorSubsDEFAULTForNegativeNutrientCoefficient() {
        Pool newPool = new Pool("Skookumchuk",
                0,
                Pool.DEFAULT_POOL_TEMP_CELSIUS,
                Pool.NEUTRAL_PH,
                -0.01);
        assertEquals(Pool.DEFAULT_NUTRIENT_COEFFICIENT, newPool.getNutrientCoefficient(), 0.0);
    }

    @Test
    public void multiParamConstructorSubsDEFAULTForOverlargeNutrientCoefficient() {
        Pool newPool = new Pool("Skookumchuk",
                0,
                Pool.DEFAULT_POOL_TEMP_CELSIUS,
                Pool.NEUTRAL_PH,
                1.01);
        assertEquals(Pool.DEFAULT_NUTRIENT_COEFFICIENT, newPool.getNutrientCoefficient(), 0.0);
    }

    @Test
    public void nameAccessorReturnsCorrectName() {
        assertTrue(defaultPool.getName().equals(Pool.DEFAULT_POOL_NAME));
        assertTrue(testPool.getName().equals("Skookumchuk"));
    }

    @Test
    public void volumeAccessorReturnsCorrectVolume() {
        assertEquals(0.0, defaultPool.getVolumeLitres(), 0.0);
        assertEquals(1000.0, testPool.getVolumeLitres(), 0.0);
    }

    @Test
    public void temperatureAccessorReturnsCorrectTemperature() {
        assertEquals(40.0, defaultPool.getTemperatureCelsius(), 0.0);
        assertEquals(40.0, testPool.getTemperatureCelsius(), 0.0);
    }

    @Test
    public void nutrientCoefficientAccessorReturnsCorrectPH() {
        assertEquals(Pool.DEFAULT_NUTRIENT_COEFFICIENT, defaultPool.getNutrientCoefficient(), 0.0);
        assertEquals(Pool.DEFAULT_NUTRIENT_COEFFICIENT, testPool.getNutrientCoefficient(), 0.0);
    }

    @Test
    public void volumeMutatorIgnoresNegativeArguments() {
        double volume = defaultPool.getVolumeLitres();
        defaultPool.setVolumeLitres(-0.01);
        assertEquals(volume, defaultPool.getVolumeLitres(), 0.0);
    }

    @Test
    public void temperatureMutatorIgnoresNegativeArguments() {
        double temperature = defaultPool.getTemperatureCelsius();
        defaultPool.setTemperatureCelsius(Pool.MINIMUM_POOL_TEMP_CELSIUS - 0.01);
        assertEquals(temperature, defaultPool.getTemperatureCelsius(), 0.0);
    }

    @Test
    public void temperatureMutatorIgnoresOverlargeArguments() {
        double temperature = defaultPool.getTemperatureCelsius();
        defaultPool.setTemperatureCelsius(Pool.MAXIMUM_POOL_TEMP_CELSIUS + 0.01);
        assertEquals(temperature, defaultPool.getTemperatureCelsius(), 0.0);
    }

    @Test
    public void pHMutatorIgnoresNegativeArguments() {
        double pH = defaultPool.getPH();
        defaultPool.setPH(-0.01);
        assertEquals(pH, defaultPool.getPH(), 0.0);
    }

    @Test
    public void pHMutatorIgnoresOverlargeArguments() {
        double pH = defaultPool.getPH();
        defaultPool.setPH(14.01);
        assertEquals(pH, defaultPool.getPH(), 0.0);
    }

    @Test
    public void nutrientCoefficientMutatorIgnoresNegativeArguments() {
        double nutrientCoefficient = defaultPool.getNutrientCoefficient();
        defaultPool.setNutrientCoefficient(-0.01);
        assertEquals(nutrientCoefficient, defaultPool.getNutrientCoefficient(), 0.0);
    }

    @Test
    public void nutrientCoefficientMutatorIgnoresOverlargeArguments() {
        double nutrientCoefficient = defaultPool.getNutrientCoefficient();
        defaultPool.setNutrientCoefficient(1.01);
        assertEquals(nutrientCoefficient, defaultPool.getNutrientCoefficient(), 0.0);
    }

    @Test
    public void changeNutrientCoefficientWillNotPermitOverlargeNutrientCoefficients() {
        testPool.changeNutrientCoefficient(1.5);
        assertEquals(1.0, testPool.getNutrientCoefficient(), 0.0);
    }


    @Test
    public void changeNutrientCoefficientWillNotPermitNegativeNutrientCoefficients() {
        testPool.changeNutrientCoefficient(-1.5);
        assertEquals(Pool.MINIMUM_NUTRIENT_COEFFICIENT, testPool.getNutrientCoefficient(), 0.0);
    }

    @Test
    public void changeTemperatureWillNotPermitOverhighTemperature() {
        testPool.changeTemperature(150.0);
        assertEquals(Pool.MAXIMUM_POOL_TEMP_CELSIUS, testPool.getTemperatureCelsius(), 0.0);
    }


    @Test
    public void changeTemperatureWillNotPermitNegativeTemperature() {
        testPool.changeTemperature(-150.0);
        assertEquals(Pool.MINIMUM_POOL_TEMP_CELSIUS, testPool.getTemperatureCelsius(), 0.0);
    }

    @Test
    public void cannotAddNullGuppy() {
        assertFalse(testPool.addGuppy(null));
        assertEquals(0, testPool.getPopulation());
    }

    @Test
    public void addingGuppyReturnsTrue() {
        assertTrue(testPool.addGuppy(new Guppy()));
        assertEquals(1, testPool.getPopulation());
    }

    @Test
    public void removeDeadGuppiesCullsDeadGuppies() {
        Guppy deadGuppy = new Guppy();
        deadGuppy.setIsAlive(false);
        assertTrue(testPool.addGuppy(deadGuppy));
        assertEquals(0, testPool.getPopulation());
        assertEquals(1, testPool.removeDeadGuppies());
        assertEquals(0, testPool.getPopulation());
    }

    @Test
    public void deadGuppiesNeedNoWater() {
        for (int i = 0; i < 100; ++i) {
            Guppy deadGuppy = new Guppy();
            deadGuppy.setIsAlive(false);
            assertTrue(testPool.addGuppy(deadGuppy));
        }
        assertEquals(0.0, testPool.getGuppyVolumeRequirementInLitres(), 0.0);
    }

    @Test
    public void emptyPoolHasAverageAgeOfZero() {
        assertEquals(0.0, testPool.getAverageAgeInWeeks(), 0.0);
    }

    @Test
    public void poolOfLivingGuppiesCalculatesCorrectAverageAge() {
        Random random = new Random();
        int count = 100;
        double ageSum = 0;
        for (int i = 0; i < count; ++i) {
            int randomAge = random.nextInt(50);
            ageSum += randomAge;
            Guppy newGuppy = new Guppy("Poecilia",
                    "elegans",
                    randomAge,
                    true,
                    3,
                    0.75);
            testPool.addGuppy(newGuppy);
        }
        assertEquals(ageSum / count, testPool.getAverageAgeInWeeks(), 0.05);
    }

    @Test
    public void deadGuppiesAreNotCountedWhenCalculatingAverageAge() {
        for (int i = 0; i < 100; ++i) {
            Guppy deadGuppy = new Guppy();
            deadGuppy.setIsAlive(false);
            assertTrue(testPool.addGuppy(deadGuppy));
        }
        assertEquals(0.0, testPool.getAverageAgeInWeeks(), 0.0);
    }

    @Test
    public void deadGuppiesAreNotCountedWhenCalculatingAverageHealthCoefficient() {
        for (int i = 0; i < 100; ++i) {
            Guppy deadGuppy = new Guppy();
            deadGuppy.setIsAlive(false);
            assertTrue(testPool.addGuppy(deadGuppy));
        }
        assertEquals(0.0, testPool.getAverageHealthCoefficient(), 0.0);
    }

    @Test
    public void calculatesAverageHealthCoefficientCorrectly() {
        Random random = new Random();
        int count = 100;
        double healthCoefficientSum = 0;
        for (int i = 0; i < count; ++i) {
            double randomHealthCoefficient = random.nextDouble();
            healthCoefficientSum += randomHealthCoefficient;
            Guppy newGuppy = new Guppy("Poecilia",
                    "elegans",
                    0,
                    true,
                    3,
                    randomHealthCoefficient);
            testPool.addGuppy(newGuppy);
        }
        assertEquals(healthCoefficientSum / count, testPool.getAverageHealthCoefficient(), 0.05);
    }

    @Test
    public void emptyPoolHasNoFemales() {
        assertEquals(0.0, testPool.getFemalePercentage(), 0.0);
    }

    @Test
    public void mixedPoolCalculatesFemalePercentageCorrectly() {
        Random random = new Random();
        int count = 100;
        int females = 0;
        for (int i = 0; i < count; ++i) {
            boolean female = random.nextBoolean();
            if (female) {
                females++;
            }
            Guppy newGuppy = new Guppy("Poecilia",
                    "elegans",
                    0,
                    female,
                    3,
                    0.75);
            testPool.addGuppy(newGuppy);
        }
        assertEquals((double) females / count, testPool.getFemalePercentage(), 0.05);
    }


    @Test
    public void testIfSpawnMethodDoesNotMakeMoreBabyGuppiesInAPoolWithAMaleGuppyOfBreedingAge() {
        Guppy newGuppy = new Guppy("Poecilia",
                "elegans",
                19, false,
                3,
                0.75);
        Pool pool = new Pool();
        pool.addGuppy(newGuppy);
        int actual = pool.spawn();
        int zero = 0;
        assertEquals(actual, zero);
    }

    @Test
    public void testIfSpawnMethodDoesNotMakeMoreBabyGuppiesInAPoolWithAMaleGuppyNotOfBreedingAge() {
        Guppy newGuppy = new Guppy("Poecilia",
                "elegans",
                1, false,
                3,
                0.75);
        Pool pool = new Pool();
        pool.addGuppy(newGuppy);
        int actual = pool.spawn();
        int zero = 0;
        assertEquals(actual, zero);
    }

    @Test
    public void testIfSpawnMethodDoesNotMakeMoreBabyGuppiesInAPoolWithAFemaleGuppyNotOfBreedingAge() {
        Guppy newGuppy = new Guppy("Poecilia",
                "elegans",
                1, true,
                3,
                0.75);
        Pool pool = new Pool();
        pool.addGuppy(newGuppy);
        int actual = pool.spawn();
        int zero = 0;
        assertEquals(actual, zero);
    }

    @Test
    public void testIfSpawnMethodOnAPoolWithAFemaleGuppyOfBreedingAgeIncreasesNumberOfBabiesBorn() {
        Guppy newGuppy = new Guppy("Poecilia",
                "elegans",
                19, true,
                3,
                0.75);
        Pool pool = new Pool();
        pool.addGuppy(newGuppy);
        int actual = pool.spawn();
        actual += pool.spawn();
        actual += pool.spawn();
        actual += pool.spawn();
        actual += pool.spawn();
        actual += pool.spawn();
        int zero = 0;
        assertTrue(actual > zero);
    }

    @Test
    public void testIfSpawnMethodIncreasesAPoolPopulationWithFemaleGuppyOfAge() {
        Guppy newGuppy = new Guppy("Poecilia",
                "elegans",
                19, true,
                3,
                0.75);
        Pool pool = new Pool();
        pool.addGuppy(newGuppy);
        int initialPopulation = pool.getPopulation();
        pool.spawn(); // Calls spawn method multiple times to increase chance of one instance being successful.
        pool.spawn();
        pool.spawn();
        pool.spawn();
        pool.spawn();
        pool.spawn();
        pool.spawn();
        int finalPopulation = pool.getPopulation();
        assertTrue((finalPopulation > initialPopulation));
    }

    @Test
    public void testIfSpawnMethodWorksAround50PercentOfTheTimeWithFemaleGuppyOfAge() {
        Guppy newGuppy = new Guppy("Poecilia",
                "elegans",
                19, true,
                3,
                0.75);
        Pool pool = new Pool();
        int count = 0;
        pool.addGuppy(newGuppy);
        int initialPopulation = pool.getPopulation();
        int finalPopulation = pool.getPopulation();
        for (int i = 0; i < 100; i++) {
            initialPopulation = pool.getPopulation();
            pool.spawn();
            finalPopulation = pool.getPopulation();
            if (finalPopulation > initialPopulation) {
                count++;
            }
        }
        assertTrue(count > 40 && count < 60);
    }


    @Test
    public void testIfSpawnMethodDoesNotIncreasesAPoolPopulationWithMaleGuppyOfAge() {
        Guppy newGuppy = new Guppy("Poecilia",
                "elegans",
                19, false,
                3,
                0.75);
        Pool pool = new Pool();
        pool.addGuppy(newGuppy);
        int initialPopulation = pool.getPopulation();
        pool.spawn();
        int finalPopulation = pool.getPopulation();
        assertFalse(finalPopulation > initialPopulation);
    }

    @Test
    public void testIfSpawnMethodDoesNotIncreaseAPoolPopulationWithFemaleGuppyNotOfAge() {
        Guppy newGuppy = new Guppy("Poecilia",
                "elegans",
                1, true,
                3,
                0.75);
        Pool pool = new Pool();
        pool.addGuppy(newGuppy);
        int initialPopulation = pool.getPopulation();
        pool.spawn();
        int finalPopulation = pool.getPopulation();
        assertFalse(finalPopulation > initialPopulation);
    }

    @Test
    public void testIfSpawnMethodDoesNotIncreasesAPoolPopulationWithMaleGuppyNotOfAge() {
        Guppy newGuppy = new Guppy("Poecilia",
                "elegans",
                1, false,
                3,
                0.75);
        Pool pool = new Pool();
        pool.addGuppy(newGuppy);
        int initialPopulation = pool.getPopulation();
        pool.spawn();
        int finalPopulation = pool.getPopulation();
        assertFalse(finalPopulation > initialPopulation);
    }

    @Test
    public void adjustForCrowdingKillsEveryGuppyInAnEmptyPool() {
        Guppy newGuppy = new Guppy("Poecilia",
                "elegans",
                1, false,
                3,
                0.75);
        Pool pool = new Pool();
        pool.addGuppy(newGuppy);
        pool.adjustForCrowding();
        assertTrue(pool.getPopulation() == 0);

    }

    @Test
    public void adjustForCrowdingdoesNotKillGuppiesInAnMassivePoolWithSufficientWater() {
        Guppy newGuppy = new Guppy("Poecilia",
                "elegans",
                1, false,
                3,
                0.75);
        Pool pool = new Pool("testPool", 1000.0,
                40.0,
                7.0,
                0.5);
        pool.addGuppy(newGuppy);
        pool.adjustForCrowding();
        assertTrue(pool.getPopulation() == 1);

    }

    @Test
    public void getMedianAgeReturnsMedianOfOddNumberOfGuppies() {
        Pool pool = new Pool();
        Guppy guppy1 = new Guppy("Poecilia",
                "elegans",
                1, false,
                3,
                0.75);
        Guppy guppy2 = new Guppy("Poecilia",
                "elegans",
                2, false,
                3,
                0.75);
        Guppy guppy3 = new Guppy("Poecilia",
                "elegans",
                3, false,
                3,
                0.75);
        pool.addGuppy(guppy1);
        pool.addGuppy(guppy2);
        pool.addGuppy(guppy3);
        double actual = pool.getMedianAge();
        double expected = 2.0;
        assertTrue(actual == expected);
    }

    @Test
    public void getMedianAgeReturnsMedianOfEvenNumberOfGuppies() {
        Pool pool = new Pool();
        Guppy guppy1 = new Guppy("Poecilia",
                "elegans",
                1, false,
                3,
                0.75);
        Guppy guppy2 = new Guppy("Poecilia",
                "elegans",
                2, false,
                3,
                0.75);
        Guppy guppy3 = new Guppy("Poecilia",
                "elegans",
                3, false,
                3,
                0.75);

        Guppy guppy4 = new Guppy("Poecilia",
                "elegans",
                4, false,
                3,
                0.75);
        pool.addGuppy(guppy1);
        pool.addGuppy(guppy2);
        pool.addGuppy(guppy3);
        pool.addGuppy(guppy4);
        double actual = pool.getMedianAge();
        double expected = 2.5;
        assertTrue(actual == expected);
    }

    @Test
    public void getMedianAgeOfOnlyGuppyInPool() {
        Pool pool = new Pool();
        Guppy lonelyGuppy = new Guppy("Poecilia",
                "elegans",
                30, false,
                3,
                0.75);

        pool.addGuppy(lonelyGuppy);
        double actual = pool.getMedianAge();
        double expected = 30.0;
        assertTrue(actual == expected);
    }

    @Test
    public void getMedianAgeReturnsZeroWhenNoGuppies() {
        Pool pool = new Pool();
        double actual = pool.getMedianAge();
        double expected = 0.0;
        assertTrue(actual == expected);
    }

    @Test
    public void incrementAgesIncrementsGuppyAge() {
        Pool pool = new Pool();
        Guppy lonelyGuppy = new Guppy("Poecilia",
                "elegans",
                12, false,
                3,
                0.75);
        pool.addGuppy(lonelyGuppy);
        pool.incrementAges();
        int actual = lonelyGuppy.getAgeInWeeks();
        int expected = 13;
        assertTrue(actual == expected);
    }

    @Test
    public void incrementAgesKillsOldGuppyOlderThan50weeks() {
        Pool pool = new Pool();
        Guppy oldGuppy = new Guppy("Poecilia",
                "elegans",
                49, false,
                3,
                0.75);
        pool.addGuppy(oldGuppy);
        pool.incrementAges();
        pool.incrementAges();
        boolean alive = oldGuppy.getIsAlive();
        boolean expected = false;
        assertTrue(alive == expected);
    }

    @Test
    public void ApplyNutrientCoefficientDoesNotKillWhenPoolNutrientCoefficientIsOne() {
        Pool poolTest = new Pool("Skookumchuk",
                1000.0,
                40.0,
                7.0,
                1.0);

        Guppy lonelyGuppy = new Guppy("Poecilia",
                "elegans",
                12, false,
                3,
                0.75);
        poolTest.addGuppy(lonelyGuppy);
        poolTest.applyNutrientCoefficient();
        boolean actual = lonelyGuppy.getIsAlive();
        boolean expected = true;
        assertTrue(actual == expected);
    }
    @Test
    public void ApplyNutrientCoefficientAlwaysKillsWhenPoolNutrientCoefficientIsZero() {
        Pool poolTest = new Pool("Skookumchuk",
                1000.0,
                40.0,
                7.0,
                0.0);

        Guppy lonelyGuppy = new Guppy("Poecilia",
                "elegans",
                12, false,
                3,
                0.75);
        poolTest.addGuppy(lonelyGuppy);
        poolTest.applyNutrientCoefficient();
        boolean actual = lonelyGuppy.getIsAlive();
        boolean expected = false;
        assertTrue(actual == expected);
    }

}

