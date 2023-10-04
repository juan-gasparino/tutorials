//Tutorial4 Operators

module operators_examples();

    reg [5:0] x = 0; //&bit variable
    reg [5:0] y = 0; //&bit variable
    reg [5:0] result = 0; //&bit variable

    //Procedure used to continously monitor x, y and result
    initial begin
        $monitor("MON x=%b, y=%b, result=%b", x, y, result);
    end

    //Procedure to generate stimulus
    initial begin
        #1; //wait some time between examples
        x = 6'b00_0101;
        y = 6'b11_0001;
        result = x & y; //AND Gate

        #1; //Use the same values for x and y from above (reg stores the value)
        result = ~(x & y); //NAND Gate

        #1;
        x = 6'b10_0101;
        y = 6'b01_1011;
        result = x | y; //OR Gate

        #1;
        result = ~(x | y); //NOR Gate

        #1;
        x = 6'b01_0110;
        y = 6'b01_1011;
        result = x ^ y; //XOR Gate

        #1;
        result = x ^ ~y; //NXOR used to check if x = y

        #1;
        x = y; //This should make all bits 1
        result = ~(x ^ y); //NXOR
    end

endmodule