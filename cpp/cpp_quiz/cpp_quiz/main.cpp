//
//  main.cpp
//  cpp_learn
//
//  Created by Hecheng Wang on 11/13/16.
//  Copyright © 2016 Hecheng Wang. All rights reserved.
//


#include <iostream>

//A function named “readNumber” should be used to get (and return) a single integer from the user.
int readNumber()
{
    int x;
    std::cout << "Enter a number: " << std::endl;
    std::cin >> x;
    return x;
}

//A function named “writeAnswer” should be used to output the answer. This function should take a single parameter and have no return value.
void writeAnswer(int x)
{
    std::cout << "Sum is equal to: " << x << std::endl;
}

int main()
{
    int x;
    int y;
    int z;
    x = readNumber();
    y = readNumber();
    z = x + y;
    writeAnswer(z);
    
    return 0;
}