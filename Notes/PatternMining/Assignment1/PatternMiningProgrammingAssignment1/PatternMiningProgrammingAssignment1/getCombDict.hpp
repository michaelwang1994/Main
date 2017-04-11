//
//  getCombDict.hpp
//  PatternMiningProgrammingAssignment1
//
//  Created by Hecheng Wang on 4/7/17.
//  Copyright © 2017 Hecheng Wang. All rights reserved.
//

#ifndef getCombDict_hpp
#define getCombDict_hpp
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <iterator>
using namespace std;

vector<vector<string>> getCombs(long k, vector<string> n);
void printCombs(vector<string> combo);
void printCombsFromList(vector<vector<string>> comboList);

#endif /* getCombDict_hpp */
