//
//  main.cpp
//  PatternMiningProgrammingAssignment1
//
//  Created by Hecheng Wang on 4/6/17.
//  Copyright © 2017 Hecheng Wang. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <unordered_map>
#include "getL1Dict.hpp"
#include "getCombDict.hpp"
using namespace std;

int main() {
    string input_path = "/Users/hechengwang/Main/Notes/PatternRecognition/Assignment1/data.txt";
    string output_path = "/Users/hechengwang/Main/Notes/PatternRecognition/Assignment1/patterns.txt";
    long minsup = 771;
    // get l_1 dict
    vector<string> n = getL1(minsup, input_path, output_path);

    long k = 2;
    while (n.size() > 0)
    {
        vector<vector<string>> v = getCombs(n, k);
        n = getFreqs(v);
        k++;
    }
    
    
    return 0;
    // iterate through l_1 dict DONE
    // while len(combHash) > 0:
    //  combList = createCombs(combHash.keys(), k) DONE
    //  combHash = checkFrequent(combList)
    //  k += 1
}

