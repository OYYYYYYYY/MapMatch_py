#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <cstring>

using namespace std;

int main(int argc, char **argv){
    // int *Data = NULL;
    // Data = (int*)malloc(sizeof(int) * 4 * 3);
    // memset(Data, 0, sizeof(int) * 4 * 3);

    int *Data_a = NULL;
    Data_a = (int*)malloc(sizeof(int) * 4);
    memset(Data_a, 0, sizeof(int) * 4);

    int *Data_b = NULL;
    Data_b = (int*)malloc(sizeof(int) * 4);
    memset(Data_b, 0, sizeof(int) * 4);

    int *Data_c = NULL;
    Data_c = (int*)malloc(sizeof(int) * 4);
    memset(Data_c, 0, sizeof(int) * 4);


    ifstream inFile(argv[1], ios::in);
    string lineStr;
    
    vector<string> item;
    // string temp;

    getline(inFile, lineStr);
    while(getline(inFile, lineStr)){
        item.push_back(lineStr);
    }
    uint round = 0;
    for (auto it = item.begin(); it != item.end(); it++){
        string str;
        istringstream istr(*it);
        getline(istr, str, ',');
        cout << str << ' ';
        Data_a[round] = atoi(str.c_str());

        getline(istr, str, ',');
        cout << str << ' ';
        Data_b[round] = atoi(str.c_str());

        getline(istr, str, ',');
        cout << str <<endl;
        Data_c[round] = atoi(str.c_str());
        round++;
    }
    // system("pause");
    for(int i = 0; i < 4; i++){
        cout<<Data_a[i]<<' ';
    }
    cout<<endl;
    for(int i = 0; i < 4; i++){
        cout<<Data_b[i]<<' ';
    }
    cout<<endl;
    for(int i = 0; i < 4; i++){
        cout<<Data_c[i]<<' ';
    }
    cout<<endl;

    return 0;
}