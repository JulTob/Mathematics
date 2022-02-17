with Ada.Text_IO; use Ada.Text_IO;
--With Ada.Float_Text_IO; use Ada.Float_Text_IO; 


procedure divisible is
    n : Natural := 15;
    d : Natural := 7;
begin
  if n mod d = 0 then
    put("d ∣ n ");
    else
    put("d ∤ n ");
    end if;

end Divisible;
