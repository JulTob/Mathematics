with Ada.Text_IO; use Ada.Text_IO;
With Ada.Integer_Text_IO; use Ada.Integer_Text_IO; 


    

procedure Algorithm_Euclides is
    X : Integer := 36;
    Y : Integer := -28;
    
    function GCD_EUCLIDES  -- Great Common divisor, EUCLIDEAN ALGORITHM
        (
        X: in Integer;
        Y: in Integer)
        return Integer is
        begin
        if X = 0 then return Y; end if;
        if Y = 0 then return X; end if;
            
        return GCD_EUCLIDES(Y,X mod Y);
        
        end GCD_EUCLIDES;
        
    function is_Coprime 
        (
        X : in Integer;
        Y : in Integer)
        return boolean
        is
        begin
            return GCD_EUCLIDES(X,Y) = 1;
        end is_Coprime;
    
    
    
begin
    Put("GCD(");
    put(X,1); Put(","); --box of 1 character
    put(Y,1); Put(")=");
    put(GCD_EUCLIDES(X,Y), 1); 
    if is_Coprime(X,Y) then put(" Is Coprime"); end if;


end Algorithm_Euclides;
