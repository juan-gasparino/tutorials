//Tutorial 18 half_adder_dataflow

module half_adder_dataflow(input a, input b, output sum, output carry);

    //Dataflow uses continous assigments
    assign sum = a ^ b; // a XOR b
    assign carry = a & b; // a AND b

endmodule