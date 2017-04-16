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

vector<string> combination;
vector<vector<string>> comboList;

vector<string> getFrequentList(long k, vector<string> combos) {
    vector<string> freqN;
    unordered_map<string, long> nDict;
    if (k == 2) {
        return combos;
    }
    else {
        for (auto category: combos) {
            if (category.size() > 0) {
                istringstream f(category);
                while (getline(f, category, ';')) {
                    if (nDict.find(category) == nDict.end()) {
                        nDict[category] = 1;
                    }
                    else {
                        nDict[category] += 1;
                    }
                }
            }
        }
    }
    for (auto it : nDict) {
        if (it.second + 1 >= k) {
            freqN.push_back(it.first);
        }
    }
    return freqN;
}

void printCombs(vector<string> combo) {
    cout << "Combination: ";
    for (auto category: combo) {
        cout << category << ", ";
    }
    cout << endl;
}

void printCombsFromList(vector<vector<string>> comboList) {
    for (auto combo: comboList) {
        cout << "Combination: ";
        for (auto category: combo) {
            cout << category << ", ";
        }
        cout << endl;
    }
}

void recursive(long offset, long k, vector<string> freqN) {
    if (k == 0) {
        comboList.push_back(combination);
        return;
    }
    for (size_t i = offset; i <= freqN.size() - k; ++i) {
        combination.push_back(freqN[i]);
        recursive(i+1, k-1, freqN);
        combination.pop_back();
    }
}

vector<vector<string>> getCombs(long k, vector<string> combos) {
    comboList = {};
    vector<string> freqN = getFrequentList(k, combos);
    cout << "Creating Combinations From:" << endl;
    printCombs(freqN);
    recursive(0, k, freqN);
    cout << k << "-length combos: " << endl;
    printCombsFromList(comboList);
    cout << comboList.size() << endl;
    return comboList;
}

#endif /* getCombDict_hpp */
