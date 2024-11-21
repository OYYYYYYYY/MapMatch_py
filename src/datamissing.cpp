#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <cstring>
#include <cmath>
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <random>

using namespace std;



int main(int argc, char **argv){



    ifstream inFile_gps(argv[1], ios::in);
    string lineStr;
    vector<string> item;
    uint nnz = 0;

    double rate = double(argv[2]);

    getline(inFile_gps, lineStr);
    while(getline(inFile_gps, lineStr)){
        item.push_back(lineStr);
        nnz++;
    }
    cout<<"nnz is: "<<nnz<<endl;

    // Data load

    uint nmodes = 3;
    uint *ndims = nullptr;
    ndims = (uint*)malloc(sizeof(uint) * nmodes);
    uint inds0 = nullptr;
    inds0 = (uint*)malloc(sizeof(uint) * ndims[0]);
    uint inds1 = nullptr;
    inds1 = (uint*)malloc(sizeof(uint) * ndims[1]);
    uint inds2 = nullptr;
    inds2 = (uint*)malloc(sizeof(uint) * ndims[2]);
    double *value = nullptr;
    value = (double*)malloc(sizeof(double) * nnz);

    uint round = 0;
    for (auto it = item.begin(); it != item.end(); it++){
        string str;
        istringstream istr(*it);
        getline(istr, str, ',');
        // cout << str << ' ';
        inds0[round] = atoi(str.c_str());

        getline(istr, str, ',');
        // cout << str << ' ';
        inds1[round] = atoi(str.c_str());

        getline(istr, str, ',');
        // cout << str <<endl;
        inds2[round] = atoi(str.c_str());

        getline(istr, str, ',');
        value[round] = atof(str.c_str());
        round++;
    }

    for(uint i = 0; i < 5; i++)
        cout<<inds0[i]<<' ';
    cout<<endl;
    for(uint i = 0; i < 5; i++){
        cout<<inds1[i]<<' ';
    }
    cout<<endl;
    for(uint i = 0; i < 5; i++){
        cout<<inds2[i]<<' ';
    }
    cout<<endl;
    for(uint i = 0; i < 5; i++){
        cout<<value[i]<<' ';
    }
    cout<<endl;

    cout<<"finish read tensor file"<<endl;

        map<uint, bool> randomnumber;

    // 初始化随机种子
    srand(static_cast<unsigned uint>(std::time(nullptr)));

    const uint arraySize = nnz * rate; // 数组大小   
    uint uniqueNumbers[arraySize]; // 存储不重复随机数的数组

    // 设置随机数生成器
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<uint> dis(0, nnz - 1); // 生成1到1200000之间的随机数

    // 生成不重复的随机数并存储到数组中
    uint count = 0; // 记录已生成的不重复随机数的数量
    while (count < arraySize) {
        uint randomNumber = dis(gen); // 生成随机数
        // 检查新生成的随机数是否已存在于数组中
        bool isUnique = true;
        for (uint i = 0; i < count; ++i) {
            if (uniqueNumbers[i] == randomNumber) {
                isUnique = false;
                break;
            }
        }
        // 如果随机数不重复，则添加到数组中
        if (isUnique) {
            uniqueNumbers[count] = randomNumber;
            ++count;
        }
    }
    std::sort(uniqueNumbers, uniqueNumbers + arraySize);
    cout<<"finish"<<endl;




    return 0;
}