--------------------------
--  Statistics Library  --
--______________________--
-- Descriptive Statistics
--
-- Population: Complete collection of potential or real observations
-- Sample: Actual measured observations from a population
-- Random Sample: When all samples are drawn from the population with equal probability
-- Experiment: Controlled parameters
-- Random Assignment: When samples are divided into control group and experimental

type Number is new Integer;

type Probability is New Float range 0.0 .. 1.0 digits 10;

type Frequency is new record   
  ThisMany: Natural;
  OutOf: Natural;
  end record;

type Population is new Enum
  ( Value1, Value2);

--Population: Sample Space
type Measures_type is new Array(Population);

Function New_Measures() return Measures_type
  New_Measures: Measures:= (others=>0);
  begin
    return New_Measures;
    end New_Measures;

function Measured_Sample() return Measures_type is
  Sample: Measures_type := (others => 0);
  begin
    -- Placeholder logic: Sample of measures is returned
    return Sample;
    end Measured_Sample;

