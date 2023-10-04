//Tutorial_14

module precedence_operators();

    reg [3:0] a;
    integer b;

    initial begin
        #1; a = ~4'b1110 & |4'b1000; //unary excuted before bit-wise
        $display("a = %b", a);

        #1; a = ~4'b1100 & |4'b1000; //unary excuted before bit-wise
        $display("a = %b", a);

        #1; a = |4'b0100 & ~&4'b1011; //unary excuted before bit-wise
        $display("a = %b", a);

        #1; b = 2 * 5 << 2; // power excute before shift
        $display("b = %0d", b);

        #1; b = 2 < 4 && -33 > -34; //relational executed before logical
        $display("b = %0d", b);

        #1; b = 2 << 3 - 3; //arithmetic before shift
        $display("b = %0d", b);
    end

endmodule