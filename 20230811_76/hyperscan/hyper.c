#include <unistd.h>
#include <errno.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <ctype.h>
#include <hs.h>
#include "cJSON.h"
#include "hyper.h"
#include <dlfcn.h>
/*正则匹配的函数以及回调函数*/
hs_database_t *database;
int regularity_number;
int *ids;
static int (*my_hs_compile_multi)();
static int (*my_hs_scan)();
static int (*my_hs_alloc_scratch)();
static int (*my_hs_free_scratch)();
static int (*my_hs_free_database)();
static int (*my_hs_free_compile_error)();
// static int (*hs_compile_multi)();
// static int (*hs_scan)();
// static int (*hs_alloc_scratch)();
// static int (*hs_free_scratch)();
// static int (*hs_free_database)();
// static int (*hs_alloc_scratch)();
// static int (*hs_free_compile_error)();
void *load_sym (const char *lib_name, const char *sym)
{
    void *handle = 0, *psym = 0;
    char *error = 0;

    handle = dlopen (lib_name, RTLD_LAZY);
    if (handle == 0)
    {
        return 0;
    }
    psym = dlsym (handle, sym);
    if ((error = dlerror()) != 0)
    {
        return 0;
    }
    //	dlclose(handle);
    return psym;
}


/*加载动态链接库，前辈写的*/
static void load_one_sym(const char *lib_name, const char *sym, void **psym)
{
    *psym = load_sym(lib_name, sym);
    if (*psym == 0)
    {
        fprintf(stderr, "%s.%d F %s %s\n", __FILE__, __LINE__, lib_name, sym);
        exit(100);
    }
}

static int eventHandler(unsigned int id, unsigned long long from,
                        unsigned long long to, unsigned int flags, void *ctx)
{
    Node *node = (Node *)ctx;
    cJSON* cjson_head = node->cjson;
  //  printf("cjson:%s\n",cJSON_Print(cjson_head));
    char* inputdata = node->inputdata;
    //printf("Match for pattern \"%d\" at offset from %llu to %llu\n", id, from, to);
    //获得to-from的值
    int offset = to - from;
   // printf("length: %d\n", offset);
    if (offset != 0)
    {
        char which[6];
        memset(which, 0, sizeof(which));
        sprintf(which,"%d",id);
     //   printf("which: %s\n", which);
       // printf("whichcontent %s\n",cJSON_Print(cJSON_GetObjectItem(cjson_head,which)));
        cJSON* cjson_test = cJSON_GetObjectItem(cjson_head, which);
        char* oldcontent = cJSON_GetObjectItem(cjson_test, "content")->valuestring;
       // printf("oldcontent %s\n",oldcontent);
        int contentlength = cJSON_GetObjectItem(cjson_test, "length")->valueint;
       // printf("contentlength %d\n",contentlength);
        char* newcontent=NULL;
        newcontent = (char*)malloc(contentlength+offset+10);
        //printf("#########newcontent###########\n");
        //char* hitcontent = (char*)malloc(offset);
        //printf("#########hitcontent###########\n");
        //memset(hitcontent, '\0', offset);
        //memcpy(hitcontent, inputdata+from,offset+1);
        //printf"hitcontent %s\n",hitcontent);
        memset(newcontent, '\0', contentlength+offset+10);
	memcpy(newcontent,oldcontent,strlen(oldcontent));
         //strcat(newcontent, oldcontent);
        //printf"newcontent %s\n",newcontent);
        if(contentlength!=1){
	memcpy(newcontent+strlen(newcontent),";",1);
             //strcat(newcontent, ";");
        }
	memcpy(newcontent+strlen(newcontent),inputdata+from,offset);
         //strcat(newcontent,hitcontent);
        //printf"newcontent %s\n",newcontent);
        contentlength = contentlength+offset+10;
        //printf"contentlength %d\n",contentlength);
        cJSON_ReplaceItemInObject(cjson_test, "content", cJSON_CreateString(newcontent));
        cJSON_ReplaceItemInObject(cjson_test, "length", cJSON_CreateNumber(contentlength));
        cJSON_ReplaceItemInObject(cjson_head,which,cjson_test);
        //printf"cjson:%s\n",cJSON_Print(cjson_head));
        free(newcontent);
        //free(hitcontent);
    }
    //printf"return 0\n");
    return 0;
}
//返回match_result
char* get_match_result(char *inputData)
{
    // 打印inputData
   // printf("inputData: %s\n", inputData);
    cJSON *cjson_head = cJSON_CreateObject();
    int i;
    for (i = 0; i < regularity_number; i++)
    {
        char which[6];
        memset(which, 0, sizeof(which));
        sprintf(which,"%d",ids[i]);
        cJSON *cjson_test = cJSON_CreateObject();
        /* 添加一条整数类型的JSON数据(添加一个链表节点) */
        cJSON_AddStringToObject(cjson_test, "model_id", which);
        cJSON_AddStringToObject(cjson_test, "content", "");
        cJSON_AddNumberToObject(cjson_test, "length", 1);

        // 添加cjson_test到cjson_head
        cJSON_AddItemToObject(cjson_head, which, cjson_test);
    }
    Node *node = (Node*)malloc(sizeof(Node));
   // printf("#################Node###########\n");
    //拷贝一份inputData
    node->inputdata = (char*)malloc(strlen(inputData)+1);
   // printf("#################inputdata###########\n");
    memset(node->inputdata, 0, strlen(inputData)+1);
    memcpy(node->inputdata, inputData, strlen(inputData));

    node->cjson = cjson_head;
    //printf"%s\n",inputData);
    //将match_result清零
    unsigned int length;
    length = strlen(inputData);
    hs_scratch_t *scratch = NULL;
    if (my_hs_alloc_scratch(database, &scratch) != HS_SUCCESS)
    {
        fprintf(stderr, "ERROR: Unable to allocate scratch space. Exiting.\n");
        my_hs_free_database(database);
        return NULL;
    } // length -=1;
//    printf("Scanning %u bytes with Hyperscan\n", length);
    if (my_hs_scan(database, inputData, length, 0, scratch, eventHandler, node) != HS_SUCCESS)
    {
        printf( "ERROR: Unable to scan input buffer. Exiting.\n");
        my_hs_free_scratch(scratch);
        return NULL;
    } /* Scanning is complete, any matches have been handled, so now we just      * clean up and exit.      */
    my_hs_free_scratch(scratch);
    printf("hyperscan：输入%s\n",inputData);
    printf("hyperscan：输出%s\n",cJSON_Print(cjson_head));
    return cJSON_Print(cjson_head);
}



