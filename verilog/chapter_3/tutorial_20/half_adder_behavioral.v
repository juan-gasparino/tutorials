//Tutorial 19 half_adder_behavioral

module half_adder_behavioral(input a, input b, output reg sum, output reg carry);

    //Behavioral style
    always @(a or b) begin
        sum = a ^ b; // a XOR begin
        carry = a & b; // a AND b XOR begin
    end

endmodule