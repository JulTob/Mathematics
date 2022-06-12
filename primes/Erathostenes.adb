with Ada.Text_IO; use Ada.Text_IO;
With Ada.Integer_Text_IO; use Ada.Integer_Text_IO;

procedure Erathostenes is --Erathostenes Sieve

type List is array (Integer range <>)
	of Boolean;

function Erathostenes_Sieve(N: in Integer)
	return List is
	Sieve: List(1..N) := (others => True);
	X: Integer := 1;
		begin
		for M in 2..N loop
			X := 2;
			Checks: while X*M < N loop
				Sieve(X*M):= False;
				X:= X+1;
				end loop Checks;
			end loop;
		return Sieve;
		end Erathostenes_Sieve;

N: Integer := 1000;
Sieve: List := Erathostenes_Sieve(N);

begin

for M in 1..N loop
	if Sieve(M) then
		Put(M,1); New_Line;
		else
		Put("X "); New_Line;
		end if;
	end loop;



end Erathostenes;