//初始化，编译数据库
void hyperscan_init(int myids[], char mypatterns[][1000], int length){
    char ** patterns;
    int j =0;
    ids = (int*)malloc(sizeof(int)*length);
    //拷贝myids到ids
    for(j=0;j<length;j++){
        ids[j] = myids[j];
    }
    for (j=0;j<length;j++){
        //拷贝mypatterns到patterns
        patterns[j] = (char*)malloc(1000);
        strcpy(patterns[j],mypatterns[j]);
    }
    // 遍历输出ids和patterns
    for (j=0;j<length;j++){
        printf("hyperscan：ids[%d]:%d\n",j,ids[j]);
        printf("hyperscan：patterns[%d]:%s\n",j,patterns[j]);
    }
    int i =0;

    load_one_sym("./libhs.so", "hs_compile_multi", (void **)&my_hs_compile_multi);
    load_one_sym("./libhs.so", "hs_scan", (void **)&my_hs_scan);
    load_one_sym("./libhs.so", "hs_alloc_scratch", (void **)&my_hs_alloc_scratch);
    load_one_sym("./libhs.so", "hs_free_scratch", (void **)&my_hs_free_scratch);
    load_one_sym("./libhs.so", "hs_free_database", (void **)&my_hs_free_database);
    load_one_sym("./libhs.so", "hs_free_compile_error", (void **)&my_hs_free_compile_error);
    regularity_number= length;
    printf("length\n");
    printf("length:%d\n",length);
    printf("load sym finish!\n");
    unsigned flags[10000];
    printf("length\n");
    printf("length:%d\n",length);

    i = 0;
    for (i = 0; i < length; i++)
    {
        flags[i] = HS_FLAG_SOM_LEFTMOST | HS_FLAG_DOTALL;
    }
    if (database == NULL)
    {

        // int j = 0;
        // for (j = 0; j < pattern_num; j++)
        // for (int i = 0; i < pattern_num; ++i) { fprintf(stdout, "%s\n", patterns[i]);  }
        hs_compile_error_t *compile_err;
        printf("before compile!\n");
        if (my_hs_compile_multi(patterns, flags, ids, length, HS_MODE_BLOCK, NULL, &database, &compile_err) != HS_SUCCESS)
        {
            printf("error\n");
            //fprintf(stderr, "error, %s\n", *compile_err);
            my_hs_free_compile_error(compile_err);
            return;
        }
	if (database == NULL)
	{
	    printf("database is null\n");
	}
	else
	{
		 printf("database is not null\n");
	}
        printf("1111111111111111compliefinish!222222222222222222222221\n");
        // my_hs_alloc_scratch(hyper_database, &scratch);
        // while (my_hs_alloc_scratch(hyper_database, &scratch) != HS_SUCCESS) { fprintf(stderr, "not enough!\n");  }
        // fprintf(stdout, "init over!!!\n");
        // exit(0);
    }
    // free the memory
    printf("free!\n");
    //for (j=0;j<length;j++){
    //    free(patterns[j]);
    //}
//    printf("11111111111111111133333333333333333311");
    return;
}
