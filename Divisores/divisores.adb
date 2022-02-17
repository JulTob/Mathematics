with Ada.Text_IO; use Ada.Text_IO;
With Ada.Integer_Text_IO; use Ada.Integer_Text_IO; 


procedure Divisores is
    N : Natural := 30;
begin
    for M in 1 .. N loop
       for d in 2..M loop  
        if M mod d = 0 then
          put(d);
        end if;
      end loop;
      New_Line;
     end loop;              

end Divisores;
