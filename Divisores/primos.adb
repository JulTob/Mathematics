with Ada.Text_IO; use Ada.Text_IO;
With Ada.Integer_Text_IO; use Ada.Integer_Text_IO; 


procedure Hello is
    N : Natural := 21;
    d : Natural := 1;
begin
  while d <= n loop  
    if n mod d = 0 then
      put(d);
      N := N / d;
    end if;
    d := d+1;
  end loop;
end Hello;
