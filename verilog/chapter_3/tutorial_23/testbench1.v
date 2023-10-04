module testbench1();

    reg a;
    reg b;
    reg c_in;
    wire sum;
    wire c_out;


    full_adder_behavioral1 FULL_ADD(.a(a),.b(b), .carry_in(c_in), .sum(sum), .carry_out(c_out));

    initial begin
        $monitor("MON TESTBENCH1 a=%b,b=%b,c_in=%b,sum=%b,c_out=%b",a,b,c_in,sum,c_out);
    end

    initial begin
        #1; a=0; b=0; c_in=0;
        #1; a=0; b=0; c_in=1;
        #1; a=0; b=1; c_in=0;
        #1; a=0; b=1; c_in=1;
        #1; a=1; b=0; c_in=0;
        #1; a=1; b=0; c_in=1;
        #1; a=1; b=1; c_in=0;
        #1; a=1; b=1; c_in=1;
    end

endmodule