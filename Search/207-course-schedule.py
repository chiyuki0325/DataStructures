from typing import List


class Solution1:
    # 第一版，太慢了，过不去样例
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 根据题目的分类得出，此题目为“判断有向图中是否存在环”问题

        # 使用数组储存依赖关系
        dependencies = [[] for _ in range(numCourses)]
        for this, next in prerequisites:
            dependencies[this].append(next)

        for course in range(numCourses):
            # print("test course", course)
            if dependencies[course]:
                # 该课程存在依赖关系
                def has_cycled_dependency(c, is_visited: List[bool]) -> bool:
                    # print("call", c)
                    if is_visited[c]:
                        return True
                    is_visited[c] = True

                    result = False
                    for dep in dependencies[c]:
                        if has_cycled_dependency(dep, is_visited.copy()):
                            result = True
                    return result

                if has_cycled_dependency(course, [False] * numCourses):
                    return False

        return True


class Solution:
    # 灵神题解版本，把“已访问”分为两种
    # 既然之前的方法难以储存“路径”，要复制大量is_visited导致空间爆炸
    # 何不直接拓展状态的种类？

    # 0: 未访问，1: 搜索中，撞到表示有环
    # 2: 跳过，走到这个节点表示彻底无环
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 使用数组储存依赖关系
        dependencies = [[] for _ in range(numCourses)]
        for this, next in prerequisites:
            dependencies[this].append(next)

        colors = [0] * numCourses

        def has_cycled_dependency(c) -> bool:
            colors[c] = 1

            for dep in dependencies[c]:
                if colors[dep] == 1:
                    return True
                elif colors[dep] == 0:
                    if has_cycled_dependency(dep):
                        return True
                # 2 跳过

            colors[c] = 2
            return False

        for course, color in enumerate(colors):
            if color == 0 and has_cycled_dependency(course):
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    assert s.canFinish(2, [[1, 0]]) == True
    assert s.canFinish(2, [[1, 0], [0, 1]]) == False
    assert s.canFinish(3, [[1, 0], [1, 2], [0, 1]]) == False
    assert s.canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]) == True
