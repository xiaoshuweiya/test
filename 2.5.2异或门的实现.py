# 定义 NAND 函数
def NAND(x1, x2):
    w1, w2, theta = -0.5, -0.5, -0.7  # NAND 的权重和阈值
    tmp = x1 * w1 + x2 * w2
    return 0 if tmp <= theta else 1

# 定义 OR 函数
def OR(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.3  # OR 的权重和阈值
    tmp = x1 * w1 + x2 * w2
    return 0 if tmp <= theta else 1

# 定义 AND 函数
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7  # AND 的权重和阈值
    tmp = x1 * w1 + x2 * w2
    return 0 if tmp <= theta else 1

# 定义 XOR 函数
def XOR(x1, x2):
    s1 = NAND(x1, x2)  # 计算 NAND
    s2 = OR(x1, x2)    # 计算 OR
    y = AND(s1, s2)    # 计算 AND
    return y

# 测试 XOR 函数
print(XOR(0, 0))  # 输出 0
print(XOR(0, 1))  # 输出 1
print(XOR(1, 0))  # 输出 1
print(XOR(1, 1))  # 输出 0