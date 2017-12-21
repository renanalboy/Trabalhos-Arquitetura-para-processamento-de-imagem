`timescale 1ns / 1ns

module testbench;

reg clk, reset;
wire [3:0] f;
wire [3:0] g;
reg  [2:0] x;

block1   dutb1  (x[0], x[1], x[2], clk, f[0], g[0]);
block2   dutb2  (x[0], x[1], x[2], clk, f[1], g[1]);
noblock1 dutnb1 (x[0], x[1], x[2], clk, f[2], g[2]);
noblock2 dutnb2 (x[0], x[1], x[2], clk, f[3], g[3]);

initial // Clock generator
  begin
    clk = 0;
    forever #10 clk = !clk;
  end

initial	// Test stimulus
  begin
    reset = 0;
    #5 reset = 1;
    #4 reset = 0;
  end

initial	// Test stimulus
  begin
    x = 0; //Coloca todas as entradas em nivel baixo
	 #25 //Incicia um loopinfinito aguardando um ciclo de clock
	 forever #20 x = x + 1; //Varre entradas posséveis
  end
  
initial
    $monitor($stime,, clk,, f[0],, f[1],, f[2],, f[3],, g[0],, g[1],, g[2],, g[3]);
    
endmodule


