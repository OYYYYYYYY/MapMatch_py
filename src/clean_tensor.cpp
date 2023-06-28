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

using namespace std;

int main(int argc, char **argv){
    
    FILE *f = fopen(argv[1], "r");
    char *line = NULL;
    size_t len = 0;

    uint nmode;
    nmode = fscanf(f, "%u", &nmode);

    uint *dims = nullptr;
    dims = (uint*)malloc(sizeof(uint) * nmode);

    for(uint i = 0; i < nmode; ++i)
        fscanf(f, "%u" &dims[i]);
    
    fscanf(f,"\n");

    uint nnz = 0;
    long fp_local = ftell(fp);
    //获得非零元个数
    while((getline(&line, &len, f)) != -1){
        ++nnz;
    }

    cout<<"nnz = "<<nnz<<endl;

    uint *segments = nullptr;
    segments = (uint*)malloc(sizeof(uint) * nnz);
    uint *timeoday = nullptr;
    timeoday = (uint*)malloc(sizeof(uint) * nnz);
    uint *days = nullptr;
    days = (uint*)malloc(sizeof(uint) * nnz);
    float *values = nullptr;
    values = (float*)malloc(sizeof(float) * nnz);

    
    tnsIndex nnz_chk = 0;
    char *ptr = NULL;
    fseek(fp, fp_local, 0);
    while((getline(&line, &len, f)) != -1)
    {
        ptr = line;
        for(uint i = 0; i < nmode; ++i)
        {
            tsr->inds[mode].values[nnz_chk] = strtoul(ptr, &ptr, 10) - indextype;
        }
        tsr->values.values[nnz_chk] = strtod(ptr, &ptr);
        ++nnz_chk;
    }
    
    // write into file 
    FILE *fp = fopen(argv[2], "w");
    fprintf(fp, "3\n");
    fprintf(fp, "%u %u %u\n", round_r, num_time, num_day);
    for(uint i = 0; i < num_match; ++i){
        if(segments[i] != 10000){
            fprintf(fp, "%u %u %u %.0f\n", segments[i], timeoday[i], days[i], values[i]);
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

    return 0;
}