//Tutorial_9 Relational operators

module relational_operators();

    reg result;

    initial begin
        $monitor("MON result = %1b", result);
    end

    initial begin
        #1; result = 3 < 0;
        #1; result = 3 < 6'b00_1111; //3 < 157
        #1; result = 6 > 6;
        #1; result = 4'b1001 <= 4'b1010; //9 <= 107
        #1; result = 4'b100X > 4'b1010;
        #1; result = 99 >= 98;
    end

endmodule