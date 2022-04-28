with Ada.Text_IO; use Ada.Text_IO;
With Ada.Integer_Text_IO; use Ada.Integer_Text_IO; 


procedure Divisor is
    N : Natural := 365*24*60*60 + 6*60*60; -- Seconds in a year
    d : Natural := 1;
  begin
  put(n);   New_Line; 
  while d*d <= n loop  
    if n mod d = 0 then
      put(d);
      end if;
    d := d+1;
    end loop;
  end Divisor;
