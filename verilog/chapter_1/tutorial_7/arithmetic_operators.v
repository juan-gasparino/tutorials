//Tutorial7 Arithmetics operators

module arithmetic_operators();

    integer a = 2;
    integer b = 3;
    integer result;

    initial begin
        $monitor("MON a = %d, b = %d, result = %d", a, b, result);
    end

    initial begin
        result = a ** b; //exponential
        #1;
        result = b ** a;

        #1;
        a = 177;
        b = 12;
        result = a * b; //multiplication
	#1;
	result = b * a;

        #1;
        a = 199;
        b = 19;
        result = a / b;

        #1;
        a = 199;
        b = 19;
        result = a % b; //remainder

        #1;
        a = 199;
        b = -19;
        result = a % b; //negative remainder

        #1;
        a = 4199;
        b = -2319;
        result = a + b;

        #1;
        a = 19234;
        b = -16;
        result = a - b;

        //always use parenthesys when complex operations are performed
        #1;
        a = 919234;
        b = 13;
        result = a - (b*(2**15));
    end

endmodule