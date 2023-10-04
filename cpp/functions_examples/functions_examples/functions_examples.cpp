#include <iostream>

// declaring a function
void greet()
{
  std::cout << "Hello there!" << std::endl;
}

// display a number
void displayNum(int n1, float n2)
{
  std::cout << "The int number is " << n1 << std::endl;
  std::cout << "The double number is " << n2 << std::endl;
}

// Add
int add(int a, int b)
{
  return (a + b);
}

// function with 2 parameters
void display(int var1, float var2)
{
  std::cout << "Integer number: " << var1 << std::endl;
  std::cout << "Float number: " << var2 << std::endl;
}

// function with float type single parameter
void display(float var)
{
  std::cout << "Float number: " << var << std::endl;
}

// function with int type single parameter
void display(int var)
{
  std::cout << "Integer number: " << var << std::endl;
}

// Function Overloading
void display(char c = '+', int count = 10)
{
  for (int i = 1; i <= count; ++i)
  {
    std::cout << c;
  }
  std::cout << std::endl;
}

int main()
{

  // calling the function
  int a = 5;
  float b = 3.5;
  int result = 0;
  greet();
  displayNum(a, b);
  result = add(5, 3);
  std::cout << "Result: " << result << std::endl;

  display(a);
  display(b);
  display(a, b);
  display('A', 10);

  return 0;
}