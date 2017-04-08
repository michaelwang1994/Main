//
//  l_1_dict.cpp
//  PatternMiningProgrammingAssignment1
//
//  Created by Hecheng Wang on 4/7/17.
//  Copyright © 2017 Hecheng Wang. All rights reserved.
//

#include "getL1Dict.hpp"
using namespace std;

vector<string> getL1(long minsup, string input_path, string output_path)
{
    ifstream input(input_path);
    ofstream patterns;
    unordered_map<string, long> d = {};
    patterns.open (output_path);
    for(string s; getline(input, s);)
    {
        istringstream f(s);
        while (getline(f, s, ';'))
        {
            if (d.find(s) == d.end())
            {
                d[s] = 1;
            }
            else
            {
                d[s] += 1;
            }
        }
    }
    
    vector<string> n;
    for (auto it : d)
    {
        if (it.second > minsup)
        {
            patterns << it.second << ":" << it.first << "\n";
            n.push_back(it.first);
        }
    }
    patterns.close();
    return n;
}
