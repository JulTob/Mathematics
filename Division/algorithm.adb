with Ada.Text_IO; use Ada.Text_IO;
With Ada.Integer_Text_IO; use Ada.Integer_Text_IO; 


procedure Algorithm is
    N : Natural := 1;
    d : Natural := 27;
    q : Natural := 0;
    r : Natural := 0;
begin
    if d > n then
        q := 0;
        r := n;
    else
        q := 1;
        while n - q*d >= d loop
            q := q+1;
            end loop;
        r := n - q * d; 
    end if;
    put(N,1); Put("/"); --box of 1 character
    put(d,1); Put("=");
    put(q, 1); 
    Put("r"); put(r,1);

    New_Line;
    -- Check
    put(N,1); Put("/"); --box of 1 character
    put(d,1); Put("=");
    put(N/d, 1); 
    Put("r"); put(N mod d,1);
    
end Algorithm;
