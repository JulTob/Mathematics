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

type Number is new Integer;

type Probability is New Float range 0.0 .. 1.0 digits 10;

type Frequency is new record   
  ThisMany: Natural;
  OutOf: Natural;
  end record;

function New_Measures return Measures_type;
function Measured_Sample return Measures_type;
