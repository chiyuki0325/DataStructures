#include <stdio.h>
#include <stdlib.h>

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
  int len = 8;
  int test_data[] = {100, 50, 200, 10, 60, 150, 300, 500};
  BST *root = bst_init(test_data[0]);
  for (int i = 1; i < len; i++) {
    bst_insert(root, test_data[i]);
  }
  printf("%lu", bst_find_min_greater(root,600)->value);
  return 0;
}
