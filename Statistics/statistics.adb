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

package body Statistics is

  -- Implicit conversion from Integer to Number
  function Number (X : Integer) return Number is
    begin
      return Number(Float(X));
      end Number;

  -- Conversion for array of Floats to array of Numbers
  function To_Data_Array (Data : array (Positive range <>) of Float) return Measures_Array is
    Result : Measures_Array(1 .. Data'Length);
    begin
      for I in Data'Range loop
        Result(I) := Number(Data(I));
        end loop;
      return Result;
      end To_Data_Array;


  -- Mean Calculation
  function Mean (Data : Measures_Array) return Number is
    Total : Number := 0.0;
    begin
      for I in Data'Range loop
        Total := Total + Data(I);
        end loop;
      return Total / Number(Data'Length);
      end Mean;

  -- Variance Calculation
  function Variance (Data : Measures_Array) return Number is
    M : Number := Mean(Data);
    Total : Number := 0.0;
    begin
      for I in Data'Range loop
        Total := Total + (Data(I) - M) ** 2;
        end loop;
      return Total / Number(Data'Length);
      end Variance;

  -- Standard Deviation Calculation
  function Standard_Deviation (Data : Measures_Array) return Number is
    begin
      return Ada.Numerics.Sqrt(Variance(Data));
      end Standard_Deviation;

  -- Random Sampling Function
  function Random_Sample (Data : Measures_Array; Sample_Size : Positive) return Measures_Array is
    package Random_Floats is new Ada.Numerics.Float_Random;
    Gen : Random_Floats.Generator;
    Sample : Measures_Array(1 .. Sample_Size);
    Picked : Positive;
    begin
      Random_Floats.Reset(Gen);
      for I in 1 .. Sample_Size loop
        Picked := Positive(Random_Floats.Random(Gen) * Number(Data'Length)) + 1;
        Sample(I) := Data(Picked);
        end loop;
      return Sample;
      end Random_Sample;

  end Statistics;

