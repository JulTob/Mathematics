-------------------------
--  Statistics Library --
--_____________________--
-- Descriptive Statistics
--
-- Population: Complete collection of potential or real observations
-- Sample: Actual measured observations from a population
-- Random Sample: When all samples are drawn from the population with equal probability
-- Experiment: Controlled parameters
-- Random Assignment: When samples are divided into control group and experimental

with Ada.Numerics.Float_Random;

package Statistics is
  
  type Number is private;

  type Measures_Array is array (Positive range <>) of Number;

  type Probability is New Float range 0.0 .. 1.0 digits 10;

  -- Basic statistics functions
  function Mean (Data : Measures_Array) return Number;
  function Variance (Data : Measures_Array) return Number;
  function Standard_Deviation (Data : Measures_Array) return Number;

  -- Sampling functions
  function Random_Sample (Data : Measures_Array; Sample_Size : Positive) return Measures_Array;

  private
    -- Defining Number as a fixed-point type with delta precision
    type Number is delta 0.001;

  end Statistics;
