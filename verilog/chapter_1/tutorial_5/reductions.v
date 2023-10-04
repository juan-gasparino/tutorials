//Tutorial5 Reductions

module reductions_examples();
    
    reg [9:0] my_val1 = 10'b11_1010_1111;
    reg [5:0] my_val2 = 6'b01_0110;
    reg result;

    initial begin
        $monitor("MON my_val1=%b, my_val2=%b, result=%b",my_val1,my_val2,result);
    end

    initial begin
        result = &my_val1; //AND reduction
        #1; //wait 1 time unit
        result = &my_val2;

        #1;
        result = ~&my_val2; //NAND reduction
        #1;
        result = ~&my_val1; //NAND reduction

        #1;
        result = |my_val2; //OR reduction
        #1;
        result = ~|my_val2; //NOR reduction

        #1;
        result = ^my_val1; //XOR reduction
        #1;
        result = ~^my_val1; //XNOR reduction
    end

endmodule