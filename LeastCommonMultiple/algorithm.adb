with Ada.Text_IO; use Ada.Text_IO;
With Ada.Integer_Text_IO; use Ada.Integer_Text_IO; 


    

procedure Algorithm is
    X : Integer := 5**2;
    Y : Integer := 7*7;

    
    function LCM -- Least common multiple 
        (
        X: in Natural;
        Y: in Natural)
        return Integer is
        n :Natural :=1;
        begin
            loop
                if (n mod x)= 0 and (n mod y)=0 then
                    return n;
                    end if;
                n := n +1;
            end loop;
        end LCM;
        
    
    
begin
    Put("LCM(");
    put(X,1); Put(","); --box of 1 character
    put(Y,1); Put(")=");
    put(LCM(X,Y), 1); 



end Algorithm;
