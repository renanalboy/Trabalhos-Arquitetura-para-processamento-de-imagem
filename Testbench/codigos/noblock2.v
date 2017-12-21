//Não blocado com inversão
module noblock2 (x1, x2, x3, Clock, f, g);
    
    input x1, x2, x3, Clock;
    output f, g;
    reg f, g;
    
    always @(posedge Clock)
	begin
	  g <= f | x3;
      f <= x1 & x2; 
    end  
endmodule