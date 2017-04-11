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

vector<string> getLMult(long k, long minsup, vector<vector<string>> comboList, string inputPath, string outputPath);
#endif /* getLMultDict_hpp */
