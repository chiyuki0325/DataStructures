#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef unsigned long lu;
typedef unsigned int du;

typedef struct BST {
  struct BST *left;
  struct BST *right;
  lu value;
  du amount;
} BST;

BST *bst_init(lu initial_value) {
  BST *root = malloc(sizeof(BST));
  root->amount = 0;
  root->value = initial_value;
  return root;
}

void bst_insert(BST *node, lu value) {
  if (value < node->value) {
    // 插入到左边
    if (node->left == NULL) {
      node->left = bst_init(value);
    } else {
      bst_insert(node->left, value);
    }
  } else if (value > node->value) {
    // 插入到右边
    if (node->right == NULL) {
      node->right = bst_init(value);
    } else {
      bst_insert(node->right, value);
    }
  } else {
    // 相等
    node->amount++;
  }
}

BST *bst_find_min_greater(BST *root, lu value) {
  BST *node = root;
  BST *result = NULL;
  while (node != NULL) {
    if (node->value <= value) {
      // 往右推进
      node = node->right;
    } else {
      // 往左推进
      result = node;
      node = node->left;
    }
  }
  return result;
}

int main() {
  // 输入
  int len;
  scanf("%d", &len);
  lu *blocks = malloc(sizeof(lu) * len);
  for (int i = 0; i < len; i++)
    scanf("%lu", blocks + i);

  // 创建塔顶搜索树
  BST *tops = bst_init(blocks[0]);
  int towers = 1;

  for (int i = 1; i < len; i++) {
    // printf("当前方块 %lu\n", blocks[i]);
    // 寻找要放置于其上的塔
    BST* tower_to_place = bst_find_min_greater(tops, blocks[i]);
    if (tower_to_place == NULL) {
      // 插入一座新的塔
      bst_insert(tops, blocks[i]);
      towers++;
    } else {
      tower_to_place->value=blocks[i];
    }
  }

  printf("%d", towers);
  return 0;
}
