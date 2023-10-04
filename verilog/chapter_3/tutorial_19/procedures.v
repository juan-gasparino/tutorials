//Tutorial 19 procedures

module procedures();

    reg [7:0] var1;
    reg [7:0] var2;
    wire [8:0] sum;
    reg [15:0] product;

    //All the procedures below are executed in parallel

    //continous assigment (Dataflow styles)
    assign sum = var1 + var2;

    //Behavioral Style - Controlled by the change of var1 or var2
    always @(var1 or var2) begin
        product = var1 * var2;
    end

    //Behavioral Style - Controlled by the change of var1
    always @(var1) begin
        $monitor("MON_VAR1: var1 = %d", var1); // var1 = 22
    end

    // Behavioral Style - controlled by the change of var1, var2, sum and product
    always @(*) begin
        $display("MON ALL: var1 = %d, var2 = %d, sum = %d, product = %d", var1,var2,sum,product);
    end

    initial begin
        #1; var1 = 10; var2 = 99;
        #1; var2 = 33;
        #1; var1 = var2 << 2;
        #1; var2 = var2 >> 3;
        #1; var2 = var2 + 1;
    end

endmodule