# 经验池,用于记录之前取的数据点.
# 具体机制:
#         采样得到的点,放入缓冲池中,记录total_size
#         太少时,全部用于学习
#         达到一个阈值thread后,之前的数据点逐渐减少权重
#         分阶段
#         前20%选择权重为0.80
#         20%-40% 权重为0.20
#         40%-60% 权重为0.10
#         60%-100% 权重为0.10
#         更新时,随机抽取total_size中75%的数据点,用于更新GP
#         达到缓冲区上限max_size后,超出部分直接丢弃掉

import numpy as np

class ExpItem(object):
    # 封装,解封装
    def __init__(self):
        self.item=None
    def compress(self,new_object):
        self.item=new_object
    def uncompress(self):
        return self.item

class ExpBuffer(object):
    def __init__(self, max_size=100):
        # 记录所有的数据点
        self.exp_buffer = []
        # 最大长度
        self.max_size = max_size
        # 门限,设定为最大长度的20%,超过20%后就需要更新数据了
        # 会返回大小为thread1的real_exp
        self.thread1 = int(self.max_size * 0.2)
        self.thread2 = int(self.max_size * 0.4)
        self.thread3 = int(self.max_size * 0.6)
        self.thread4 = self.max_size

        self.weight = [0.8, 0.2, 0.1, 0.1]

    # 维护缓冲区
    def add_point(self, point):
        new_item=ExpItem()
        new_item.compress(point)
        total_num = len(self.exp_buffer)
        if total_num < self.max_size:
            self.exp_buffer.append(new_item)
        elif total_num >= self.max_size:
            self.exp_buffer = self.exp_buffer[1:]
            self.exp_buffer.append(new_item)

    # 返回用于更新GP的数据点
    def get_real_exp(self):
        real_exp = []
        total_num = len(self.exp_buffer)
        # 完全的权重
        if total_num <= self.thread1:
            real_exp = np.random.choice(self.exp_buffer, size=total_num,replace=False)
        # 权重99/1分
        elif self.thread1 < total_num and total_num <= self.thread2:
            # 记录是否被选择
            weight = [0.99 / self.thread1] * self.thread1 + [0.01 / (total_num - self.thread1)] * (
                        total_num - self.thread1)
            real_exp = np.random.choice(self.exp_buffer, size=self.thread1, replace=False, p=weight)
        # 权重95/4/1分
        elif self.thread2 < total_num and total_num <= self.thread3:
            weight = [0.95 / self.thread1] * self.thread1 + [0.04 / (self.thread2 - self.thread1)] * (
                        self.thread2 - self.thread1) + [0.01 / (total_num - self.thread2)] * (total_num - self.thread2)
            real_exp = np.random.choice(self.exp_buffer, size=self.thread1, replace=False, p=weight)
        # 权重90/5/4/1分
        elif self.thread3 < total_num and total_num <= self.thread4:
            weight = [0.90 / self.thread1] * self.thread1 + [0.05 / (self.thread2 - self.thread1)] * (
                        self.thread2 - self.thread1) + [0.04 / (self.thread3 - self.thread2)] * (
                                 self.thread3 - self.thread2) + [0.01 / (total_num - self.thread3)] * (
                                 total_num - self.thread3)
            real_exp = np.random.choice(self.exp_buffer, size=self.thread1, replace=False, p=weight)

        real_items=[]
        for i in real_exp:
            real_items.append(i.uncompress())
        return real_items


if __name__ == '__main__':
    buffer = ExpBuffer(max_size=20)

    for i in range(100):
        buffer.add_point(i)
        # print(buffer.exp_buffer)
        real_buffer = buffer.get_real_exp()
        print(real_buffer)
