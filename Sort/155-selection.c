#include <stdio.h>
#include <stdlib.h>

void swap(int* a, int* b, int* swapCount) {
    int tmp=*a;
    *a=*b;
    *b=tmp;
    *swapCount=*swapCount+1;
}

void selectionSort(int len, int* arr, int* swapCount) {
    for (int i=0; i<len; i++) {
        int minIdx=i;
        for (int j=i; j<len; j++) {
            if (arr[j]<arr[minIdx]) minIdx=j;
        }
        // 已经得到当前未排序部分中最小的元素
        if (i!=minIdx)
        swap(arr+i, arr+minIdx, swapCount);
    }
}

int main() {
    // 输入
    int len; scanf("%d", &len);
    int* arr = malloc(sizeof(int)*len);
    for (int i=0; i<len; i++) {
        scanf("%d", arr+i);
    }

    /*
    for (int i=0; i<len; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    */

    int swapCount=0;
    selectionSort(len, arr, &swapCount);


    for (int i=0; i<len; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n%d\n", swapCount);

    return 0;
}
