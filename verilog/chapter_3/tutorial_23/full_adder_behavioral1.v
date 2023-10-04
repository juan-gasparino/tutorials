module full_adder_behavioral1(input a, input b, input carry_in, output reg sum, output reg carry_out);

    //Behavioral style
    always @(a or b or carry_in) begin
        sum = a ^ b ^ carry_in;
        carry_out = (a & b) | (carry_in & (a ^ b));
    end

endmodule