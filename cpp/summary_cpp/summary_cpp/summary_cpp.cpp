#include <iostream>

void primitivesDataTypes()
{
  int a = 0;
  float b = 13.754;
  double c = 15.54; // double precision of float
  bool d = true;
  char e = 'A';
  char f[] = "Hello world";
  wchar_t g = L'ם'; // storing Hebrew character  similar to the char data type, except its size is 2 bytes instead of 1;

  // We can further modify some of the fundamental data types by using type modifiers
  // signed
  // unsigned
  // short
  // long

  std::cout << "int: " << a << std::endl;
  std::cout << "float: " << b << std::endl;
  std::cout << "double: " << c << std::endl;
  std::cout << "bool: " << d << std::endl;
  std::cout << "char: " << e << std::endl;
  std::cout << "char[]: " << f << std::endl;
  std::cout << "wchar_t: " << g << std::endl;

  // const cant change the value the name goes in capital and snaked

  const int LIGHT_SPEED = 299792458;

  std::cout << "light speed: " << LIGHT_SPEED << std::endl;
}

void convertionExamples()
{
  // from int to double (implicit)
  int numIntA = 9;
  double numDoubleA;
  numDoubleA = numIntA;

  std::cout << "\nFrom Int to Double" << std::endl;
  std::cout << "numIntA = " << numIntA << std::endl;
  std::cout << "numDoubleA = " << numDoubleA << std::endl;

  // from double to int (implicit)

  int numIntB;
  double numDoubleB = 9.99;
  numIntB = numDoubleB;

  std::cout << "\nFrom Double to Int" << std::endl;
  std::cout << "numDoubleB = " << numDoubleB << std::endl;
  std::cout << "numIntB = " << numIntB << std::endl;

  // initializing int variable C-style Type Casting
  int numIntC = 26;
  double numDoubleC;
  numDoubleC = (double)numIntC;

  std::cout << "\nC-style Type Casting" << std::endl;
  std::cout << "numDoubleC = " << numDoubleC << std::endl;

  // initializing int variable Function-style Casting
  int numIntD = 34;
  double numDoubleD;
  numDoubleD = double(numIntD);

  std::cout << "\nFunction-style Casting" << std::endl;
  std::cout << "numDoubleD = " << numDoubleD << "\n"
            << std::endl;
}

void arithmeticOperators()
{

  int a, b;
  a = 7;
  b = 2;

  std::cout << "Arithmetic Operators\n"
            << std::endl;
  // printing the sum of a and b
  std::cout << "a + b = " << (a + b) << std::endl;
  // printing the difference of a and b
  std::cout << "a - b = " << (a - b) << std::endl;
  // printing the product of a and b
  std::cout << "a * b = " << (a * b) << std::endl;
  // printing the division of a by b
  std::cout << "a / b = " << (a / b) << std::endl;
  // printing the modulo of a by b
  std::cout << "a % b = " << (a % b) << std::endl;
  std::cout << "\n"
            << std::endl;
}

void incrementandDecrementOperators()
{

  int a = 10, b = 100, result_a, result_b;
  // incrementing a by 1 and storing the result in result_a
  std::cout << "Increment and decrement operators\n"
            << std::endl;
  std::cout << "++a" << std::endl;
  std::cout << "a = " << a << std::endl;
  result_a = ++a;
  std::cout << "result_a = " << result_a << std::endl;
  // decrementing b by 1 and storing the result in result_b
  std::cout << "--b" << std::endl;
  std::cout << "b = " << b << std::endl;
  result_b = --b;
  std::cout << "result_b = " << result_b << std::endl;
  std::cout << "\n"
            << std::endl;
}

void assignmentOperators()
{

  int a, b;

  // 2 is assigned to a
  a = 2;
  // 7 is assigned to b
  b = 7;

  std::cout << "Assignment Operators\n"
            << std::endl;

  std::cout << "a = " << a << std::endl;
  std::cout << "b = " << b << std::endl;
  std::cout << "\nAfter a += b;" << std::endl;

  // assigning the sum of a and b to a
  a += b; // a = a +b
  std::cout << "a = " << a << std::endl;
}

