with Ada.Text_IO; use Ada.Text_IO;

procedure Sum_List is

   -- Define a type alias for easy future changes
   subtype Number is Integer;  
      -- Change this to Float, Natural, etc., if needed

   -- Flexible List of Numbers to add
   type Number_Array is array (Positive range <>) of Number;

   function Sum(Arr : Number_Array) return Number is
      Total : Number := 0;
      begin
         for I in Arr'Range loop
            Total := Total + Arr(I);
            end loop;
         return Total;
      end Sum;

   -- Example usage
   Numbers : constant Number_Array := (1, 2, 3, 4, 5);
   Result  : Number;
   begin
      Result := Sum(Numbers);
      Put_Line("The sum is: " & Number'Image(Result));
   end Sum_List;

