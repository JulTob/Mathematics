with Ada.Text_IO, Ada.Integer_Text_IO;
use  Ada.Text_IO, Ada.Integer_Text_IO;

procedure Fuzz is
	subtype Number -- is range <>;
		is Integer;
		-- renames Float;
	Zero 	: constant Number
			:= 0;

	One 	: constant Number
			:= 1;

	type Fuzzy is record
		Center: Number;
		Bound: Number;
		end record;


	function "+" (A : Number) return Fuzzy is
		begin
		return (zero, abs A);
		end "+";

	function "+" (A : Number; B : Fuzzy)
		return Fuzzy is
		C 	: Fuzzy := (zero, zero);
		begin
		C.Center := A + B.Center;
		C.Bound := abs B.Bound;
  		return C;
		end "+";

	function "+" (A : Fuzzy; B : Fuzzy)
		return Fuzzy is
		C 	: Fuzzy := (zero, zero);
		begin
		C.Center := A.Center + B.Center;
		C.Bound := abs A.Bound + abs B.Bound;
  		return C;
		end "+";

	function "*" (A : Fuzzy; B : Fuzzy)
		return Fuzzy is
		C 	: Fuzzy := (zero, zero);
		begin
		C.Center := A.Center * B.Center;
		C.Bound :=
			abs (A.Center * B.Bound)
			+
			abs (A.Bound * B.Center)
			+
			abs (A.Bound * B.Bound)
			;
  		return C;
		end "*";



	x: Fuzzy := 100 + (+2);
	y: Fuzzy := 10 + (+1);
	z: Fuzzy := x*y + x;
	begin
	Put(z.Center);
	Put(z.Bound);
	New_Line;
	end Fuzz;
