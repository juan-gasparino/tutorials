//Tutorial_2_3 Literal values
//use to represent data in specific format

module literal_values();

    reg [7:0] my_var;

    initial begin
        my_var = 8'd137; //137 in decimal
        $display("\n\t my_var = %d", my_var);

        my_var = 8'h89; //137 in hexa
        $display("\n\t my_var = %x", my_var);

        my_var = 8'b1000_1001; //137 in binary
        $display("\n\t my_var = %b", my_var);

        my_var = 8'o2110; //137 in octal
        $display("\n\t my_var = %o", my_var);

        my_var = 8'hZ1; //137 zzzz_0001
        $display("\n\t my_var = %b", my_var);

        my_var = 1'b1; //8bi variable gets 1 bit values
        $display("\n\t my_var = %b", my_var);

        my_var = 12'b1111_1111_0000; //8 bit variable gets 12bits values
        $display("\n\t my_var = %b", my_var);
    end

endmodule