void relationalOperators()
{

  int a, b;
  a = 3;
  b = 5;
  bool result;

  std::cout << "Relational Operators\n"
            << std::endl;

  result = (a == b); // false
  std::cout << "3 == 5 is " << result << std::endl;

  result = (a != b); // true
  std::cout << "3 != 5 is " << result << std::endl;

  result = a > b; // false
  std::cout << "3 > 5 is " << result << std::endl;

  result = a < b; // true
  std::cout << "3 < 5 is " << result << std::endl;

  result = a >= b; // false
  std::cout << "3 >= 5 is " << result << std::endl;

  result = a <= b; // true
  std::cout << "3 <= 5 is " << result << std::endl;
}

void logicalOperators()
{

  bool result;

  std::cout << "Logical Operators\n"
            << std::endl;

  result = (3 != 5) && (3 < 5); // true
  std::cout << "(3 != 5) && (3 < 5) is " << result << std::endl;

  result = (3 == 5) && (3 < 5); // false
  std::cout << "(3 == 5) && (3 < 5) is " << result << std::endl;

  result = (3 == 5) && (3 > 5); // false
  std::cout << "(3 == 5) && (3 > 5) is " << result << std::endl;

  result = (3 != 5) || (3 < 5); // true
  std::cout << "(3 != 5) || (3 < 5) is " << result << std::endl;

  result = (3 != 5) || (3 > 5); // true
  std::cout << "(3 != 5) || (3 > 5) is " << result << std::endl;

  result = (3 == 5) || (3 > 5); // false
  std::cout << "(3 == 5) || (3 > 5) is " << result << std::endl;

  result = !(5 == 2); // true
  std::cout << "!(5 == 2) is " << result << std::endl;

  result = !(5 == 5); // false
  std::cout << "!(5 == 5) is " << result << std::endl;
}

void bitwiseOperators()
{

  // declare variables
  int a = 12, b = 25;

  std::cout << "AND Operators" << std::endl;
  std::cout << "a = " << a << std::endl;
  std::cout << "b = " << b << std::endl;
  std::cout << "a & b = " << (a & b) << std::endl;
  std::cout << "\n"
            << std::endl;

  int c = 12, d = 25;
  std::cout << "OR Operators" << std::endl;
  std::cout << "c = " << c << std::endl;
  std::cout << "d = " << d << std::endl;
  std::cout << "c | d = " << (c | d) << std::endl;
  std::cout << "\n"
            << std::endl;

  int e = 12, f = 25;
  std::cout << "XOR Operators" << std::endl;
  std::cout << "e = " << e << std::endl;
  std::cout << "f = " << f << std::endl;
  std::cout << "e ^ f = " << (e ^ f) << std::endl;
  std::cout << "\n"
            << std::endl;

  int num1 = 35;
  int num2 = -150;
  std::cout << "Bitwise Complement" << std::endl;
  std::cout << "~(" << num1 << ") = " << (~num1) << std::endl;
  std::cout << "~(" << num2 << ") = " << (~num2) << std::endl;
  std::cout << "\n"
            << std::endl;

  // declaring two integer variables
  int num = 212, i;

  std::cout << "Shift Right:" << std::endl;

  // Using for loop for shifting num right from 0 bit to 3 bits
  for (i = 0; i < 4; i++)
  {
    std::cout << "212 >> " << i << " = " << (212 >> i) << std::endl;
  }

  std::cout << "\nShift Left:" << std::endl;

  // Using for loop for shifting num left from 0 bit to 3 bits
  for (i = 0; i < 4; i++)
  {
    std::cout << "212 << " << i << " = " << (212 << i) << std::endl;
  }
}

