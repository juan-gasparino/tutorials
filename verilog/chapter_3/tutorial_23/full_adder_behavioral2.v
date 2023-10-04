module full_adder_behavioral2(input a, input b, input carry_in, output reg sum, output reg carry_out);

    //Behavioral style
    always @(*) begin
        {carry_out, sum} = a + b + carry_in;
    end

endmodule