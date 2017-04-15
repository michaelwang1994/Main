//
//  getLMultDict.hpp
//  PatternMiningProgrammingAssignment1
//
//  Created by Hecheng Wang on 4/8/17.
//  Copyright © 2017 Hecheng Wang. All rights reserved.
//

#ifndef getLMultDict_hpp
#define getLMultDict_hpp
#include "getL1Dict.hpp"
#include "getCombDict.hpp"
#include <stdio.h>

bool checkConditions(vector<string> combo, string txtLine) {
    for (auto category: combo) {
        if (txtLine.find(category) == string::npos) {
            return false;
        }
    }
    return true;
}

string vecToStr(vector<string> l) {
    string comboStr;
    for (auto value: l) {
        comboStr += value + ";";
    }
    return comboStr.substr(0, comboStr.size()-1);
}

vector<string> getLMult(long k, long minsup, vector<vector<string>> comboList, string inputPath, string outputPath)
{
    ofstream patterns;
    unordered_map<string, long> comboDict = {};
    patterns.open (outputPath, ios_base::app);
    for (auto combo: comboList) {
        string comboStr = vecToStr(combo);
        cout << "Checking for: " << comboStr << endl;
        ifstream input(inputPath);
        for(string txtLine; getline(input, txtLine);) {
            if (checkConditions(combo, txtLine)) {
                if (comboDict.find(comboStr) == comboDict.end()) {
                    comboDict[comboStr] = 1;
                }
                else {
                    comboDict[comboStr] += 1;
                }
            }
        }
    }
    vector<string> freqComboList;
    for (auto it : comboDict) {
        if (it.second >= minsup) {
            string supCat = to_string(it.second) + ":" + it.first;
            patterns << supCat << "\n";
            cout << "Frequent Itemset: " << supCat << endl;
            freqComboList.push_back(it.first);
        }
    }
    patterns.close();
    return freqComboList;
}
#endif /* getLMultDict_hpp */
