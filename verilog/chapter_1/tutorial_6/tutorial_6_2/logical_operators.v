//Tutorial_6 Logicals operators

module logical_operators();

    reg [2:0] my_val1 = 3'b111; //3bit variable
    reg [3:0] my_val2 = 4'b0000; //4bit variables
    reg result;

    //Procedure
    // check if my_val == 0
    initial begin
        #1;
        if(!my_val1) begin
            $display("GREAT my_val1=%b",my_val1);
        end
        else begin
            $display(":( my_val1 is not 0 is my_val1=%b",my_val1);
        end

        #1;
        if(!my_val2) begin
            $display("GREAT my_val2=%b", my_val2);
        end
        else begin
            $display(":( my_val2 is not 0 is my_val2=%b",my_val2);
        end

        #1;
        if(my_val1 && (!my_val2)) begin
            $display("GREAT!!! my_val1=%b my_val2=%b",my_val1,my_val2);
        end
        else begin
            $display(":( my_val1=%b and my_val2=%b are not 0",my_val1,my_val2);
        end

        #1;
        while(my_val2 < 3) begin
            $display("While loop my_val2=%d", my_val2);
            my_val2 = my_val2 + 1; //increment +1 my_val2
        end
    end

endmodule