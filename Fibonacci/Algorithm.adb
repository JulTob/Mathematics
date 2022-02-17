with Ada.Text_IO; use Ada.Text_IO;
With Ada.Integer_Text_IO; use Ada.Integer_Text_IO; 


    

procedure Algorithm is
    
    function Fibonacci
        (
        Order: in Natural)
        return Natural is
        begin
        if Order = 0 then return 1; end if;
        if Order = 1 then return 1; end if;
            
        return Fibonacci(Order-1) +Fibonacci(Order-2);
        
        end Fibonacci;
    
    
begin
    Put("Fibonacci: ");
    for i in 1..30 loop
        put(Fibonacci(i),1); Put(", "); --box of 1 character
        end loop;

end Algorithm;
