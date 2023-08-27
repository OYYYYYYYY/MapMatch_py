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
#include <cuda.h>
#include <cuda_runtime.h>


using namespace std;

#define gridmax 32768

__global__ void check_redun(uint num_match, uint* segments, uint* timeoday, uint* days, float* values, uint* num_redun){
    uint i = blockIdx.x + threadIdx.x;
    if(i < num_match){
        for(int j = i + 1; j < num_match; ++j){
            if((segments[i] == segments[j]) && (timeoday[i] == timeoday[j]) && (days[i] == days[j])){
                segments[j] = 10000;
                atomicAdd(&(values[j]), values[i]);
                atomicAdd(&(num_redun[0]), 1);
            }
        }
    }
    printf("%u", num_redun[0]);

}

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

    uint *Data_time = nullptr;
    Data_time = (uint*)malloc(sizeof(uint) * num_gps);
    memset(Data_time, 0, sizeof(uint) * num_gps);

    int *Data_day = nullptr;
    Data_day = (int*)malloc(sizeof(int) * num_gps);
    memset(Data_day, 0, sizeof(int) * num_gps);

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

        getline(istr, str, ',');
        // cout << str <<endl;
        Data_time[round] = atoi(str.c_str());

        getline(istr, str, ',');
        Data_day[round] = atoi(str.c_str());
        round++;
    }

    // 输出每个数组的前五个元素.检查是否正确
    for(uint i = 0; i < 5; i++){
        cout<<Data_lng[i]<<' ';
    }
    cout<<endl;
    for(uint i = 0; i < 5; i++){
        cout<<Data_lat[i]<<' ';
    }
    cout<<endl;
    for(uint i = 0; i < 5; i++){
        cout<<Data_time[i]<<' ';
    }
    cout<<endl;
    for(uint i = 0; i < 5; i++){
        cout<<Data_day[i]<<' ';
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

    uint *Road_id = nullptr;
    Road_id = (uint*)malloc(sizeof(uint) * num_road);
    memset(Road_id, 0, sizeof(uint) * num_road);

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

    // 判断segments数组赋值是否有错误
    // for(uint i = 0; i < num_gps; ++i){
    //     if(segments[i] != 10000){
    //         cout<<"segments value error\n";
    //         return 0;
    //     }
    // }
    // for(int i = 0; i < num_road; ++i){
    //     cout<<Road_id[i]<<' ';
    // }
    //进行路网匹配
    uint num_match = 0;
    uint i, j;
    // #pragma omp parallel for num_threads(16), private(i,j)
    for(i = 0; i < num_gps; ++i){
        for(j = 0; j < num_road; ++j){
            if((fabs(Data_lng[i] - Road_lng[j]) <= 0.005) && (fabs(Data_lat[i] - Road_lat[j]) <= 0.005)){
                segments[num_match] = Road_id[j];
                // cout<<segments[num_match]<<' '<<Road_id[j]<<endl;
                timeoday[num_match] = Data_time[i];
                days[num_match] = Data_day[i];
                values[num_match] = 1;
                num_match++;
                break;
            }
        }
    }

    cout<<"num_match = "<<num_match<<endl;
    
    // uint num_repetition = 0;
    uint re_num[1] = {0};
    // #pragma omp parallel for num_threads(16), private(i)
    // for(i = 0; i < num_match; ++i){
    //     for(j = i + 1; j < num_match; ++j){
    //         if((segments[i] == segments[j]) && (timeoday[i] == timeoday[j]) && (days[i] == days[j])){
    //             segments[j] = 10000;
    //             values[i]++;
    //             num_repetition++;
    //         }
    //     }
    // }
    
    uint *segments_d;
    cudaMalloc((void**)&segments_d, sizeof(uint) * num_gps);
    cudaMemcpy(segments_d, segments, sizeof(uint) * num_gps, cudaMemcpyHostToDevice);
    uint *timeoday_d;
    cudaMalloc((void**)&timeoday_d, sizeof(uint) * num_gps);
    cudaMemcpy(timeoday_d, timeoday, sizeof(uint) * num_gps, cudaMemcpyHostToDevice);
    uint *days_d;
    cudaMalloc((void**)&days_d, sizeof(uint) * num_gps);
    cudaMemcpy(days_d, days, sizeof(uint) * num_gps, cudaMemcpyHostToDevice);
    float *values_d;
    cudaMalloc((void**)&values_d, sizeof(float) * num_gps);
    cudaMemcpy(values_d, values, sizeof(float) * num_gps, cudaMemcpyHostToDevice);
    uint *re_num_d;
    cudaMalloc((void**)&re_num_d, sizeof(uint) * 1);
    cudaMemcpy(re_num_d, re_num, sizeof(uint) * 1, cudaMemcpyHostToDevice);
    

    // uint *segments_r = nullptr;
    // segments_r = (uint*)malloc(sizeof(uint) * num_gps);
    // memset(segments_r, 10000, sizeof(uint) * num_gps);
    // uint *timeoday_r = nullptr;
    // timeoday_r = (uint*)malloc(sizeof(uint) * num_gps);
    // memset(timeoday_r, 0, sizeof(uint) * num_gps);
    // uint *days_r = nullptr;
    // days_r = (uint*)malloc(sizeof(uint) * num_gps);
    // memset(days_r, 0, sizeof(uint) * num_gps);
    // float *values_r = nullptr;
    // values_r = (float*)malloc(sizeof(float) * num_gps);
    // memset(values_r, 0, sizeof(float) * num_gps);
    
    cout<<"data memcpy to device"<<endl;
    dim3 block(256);
    dim3 grid;
    if(num_match < gridmax)
        grid.x = num_match;
    else
        grid.x = gridmax - 10000;
    check_redun<<<grid, block>>>(num_match, segments_d, timeoday_d, days_d, values_d, re_num_d);

    cout<<"finish gpu"<<endl;

    cudaMemcpy(segments, segments_d, sizeof(uint) * num_gps, cudaMemcpyDeviceToHost);
    cudaMemcpy(timeoday, timeoday_d, sizeof(uint) * num_gps, cudaMemcpyDeviceToHost);
    cudaMemcpy(days, days_d, sizeof(uint) * num_gps, cudaMemcpyDeviceToHost);
    cudaMemcpy(values, values_d, sizeof(float) * num_gps, cudaMemcpyDeviceToHost);
    cudaMemcpy(re_num, re_num_d, sizeof(uint) * 1, cudaMemcpyDeviceToHost);


    cout<<"The number of repetition is :"<<re_num[0]<<endl;
    uint num_day = 28;
    uint num_time = 18 * 60 * 60 / 60;

    // for(uint s = 0; s < 100; ++s)
    //     cout<<segments[s]<<' ';
    // cout<<endl;

    // make the begin index from 0 to 1
    for(uint i = 0; i < num_match; ++i){
        segments[i]++;
        timeoday[i] = (timeoday[i] / 60) - 359;
        days[i]++;
    }
    
    // write into file 
    FILE *fp = fopen(argv[3], "w");
    fprintf(fp, "3\n");
    fprintf(fp, "%u %u %u\n", round_r, num_time, num_day);
    for(uint i = 0; i < num_match; ++i){
        if(segments[i] != 10001){
            fprintf(fp, "%u %u %u %.4f\n", segments[i], timeoday[i], days[i], values[i]);
        }
    }
    cout<<"finish write\n";

    free(Data_lng);
    free(Data_lat);
    free(Data_time);
    free(Data_day);
    free(Road_id);
    free(Road_lng);
    free(Road_lat);
    free(segments);
    free(timeoday);
    free(days);
    free(values);
    cudaFree(segments_d);
    cudaFree(timeoday_d);
    cudaFree(days_d);
    cudaFree(values_d);
    cudaFree(re_num_d);

    return 0;
}