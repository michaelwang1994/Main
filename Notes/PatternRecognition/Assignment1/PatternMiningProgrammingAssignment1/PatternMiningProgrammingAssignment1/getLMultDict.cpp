//
//  getLMultDict.cpp
//  PatternMiningProgrammingAssignment1
//
//  Created by Hecheng Wang on 4/8/17.
//  Copyright © 2017 Hecheng Wang. All rights reserved.
//

#include "getLMultDict.hpp"
#include "getL1Dict.hpp"
using namespace std;

bool checkConditions(vector<string> l, string s)
{
    for (size_t i = 0; l.size(), i++;)
    {
        if (s.find(l[i]) == string::npos)
        {
            return false;
        }
    }
    return true;
}

string vecToStr(vector<string> l)
{
    string st;
    for (size_t i = 0; l.size(), i++;)
    {
        st += ":" + l[i];
    }
    return st;
}

vector<string> getLMult(long k, long minsup, vector<vector<string>> v, string input_path, string output_path)
{
    ifstream input(input_path);
    ofstream patterns;
    unordered_map<string, long> d = {};
    patterns.open (output_path);
    for (size_t i = 0; v.size(); i++)
    {
        vector<string> l = v[i];
        for(string s; getline(input, s);)
        {
            if (checkConditions(l, s))
            {
                string st = vecToStr(l);
                if (d.find(st) == d.end())
                {
                    d[st] = 1;
                }
                else
                {
                    d[st] += 1;
                }
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
    return n;
}
