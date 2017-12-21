`timescale 1ns / 1ns

module tSobel;

	parameter SIZE_X = 640;

	reg clock, control;
	reg  [9:0] pin;
	wire [9:0] pout;
	integer i;

	
	Sobel dut (clock, pin, pout, control);
	
	initial 
	begin
		clock = 0;
		i = 0;
		control = 1;
		//forever clock = !clock;
	end
	
	always
		#1 clock = !clock;
	
	always@(posedge clock)
	begin
		i = i+1;
		if(i < (SIZE_X/2))
			pin = 'b0;
		else
			pin = 'b1;
		if(i == SIZE_X)
			i = 0;
	end
	
	//initial begin
		//$readmemh("file.hex", image);
		/*for (i = 0; i < MAX_SIZE/4; i = i + 1) begin
			image_32[i] = ({24'b0, image_8[i*4]} << 24) | ({24'b0, image_8[i*4 + 1]} << 16) | ({24'b0, image_8[i*4 + 2]} << 8) | (image_8[i*4 + 3]);
		end*/
	//end
	
	initial
    $monitor($stime,, clock,, control,, pin,, pout);
	
endmodule
	
	