void ifelseExamples()
{

  int num;

  std::cout << "Enter an integer: ";
  std::cin >> num;

  // outer if condition
  if (num != 0)
  {

    // inner if condition
    if (num > 0)
    {
      std::cout << "The number is positive." << std::endl;
    }
    // inner else condition
    else
    {
      std::cout << "The number is negative." << std::endl;
    }
  }
  // outer else condition
  else
  {
    std::cout << "The number is 0 and it is neither positive nor negative." << std::endl;
  }

  std::cout << "This line is always printed." << std::endl;
}

void loopsFor()
{

  std::cout << "Printing Numbers From 1 to 5\n";
  for (int i = 1; i <= 5; ++i)
  {
    std::cout << i << " ";
  }

  std::cout << "Range Based for Loop\n";
  int num_array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  for (int n : num_array)
  {
    std::cout << n << " ";
  }

  int i = 1;

  // do...while loop from 1 to 5
  std::cout << "Do while\n";
  do
  {
    std::cout << i << " ";
    ++i;
  } while (i <= 5);
}

void loopsForBreak()
{

  std::cout << "Break for\n";
  for (int i = 1; i <= 5; i++)
  {
    // break condition
    if (i == 3)
    {
      break;
    }
    std::cout << i << std::endl;
  }

  std::cout << "Break with while loop\n";
  int number;
  int sum = 0;
  while (true)
  {
    // take input from the user
    std::cout << "Enter a number: ";
    std::cin >> number;

    // break condition
    if (number < 0)
    {
      break;
    }

    // add all positive numbers
    sum += number;
  }

  // display the sum
  std::cout << "The sum is " << sum << std::endl;
}

void loopsForContinue()
{

  std::cout << "Continue for\n";
  for (int i = 1; i <= 5; i++)
  {
    // condition to continue
    if (i == 3)
    {
      continue;
    }

    std::cout << i << std::endl;
  }

  std::cout << "Continue with while loop\n";
  int sum = 0;
  int number = 0;

  while (number >= 0)
  {
    // add all positive numbers
    sum += number;

    // take input from the user
    std::cout << "Enter a number: ";
    std::cin >> number;

    // continue condition
    if (number > 50)
    {
      std::cout << "The number is greater than 50 and won't be calculated.\n"
                << std::endl;
      number = 0; // the value of number is made 0 again
      continue;
    }
  }

  // display the sum
  std::cout << "The sum is " << sum << std::endl;
}

void switchStatementExample()
{

  char oper;
  float num1, num2;
  std::cout << "Enter an operator (+, -, *, /): ";
  std::cin >> oper;
  std::cout << "Enter two numbers: " << std::endl;
  std::cin >> num1 >> num2;

  switch (oper)
  {
  case '+':
    std::cout << num1 << " + " << num2 << " = " << num1 + num2;
    break;
  case '-':
    std::cout << num1 << " - " << num2 << " = " << num1 - num2;
    break;
  case '*':
    std::cout << num1 << " * " << num2 << " = " << num1 * num2;
    break;
  case '/':
    std::cout << num1 << " / " << num2 << " = " << num1 / num2;
    break;
  default:
    // operator is doesn't match any case constant (+, -, *, /)
    std::cout << "Error! The operator is not correct";
    break;
  }
}

void gotoStatement()
{

  float num, average, sum = 0.0;
  int i, n;

  std::cout << "Maximum number of inputs: ";
  std::cin >> n;

  for (i = 1; i <= n; ++i)
  {
    std::cout << "Enter n" << i << ": ";
    std::cin >> num;

    if (num < 0.0)
    {
      // Control of the program move to jump:
      goto jump;
    }
    sum += num;
  }

jump:
  average = sum / (i - 1);
  std::cout << "\nAverage = " << average;
}

int main()
{
  std::cout << "Summary cpp" << std::endl;
  // primitivesDataTypes();
  // convertionExamples();
  // arithmeticOperators();
  // incrementandDecrementOperators();
  // assignmentOperators();
  // relationalOperators();
  // bitwiseOperators();
  // ifelseExamples();
  // loopsFor();
  // loopsForBreak();
  // loopsForContinue();
  // gotoStatement();
  return 0;
}