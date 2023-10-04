//Tutorial_6 Logicals operators

module logical_operators();

    reg [2:0] my_val1 = 3'b111; //3bit variable
    reg [3:0] my_val2 = 4'b0000; //4bit variables
    reg result;

    //Procedure show values per click
    initial begin
        $monitor("MON my_val1=%b, my_val2=%b, result=%b", my_val1, my_val2, result);
    end

    //Procedure change values 
    initial begin
        result = !my_val1; //Logical NOT
        #1; //wait 1 tick
        result = !my_val2; //Logical NOT

        #1;
        result = my_val1 && my_val2; //Logical AND

        #1;
        result = my_val1 || my_val2;

        #1;
        my_val1 = 3'bz0X; //Add some unknown bits
        result = !my_val1;

        #1;
        result = my_val1 || my_val2;

        #1;
        result = my_val1 && my_val2;
    end

endmodule