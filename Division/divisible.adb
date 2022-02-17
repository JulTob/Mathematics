with Ada.Text_IO; use Ada.Text_IO;
With Ada.Integer_Text_IO; use Ada.Integer_Text_IO; 


    

procedure divisible is
    N : Natural := 100;
    d : Natural := 25;
    q : Natural := 0;
    r : Natural := 0;
    
    
    function is_Divisible 
        ( N : in Natural;
        d: in Natural)
        return boolean
        is
        begin
            return N mod d = 0;
        end Is_Divisible;
    
    
    
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
    if Is_Divisible(N,d) then put(" Is divisible"); end if;

    New_Line;
    -- Check
    put(N,1); Put("/"); --box of 1 character
    put(d,1); Put("=");
    put(N/d, 1); 
    Put("r"); put(N mod d,1);

end divisible;
