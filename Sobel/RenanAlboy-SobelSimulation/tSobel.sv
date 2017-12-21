`timescale 1ns / 1ns

module tSobel();

	reg clock, control;
	reg  [9:0] pin;
	wire [9:0] pout;
	logic [31:0] i;

	logic [7:0] RAM[307199:0];
	logic [7:0] RAM_out[309000:0];
	
	Sobel dut (clock, pin, pout, control);
	
	initial 
	begin
		clock = 0;
		control = 1;
		pin = 10'b0;
		$readmemh("resultado.hex", RAM);
		i = 0;
	end
	
	always
	begin
		#1 clock = !clock;
	end
	 
	always @(posedge clock)
	begin
		if(i < 307200)
			begin
				pin = {2'b0, RAM[i]};
				RAM_out[i] = pout;
			end
		else if(i < 308489)
			begin
				pin = {2'b0, 8'b0};
				RAM_out[i] = pout;
			end
		else
			begin
				$writememh("arq_out.hex", RAM_out);
				$stop;
			end
	end
	
	always @(negedge clock) 
   begin
		i = i + 1;
	end

	// initial
    // $monitor($stime,, clock,, control,, pin,, pout);
	
endmodule