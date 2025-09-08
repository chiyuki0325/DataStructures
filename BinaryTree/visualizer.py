# 使用哈基米生成
import sys

class TreeVisualizer:
    """將 TreeNode 渲染成 SVG 圖片"""
    def __init__(self, config: dict = None):
        # 預設外觀設定
        self.config = {
            'radius': 20,
            'v_spacing': 70,
            'h_spacing': 50,
            'stroke_width': 2,
            'node_color': '#4a90e2',
            'node_stroke': '#357abd',
            'edge_color': '#666666',
            'text_color': '#ffffff',
            'font_size': '14px',
            'padding': 40,
        }
        if config:
            self.config.update(config)

    def _get_positions(self, node: 'TreeNode', depth=0, x_counter=[0], positions=None) -> dict:
        """
        透過中序遍歷計算每個節點的 (x, y) 座標。
        返回一個字典，儲存所有節點的佈局資訊。
        """
        if positions is None:
            positions = {}
        if node is None:
            return {}

        # 1. 遞迴訪問左子樹
        self._get_positions(node.left, depth + 1, x_counter, positions)

        # 2. 處理當前節點 (中序位置)
        # 根據中序遍歷的順序，賦予 x 座標
        x = x_counter[0] * self.config['h_spacing']
        y = depth * self.config['v_spacing']

        # 使用 id(node) 作為唯一鍵，避免節點值重複時出錯
        positions[id(node)] = {
            'x': x, 'y': y, 'val': node.val,
            'left_id': id(node.left) if node.left else None,
            'right_id': id(node.right) if node.right else None
        }
        x_counter[0] += 1

        # 3. 遞迴訪問右子樹
        self._get_positions(node.right, depth + 1, x_counter, positions)

        return positions

    def _generate_svg_elements(self, positions: dict) -> tuple[list, int, int]:
        """根據位置資訊產生 SVG 元素字串並計算畫布大小"""
        cfg = self.config
        svg_elements = []
        max_x, max_y = 0, 0

        # Pass 1: 繪製線條 (先畫線條，確保節點在上方)
        for node_id, pos in positions.items():
            if pos['x'] > max_x: max_x = pos['x']
            if pos['y'] > max_y: max_y = pos['y']

            # 連接到左子節點的線
            if pos['left_id'] and pos['left_id'] in positions:
                child_pos = positions[pos['left_id']]
                svg_elements.append(
                    f'<line x1="{pos["x"]}" y1="{pos["y"]}" x2="{child_pos["x"]}" y2="{child_pos["y"]}" '
                    f'stroke="{cfg["edge_color"]}" stroke-width="{cfg["stroke_width"]}" />'
                )
            # 連接到右子節點的線
            if pos['right_id'] and pos['right_id'] in positions:
                child_pos = positions[pos['right_id']]
                svg_elements.append(
                    f'<line x1="{pos["x"]}" y1="{pos["y"]}" x2="{child_pos["x"]}" y2="{child_pos["y"]}" '
                    f'stroke="{cfg["edge_color"]}" stroke-width="{cfg["stroke_width"]}" />'
                )

        # Pass 2: 繪製節點 (圓形和文字)
        for node_id, pos in positions.items():
            # 圓形
            svg_elements.append(
                f'<circle cx="{pos["x"]}" cy="{pos["y"]}" r="{cfg["radius"]}" '
                f'fill="{cfg["node_color"]}" stroke="{cfg["node_stroke"]}" stroke-width="{cfg["stroke_width"]}" />'
            )
            # 文字
            svg_elements.append(
                f'<text x="{pos["x"]}" y="{pos["y"]}" fill="{cfg["text_color"]}" '
                f'font-family="Arial, sans-serif" font-size="{cfg["font_size"]}" '
                f'text-anchor="middle" dy=".3em">{pos["val"]}</text>'
            )

        width = max_x + cfg['padding'] * 2
        height = max_y + cfg['padding'] * 2

        return svg_elements, width, height

    def render(self, root: 'TreeNode', output_filename: str):
        """
        公開方法，將傳入的根節點渲染成一張 SVG 圖片。

        :param root: 樹的根節點。
        :param output_filename: 輸出的 SVG 檔案名稱，例如 'tree.svg'。
        """
        if not root:
            print("錯誤：樹是空的，無法產生 SVG。", file=sys.stderr)
            return

        # 1. 計算所有節點的座標
        positions = self._get_positions(root)

        # 2. 產生 SVG 元素並取得畫布大小
        elements, width, height = self._generate_svg_elements(positions)

        # 3. 組合最終的 SVG 內容
        padding = self.config['padding']
        # 使用 <g> 標籤和 transform 來統一添加邊距
        svg_content = (
            f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
            f'  <g transform="translate({padding}, {padding})">\n'
            + '    ' + '\n    '.join(elements) + '\n'
            f'  </g>\n'
            f'</svg>'
        )

        # 4. 寫入檔案
        try:
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(svg_content)
            print(f"成功將樹渲染至檔案：{output_filename}")
        except IOError as e:
            print(f"寫入檔案 {output_filename} 時發生錯誤: {e}", file=sys.stderr)
