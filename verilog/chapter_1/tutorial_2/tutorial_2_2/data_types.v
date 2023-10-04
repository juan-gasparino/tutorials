//Tutorial_2_2 Language data types
//data types are used to describe a harware circuit

module multiple_procedure();

    reg x = 1'b0; //1 bit variable with the value 0
    reg y = 1'b1; //1 bit variable with the value 1
    reg z ; //store result from x and y

    //A procedure Example
    always @(z) begin
        $display("\n\t x=%b, y=%b, z=%b", x,y,z);
    end

    //Another procedure Examples
    initial begin
        #2; //wait 2 times unit
        z = x^y; //bit-wise XOR between the 1 bit variables x and y
        #10; //wait 10 times units
        y = 0; //change the value of y
        z = x | y; // bit-wise OR between the 1 bit variables x and y
        #10; //wait 10
        z = ~z; //bit-wise NOT of the variable z
        #10; //wait 10
    end

endmodule