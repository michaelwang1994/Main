//
//  main.cpp
//  PatternMiningProgrammingAssignment1
//
//  Created by Hecheng Wang on 4/6/17.
//  Copyright © 2017 Hecheng Wang. All rights reserved.
//


#include "getL1Dict.hpp"
#include "getLMultDict.hpp"
#include "getCombDict.hpp"
using namespace std;

int main() {
    string input_path = "/Users/hechengwang/Main/Notes/PatternRecognition/Assignment1/data.txt";
    string output_path = "/Users/hechengwang/Main/Notes/PatternRecognition/Assignment1/patterns.txt";
    long minsup = 771;

    vector<string> comboList = getL1(minsup, input_path, output_path);

    long k = 2;
    while (comboList.size() > 0)
    {
        vector<vector<string>> v = getCombs(k, comboList);
        comboList = getLMult(k, minsup, v, input_path, output_path);
        k++;
    }
    return 0;
}

