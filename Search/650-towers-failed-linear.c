#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef unsigned long lu;

int main() {
  // 输入
  int len;
  scanf("%d", &len);
  lu *blocks = malloc(sizeof(lu) * len);
  for (int i = 0; i < len; i++)
    scanf("%lu", blocks + i);

  lu *ground = malloc(sizeof(lu) * len);
  // 最坏情况是len个
  for (int i = 0; i < len; i++)
    ground[i] = 0;
  // 当前最右侧格子+1
  int edge = 0;

  for (int i = 0; i < len; i++) {
    // printf("当前方块 %lu\n", blocks[i]);
    lu min_square = ULONG_MAX; // 塔顶面积最小的格子的面积
    int min_pos = -1;
    for (int pos = 0; pos < edge; pos++) {
      // 遍历所有已经放过方块的格子
      // 找到当前符合条件的，塔顶面积最小的格子
      if (ground[pos] > blocks[i] && ground[pos] < min_square) {
        min_square = ground[pos];
        min_pos = pos;
      }
    }

    if (min_pos != -1) {
      // 有可放的格子
      // printf("放置在现有格子 %d 上\n", min_pos);
      ground[min_pos] = blocks[i];
    } else {
      // 向右拓展格子
      // printf("向右拓展一格：%d\n", edge);
      ground[edge] = blocks[i];
      edge++;
    }
  }

  printf("%d", edge);
  return 0;
}
