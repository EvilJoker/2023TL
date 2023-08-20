#include <stdio.h>
#include <string.h>
#include <stdlib.h>


struct KeyValue {
    const char *key;
    const char *value;
};

struct KeyValue dict[] = {
    {"dwAge-json", "jage"},
    {"acName-json", "jname"},
    {"acName-yaml", "yaml"},
    // ...
};

// 假设定义了一个名为Student的结构体


// 定义函数，从map中提取指定字段的值，并放入mybuf中
void GetTagOfStudentByField(const char *pcField, const char *pcTag, char *mybuf, size_t mybuflen) {
    snprintf(mybuf, mybuflen, "%s", "-1");

    size_t len1 = strlen(pcField);
    size_t len2 = strlen(pcTag);
    size_t totalLen = len1 + len2 + 3;
    char *search_key = (char *)malloc(totalLen);

    if (search_key == NULL) {
        return;
    }
    strcpy(search_key, pcField);
    strcat(search_key, "-");
    strcat(search_key, pcTag);
    printf("search_key: %s\n", search_key);

    for (size_t i = 0; i < sizeof(dict) / sizeof(dict[0]); i++) {
        if (strcmp(dict[i].key, search_key) == 0) {
            const char *tags = dict[i].value;

            printf("Value for key '%s': %s\n", search_key, tags);
            snprintf(mybuf, mybuflen, "%s", tags);
            break;
        }
    }
    // 释放
    free(search_key);

}

void GetTagOfStudentByIndex(int index, const char *pcTag, char *mybuf, size_t mybuflen) {

    snprintf(mybuf, mybuflen, "%s", "-1");

    if (index < 0 || index >= sizeof(dict) ){
        return ;
    }

    const char * target_value = dict[index].key;
    
    size_t str_len = strlen(target_value);
    size_t suffix_len = strlen(pcTag);

    if (str_len < suffix_len) {
        return ; // 字符串长度不够，不可能以后缀结尾
    }

    const char *end_of_str = target_value + (str_len - suffix_len);
    if (strcmp(end_of_str, pcTag) == 0){
        snprintf(mybuf, mybuflen, "%s", dict[index].value);
    }
    

}



int main() {
    char mybuf[100]; // 用于存储结果的缓冲区
    size_t mybuflen = sizeof(mybuf);


    GetTagOfStudentByField("dwAge", "json", mybuf, mybuflen);
    printf("Result by Field: %s\n", mybuf);
    GetTagOfStudentByField("dwAge", "json222", mybuf, mybuflen);
    printf("Result by Field err: %s\n", mybuf);
    GetTagOfStudentByIndex(1, "json", mybuf, mybuflen);
    printf("Result by Index: %s\n", mybuf);


    return 0;
}
