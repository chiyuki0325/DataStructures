from collections import deque


class Solution1:
    # 暴力穷举法
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        waiting_time = delay
        running_time = forget - waiting_time  # 一个人的运行天数
        waiting: deque[int] = deque([delay])  # 初始只有一个人
        running: deque[int] = deque()
        # expired 不存储
        for now in range(1, n + 1):
            # print(f"第 {now} 天")
            # print(f"变更之前: waiting: {list(waiting)}  running: {list(running)}")
            # now 为当前天数

            # 计算死亡
            while len(running) > 0 and now > running[0]:
                # print(f"死亡一人 ({running[0]} < {now})")
                running.popleft()

            # 计算启动
            while len(waiting) > 0 and now > waiting[0]:
                # 第一个人，存储为delay，则在第delay+1天启动
                # print(f"启动一人 ({waiting[0]} < {now}) => {now + running_time - 1}")
                waiting.popleft()
                running.append(now + running_time - 1)

            # 再计算传染
            for running_man in running:
                # print(f"{running_man} 传染一人")
                waiting.append(now + waiting_time - 1)

            # print(f"变更之后: waiting: {list(waiting)}  running: {list(running)}\n")

        result = len(running) + len(waiting)
        # print(result)
        return result


class Solution2:
    # 方法 1 的优化版本，节省了内存
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        waiting_time = delay
        running_time = forget - waiting_time  # 一个人的运行天数
        waiting: deque[list[int]] = deque([[delay, 1]])  # 初始只有一个人
        running: deque[list[int]] = deque()
        for now in range(2, n + 1):
            # print(f"第 {now} 天")
            # now 为当前天数

            # 计算死亡
            while len(running) > 0 and now > running[0][0]:
                # print(f"死亡 ({running[0]} < {now})")
                running.popleft()

            # 计算启动
            while len(waiting) > 0 and now > waiting[0][0]:
                # 第一个人，存储为delay，则在第delay+1天启动
                # print(f"启动 ({waiting[0]} < {now}) => {now + running_time - 1}")
                die_time = now + running_time - 1
                count = waiting.popleft()[1]
                if len(running) == 0 or running[-1][0] != die_time:
                    running.append([die_time, count])
                else:
                    running[-1][1] += count

            # 再计算传染
            for running_men in running:
                # print(f"{running_men[0]} 传染 {running_men[1]} 人")
                launch_time = now + waiting_time - 1
                count = running_men[1]
                if len(waiting) == 0 or waiting[-1][0] != launch_time:
                    waiting.append([launch_time, count])
                else:
                    waiting[-1][1] += count

            # print(f"变更之后: waiting: {list(waiting)}  running: {list(running)}\n")

        result = (
            sum(count for _, count in running) + sum(count for _, count in waiting)
        ) % (10**9 + 7)
        # print(result)
        return result


class Solution:
    # 看了题解后重写的版本，最简单易懂
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        people = [0] * (n + 1)
        # people 存的是第 n 天被启动的人数
        people[1] = 1  # 初始 1 人
        waiting_time = delay
        running_time = forget - waiting_time  # 一个人的运行天数
        MOD = 10**9 + 7

        for now in range(2, n + 1):
            # 时间轴: [   死亡   ]([  运行中  ])[  冷却  ][今天]
            for running_day in range(max(1, now - forget + 1), now - delay + 1):
                # 处于“运行中“段落的人可以传播秘密
                people[now] += people[running_day]
                people[now] %= MOD
            # 推演完毕

        # 此时，people[n] 只是当天启动的人
        # 要加上之前启动了还没死的人

        alive = 0
        for running_day in range(max(1, n - forget + 1), n + 1):
            alive += people[running_day]

        return alive % MOD


if __name__ == "__main__":
    assert Solution().peopleAwareOfSecret(6, 2, 4) == 5
    assert Solution().peopleAwareOfSecret(4, 1, 3) == 6
    # print(Solution().peopleAwareOfSecret(684, 18, 496))
