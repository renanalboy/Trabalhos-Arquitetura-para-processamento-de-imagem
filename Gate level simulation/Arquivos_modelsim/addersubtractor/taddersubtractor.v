`timescale 10ps / 10ps

module taddersubtractor;

	parameter	n = 5;
	reg 		[n-1:0] A, B;
	reg 		Clock, Reset, Sel, AddSub;
	wire 		[n-1:0] Z;
	wire 		Overflow;

//module addersubtractor (A, B, Clock, Reset, Sel, AddSub, Z, Overflow);
addersubtractor dut (A, B, Clock, Reset, Sel, AddSub, Z, Overflow);

initial // Clock generator
  begin
    Clock = 0;
    forever #225 Clock = !Clock;
  end

initial	// Test stimulus
  begin
    Reset = 1;
    #400 Reset = 0;
    #500 Reset = 1;
	 B = 1;
	 A = 0;
	 AddSub = 0;
	 Sel = 1;
	 
  end
  
initial
    $monitor($stime,, A,, B,, Clock,, Reset,, Sel,, AddSub,, Z,, Overflow);
    
endmodule


