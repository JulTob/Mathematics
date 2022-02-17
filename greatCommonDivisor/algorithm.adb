with Ada.Text_IO; use Ada.Text_IO;
With Ada.Integer_Text_IO; use Ada.Integer_Text_IO; 


    

procedure Algorithm is
    X : Integer := 7;
    Y : Integer := 5;
    a : Natural := 3;
    b : Natural := 5;
    
    function GCD  -- Great Common divisor
        (
        X: in Natural;
        Y: in Natural)
        return Integer is
        result : Natural := 1;
        n :Natural :=1;
        begin
            while n < X OR n < Y loop
                if (x mod n)= 0 and (y mod n)=0 then
                    result := n;
                    end if;
                n := n +1;
            end loop;
            return result;
        end GCD;
        
    function is_Coprime 
        (
        X : in Natural;
        Y : in Natural)
        return boolean
        is
        begin
            return GCD(X,Y) = 1;
        end is_Coprime;
    
    
    
begin
    Put("GCD(");
    put(X,1); Put(","); --box of 1 character
    put(Y,1); Put(")=");
    put(GCD(X,Y), 1); 
    if is_Coprime(X,Y) then put(" Is Coprime"); end if;


end Algorithm;
