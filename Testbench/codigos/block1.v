//Blocado sem inversão
module block1 (x1, x2, x3, Clock, f, g);
    
    input x1, x2, x3, Clock;
    output f, g;
    reg f, g;
    
    always @(posedge Clock)
    begin
      f = x1 & x2; 
      g = f | x3;
    end  
endmodule