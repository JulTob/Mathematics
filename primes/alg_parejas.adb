with Ada.Text_IO; use Ada.Text_IO;
With Ada.Integer_Text_IO; use Ada.Integer_Text_IO; 


procedure alg_parejas is
    function is_Prime(
        N: in Natural) return Boolean
        is
        begin
          if N = 1  then return false; end if;  -- (:
          if N = 2  then return true; end if;  -- (:
          if N rem 2 = 0  then return false; end if;  -- (:

            for i in 2..N/2 loop
                if  --is_Prime(i) and then 
                    N rem i = 0 then
                        return false;
                end if;
            end loop;
            return true;
        end Is_Prime;
        
        
    procedure factorization
        (
        N: in Natural)
        is
        M: Natural := N;
        i: Natural := 2;
        begin
        while i <= M loop
            if i = M then
                Put(i,1);
                M := M/i;
                end if;

            if M rem i = 0 then
                Put(i,1); Put(" · ");
                M := M/i;
            else
                i := i+1;
                end if;
        end loop;
        
        end factorization;
    
    N : Natural := 250;
begin
for x in 1..N loop
for y in x..N loop
    
    if is_prime(x) and is_prime(y) and is_prime(x*y+1) then
        put(x,1); put(","); put(y,1); put(" >> ");put(x*y+1,1);
        New_Line;
    end if;
    end loop;
    end loop;

end alg_parejas;
