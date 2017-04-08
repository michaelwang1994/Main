//
//  getCombDict.cpp
//  PatternMiningProgrammingAssignment1
//
//  Created by Hecheng Wang on 4/7/17.
//  Copyright © 2017 Hecheng Wang. All rights reserved.
//

#include "getCombDict.hpp"
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

#include <iostream>
#include <vector>

using namespace std;

vector<string> combination;
vector<vector<string>> v;

void recursive(long offset, long k, vector<string> n) {
    if (k == 0)
    {
        
        v.push_back(combination);
        return;
    }
    for (size_t i = offset; i <= n.size() - k; ++i)
    {
        combination.push_back(n[i]);
        recursive(i+1, k-1, n);
        combination.pop_back();
    }
}

vector<vector<string>> getCombs(vector<string> n, long k) {
    recursive(0, k, n);
    
    return v;
}
