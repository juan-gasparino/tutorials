module testbench();

    reg a;
    reg b;
    reg c_in;
    wire sum;
    wire c_out;

    full_adder_structural FULL_ADD(.a(a),.b(b),.carry_in(c_in),.sum(sum),.carry_out(c_out));

    initial begin
        $monitor("a=%b, b=%b, carry_in=%b, sum=%b, carry_out=%b", a,b,c_in,sum,c_out);
    end

    initial begin
        #1; a = 0; b = 0; c_in = 0;
        #1; a = 0; b = 0; c_in = 1;
        #1; a = 0; b = 1; c_in = 0;
        #1; a = 0; b = 1; c_in = 1;
        #1; a = 1; b = 0; c_in = 0;
        #1; a = 1; b = 0; c_in = 1;
        #1; a = 1; b = 1; c_in = 0;
        #1; a = 1; b = 0; c_in = 1;
    end

endmodule