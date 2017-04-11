//
//  l_1_dict.cpp
//  PatternMiningProgrammingAssignment1
//
//  Created by Hecheng Wang on 4/7/17.
//  Copyright © 2017 Hecheng Wang. All rights reserved.
//

#include "getL1Dict.hpp"

vector<string> getL1(long minsup, string inputPath, string outputPath) {
    ifstream input(inputPath);
    ofstream patterns;
    unordered_map<string, long> l1Dict = {};
    patterns.open (outputPath);
    for(string s; getline(input, s);) {
        if (s.size() > 0) {
            istringstream f(s);
            while (getline(f, s, ';')) {
                if (l1Dict.find(s) == l1Dict.end()) {
                    l1Dict[s] = 1;
                }
                else {
                    l1Dict[s] += 1;
                }
            }
        }
    }
    
    vector<string> freqL1List;
    for (auto it : l1Dict) {
        if (it.second >= minsup) {
            patterns << it.second << ":" << it.first << "\n";
            freqL1List.push_back(it.first);
        }
    }
    patterns.close();
    return freqL1List;
}
