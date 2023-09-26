#include <stdio.h>
#include <stdlib.h>
#include "cJSON.h"
typedef struct _node
{
    char *inputdata;
    cJSON * cjson;
} Node;
char* get_match_result(char *inputData);
void hyperscan_init(int myids[], char mypatterns[][1000], int length);
