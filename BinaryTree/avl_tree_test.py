# 测试样例由哈基米生成

from avl_tree import AVLTree, TreeNode
from visualizer import TreeVisualizer
import random

if __name__ == '__main__':
    # --- 產生一組大型的、不重複的隨機數據 ---
    # 設定數據範圍和數量
    data_range = range(101)  # 數字範圍 0-100
    num_nodes = 70

    # 從範圍中隨機抽取不重複的樣本
    # random.sample確保了所有數字都是唯一的
    nodes_to_insert = random.sample(data_range, num_nodes)

    print(f"用 {num_nodes} 個隨機節點進行測試: ")
    print(sorted(nodes_to_insert))  # 排序後印出，方便查看

    # 建立一棵 AVL 樹
    tree = AVLTree()

    # 依序插入所有隨機產生的節點
    for val in nodes_to_insert:
        tree.insert(val)

    # 建立渲染器實例
    visualizer = TreeVisualizer()

    # 將經過大量數據插入並自動平衡後的樹，渲染成 SVG 檔案
    visualizer.render(tree.root, 'avl_tree_random_test.svg')
