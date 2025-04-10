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
#include <random>

using namespace std;

int main(int argc, char **argv){
    
    // Read gps file and load the data into lists
    ifstream inFile_gps(argv[1], ios::in);
    string lineStr;
    vector<string> item;
    uint num_gps = 0;

    getline(inFile_gps, lineStr);
    while(getline(inFile_gps, lineStr)){
        item.push_back(lineStr);
        num_gps++;
    }
    cout<<"The number of gps is: "<<num_gps<<endl;

    // 创建数组存储轨迹数据的各列
    double *Data_lng = nullptr;
    Data_lng = (double*)malloc(sizeof(double) * num_gps);
    memset(Data_lng, 0, sizeof(double) * num_gps);

    double *Data_lat = nullptr;
    Data_lat = (double*)malloc(sizeof(double) * num_gps);
    memset(Data_lat, 0, sizeof(double) * num_gps);


    // 存储轨迹数据
    uint round = 0;
    for (auto it = item.begin(); it != item.end(); it++){
        string str;
        istringstream istr(*it);
        getline(istr, str, ',');
        // cout << str << ' ';
        Data_lng[round] = atof(str.c_str());

        getline(istr, str, ',');
        // cout << str << ' ';
        Data_lat[round] = atof(str.c_str());

        round++;
    }

    // 输出每个数组的前五个元素.检查是否正确
    // for(uint i = 0; i < 5; i++){
    //     cout<<Data_lng[i]<<' ';
    // }
    for(uint i = 0; i < 5; i++)
        printf("%.5f ", Data_lng[i]);
    cout<<endl;
    for(uint i = 0; i < 5; i++){
        cout<<Data_lat[i]<<' ';
    }
    cout<<endl;
    

    cout<<"finish read the gps file"<<endl;

    // 创建数组存储张量的各列元素
    uint *segments = nullptr;
    segments = (uint*)malloc(sizeof(uint) * num_gps);
    memset(segments, 10000, sizeof(uint) * num_gps);
    uint *timeoday = nullptr;
    timeoday = (uint*)malloc(sizeof(uint) * num_gps);
    memset(timeoday, 0, sizeof(uint) * num_gps);
    uint *days = nullptr;
    days = (uint*)malloc(sizeof(uint) * num_gps);
    memset(days, 0, sizeof(uint) * num_gps);
    float *values = nullptr;
    values = (float*)malloc(sizeof(float) * num_gps);
    memset(values, 0, sizeof(float) * num_gps);

    cout<<"create arrays to store tensor values and index"<<endl;

    // Read link file and load the data into lists
    ifstream inFile_road(argv[2], ios::in);
    string lineStr_road;
    vector<string> item_road;
    uint num_road = 0;

    // 存取道路文件信息
    getline(inFile_road, lineStr_road);
    while(getline(inFile_road, lineStr_road)){
        item_road.push_back(lineStr_road);
        num_road++;
    }
    cout<<"The number of road is: "<<num_road<<endl;

    // 创建数组存储道路信息
    double *Road_lng = nullptr;
    Road_lng = (double*)malloc(sizeof(double) * num_road);
    memset(Road_lng, 0, sizeof(double) * num_road);

    double *Road_lat = nullptr;
    Road_lat = (double*)malloc(sizeof(double) * num_road);
    memset(Road_lat, 0, sizeof(double) * num_road);

    double *Road_id = nullptr;
    Road_id = (double*)malloc(sizeof(double) * num_road);
    memset(Road_id, 0, sizeof(double) * num_road);

    // 存储道路信息
    uint round_r = 0;
    for (auto it_r = item_road.begin(); it_r != item_road.end(); it_r++){
        string str_r;
        istringstream istr_r(*it_r);
        getline(istr_r, str_r, ',');
        Road_id[round_r] = atoi(str_r.c_str());

        getline(istr_r, str_r, ',');
        Road_lng[round_r] = atof(str_r.c_str());

        getline(istr_r, str_r, ',');
        Road_lat[round_r] = atof(str_r.c_str());


        round_r++;
    }

    // 输出数组前五个元素验证是否正确
    for(int i = 0; i < 5; ++i)
        cout<<Road_lng[i]<<' ';
    cout<<endl;
    for(int i = 0; i < 5; ++i)
        cout<<Road_lat[i]<<' ';
    cout<<endl;
    for(int i = 0; i < 5; ++i)
        cout<<Road_id[i]<<' ';
    cout<<endl;
    cout<<"The number of road is: "<<round_r<<endl;
    cout<<"finish load the road data\n";

    std::random_device rd; // 获取随机种子
    std::mt19937 gen(rd()); // 用随机种子初始化随机数生成器

    // 创建一个用于生成0到287之间的随机整数的分布
    std::uniform_int_distribution<> dist_0_287(0, 287);

    // 创建一个用于生成0到55之间的随机整数的分布
    std::uniform_int_distribution<> dist_0_55(0, 55);

    

    //进行路网匹配
    uint num_match = 0;
    uint i, j;
    double dis[10];
    int dis_idx[10];
    double distance_min;
    int index_min;

    for(i = 0; i < num_gps; ++i){
        // initialize the list dis[] and dis_idx[]
        for(int s = 0; s < 10; ++s){
            dis[s] = 1;
            dis_idx[s] = 10000;
        }
        uint num_dis = 0;
        double dis_min = 2.0;
        int dis_idx_min = 10000;
        for(j = 0; j < num_road; ++j){
            if((fabs(Data_lng[i] - Road_lng[j]) <= 0.0001) || (fabs(Data_lat[i] - Road_lat[j]) <= 0.0001)){
            // if(fabs(Data_lng[i] - Road_lng[j]) <= 0.00005){
            //     if(fabs(Data_lat[i] - Road_lat[j]) <= 0.00005){
                    // Calculate the distance between the trajectory point and the road :: calculate the 10 minimum distance between the trajectory point and the road
                    double distance_temp = sqrt(pow(Data_lng[i] - Road_lng[j], 2) + pow(Data_lat[i] - Road_lat[j], 2));
                    dis_idx[num_dis] = j;
                    dis[num_dis] = distance_temp;
                    ++num_dis;
                // }
            }
            // find the min road and its index 
            if(num_dis == 20 || j == num_road - 1){
                for(int k = 0; k < num_dis; ++k){
                    if(dis[k] < distance_min)
                        distance_min = dis[k];
                        index_min = dis_idx[k];
                }
                segments[num_match] = Road_id[index_min];
                // timeoday[num_match] = Data_time[i];
                // days[num_match] = Data_day[i];
                // 生成随机整数
                timeoday[num_match] = dist_0_287(gen);
                days[num_match] = dist_0_55(gen);
                values[num_match] = 1;

                ++num_match;
                break;
            }

        }

    }
    cout<<"num_match = "<<num_match<<endl;
    
    // uint num_day = 56;
    
    // write into file 
    FILE *fp = fopen(argv[3], "w");
    fprintf(fp, "road,time,days,values\n");
    for(uint i = 0; i < num_match; ++i){
        if(segments[i] != 10000){
            // fprintf(fp, "%u,%u,%u,%.4f,%.0f,%.0f,%.6f,%.6f\n", segments[i], timeoday[i], days[i], values[i], from_values[i], to_values[i], lng_values[i], lat_values[i]);
            fprintf(fp, "%u,%u,%u,%.4f\n", segments[i], timeoday[i], days[i], values[i]);
        }
    }
    cout<<"finish write\n";

    free(Data_lng);
    free(Data_lat);
    // free(Data_time);
    // free(Data_day);
    free(Road_id);
    free(Road_lng);
    free(Road_lat);
    free(segments);
    free(timeoday);
    free(days);
    free(values);

    return 0;
}