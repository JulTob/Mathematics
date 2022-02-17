with Ada.Text_IO; use Ada.Text_IO;
With Ada.Integer_Text_IO; use Ada.Integer_Text_IO; 


procedure Algorithm is
    N : Integer := 100;
    d : Natural := 3;
begin
    put(N,1); Put("/"); --box of 1 character
    put(d,1); Put("=");
    put(N/d, 1); 
    Put("r"); put(N mod d,1);

end Algorithm;
