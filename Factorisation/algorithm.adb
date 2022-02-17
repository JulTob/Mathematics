with Ada.Text_IO; use Ada.Text_IO;
With Ada.Integer_Text_IO; use Ada.Integer_Text_IO; 


procedure algorithm is
    
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
    
    X : Natural := 555;
begin
    Put("Factors: ");
    put(X,1); Put(" = "); 
    factorization(x);
    Put(" "); 
end algorithm;
