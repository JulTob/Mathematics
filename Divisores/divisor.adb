with Ada.Text_IO; use Ada.Text_IO;
With Ada.Integer_Text_IO; use Ada.Integer_Text_IO; 


procedure Divisor is
    N : Natural := 156;
    d : Natural := 1;
begin
  while d*d <= n loop  
    if n mod d = 0 then
      put(d);
    end if;
    d := d+1;
  end loop;
end Divisor;
