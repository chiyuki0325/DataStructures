#include <stdio.h>
#include <stdlib.h>

typedef unsigned long lu;

int main() {
    // 输入
    int len; scanf("%d", &len);

    lu* blocks = malloc(sizeof(lu)*len);
    for (int i=0; i<len; i++) scanf("%lu", blocks+i);

    lu *tops = malloc(sizeof(lu)*len);
    // 最坏情况是len个
    tops[0]=blocks[0];
    // 当前最右侧格子+1
    int edge=1;

    for (int i=1; i<len; i++) {
        // 此时tops是有序的
        // 要找到第一个比blocks[i]大的元素
        int left=0; int right=edge;
        while (left<right) {
            int middle = left + (right-left)/2;
            if (tops[middle]<=blocks[i]) {
                left=middle+1;
            } else {
                right=middle;
            }
        }
        // middle 即为要找的第一个塔顶
        tops[left]=blocks[i];
        if (left==edge) {
            // 向右扩展
            edge+=1;
        }
    }

    printf("%lu", edge);
    return 0;
}
