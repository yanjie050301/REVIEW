

MaxTime = 16

# 生成子密钥的置换表1，将64位的密钥转换为56位
key_table1 = [
    57, 49, 41, 33, 25, 17,  9,
    1,  58, 50, 42, 34, 26, 18,
    10,  2, 59, 51, 43, 35, 27,
    19, 11,  3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7,  62, 54, 46, 38, 30, 22,
    14,  6, 61, 53, 45, 37, 29,
    21, 13,  5, 28, 20, 12,  4
]

# 生成子密钥的置换表2，将56位的密钥转换为48位
key_table2 = [
    14, 17, 11, 24,  1,  5,
    3,  28, 15,  6, 21, 10,
    23, 19, 12,  4, 26,  8,
    16,  7, 27, 20, 13,  2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

# IP置换表
IP_table = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17,  9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# 逆IP置换表
Inv_IP_table = [
    40,  8, 48, 16, 56, 24, 64, 32,
    39,  7, 47, 15, 55, 23, 63, 31,
    38,  6, 46, 14, 54, 22, 62, 30,
    37,  5, 45, 13, 53, 21, 61, 29,
    36,  4, 44, 12, 52, 20, 60, 28,
    35,  3, 43, 11, 51, 19, 59, 27,
    34,  2, 42, 10, 50, 18, 58, 26,
    33,  1, 41,  9, 49, 17, 57, 25
]

# S盒中的S1盒
S1 = [
    14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
    0,  15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
    4,   1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
    15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13
]
# S盒中的S2盒
S2 = [
    15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10,
    3,  13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5,
    0,  14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15,
    13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9
]
# S盒中的S3盒
S3 = [
    10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,
    13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,
    13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7,
    1,  10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12
]
# S盒中的S4盒
S4 = [
    7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15,
    13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9,
    10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4,
    3,  15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14
]
# S盒中的S5盒
S5 = [
    2,  12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9,
    14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6,
    4,   2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14,
    11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3
]
# S盒中的S6盒
S6 = [
    12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11,
    10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,
    9,  14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6,
    4,   3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13
]
# S盒中的S7盒
S7 = [
    4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1,
    13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6,
    1,   4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2,
    6,  11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12
]
# S盒中的S8盒
S8 = [
    13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7,
    1,  15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2,
    7,  11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8,
    2,   1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11
]
# S盒
S = [S1, S2, S3, S4, S5, S6, S7, S8]
# 用于对数据进行扩展置换，将32bit数据扩展为48bit
extend_table = [
    32,  1,  2,  3,  4,  5,
    4,   5,  6,  7,  8,  9,
    8,   9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32,  1
]
# P盒
P_table = [
    16,  7, 20, 21, 29, 12, 28, 17,
    1,  15, 23, 26,  5, 18, 31, 10,
    2,   8, 24, 14, 32, 27,  3,  9,
    19, 13, 30,  6, 22, 11,  4, 25
]


def Listmove(l, step):    # 将列表中的元素循环左移
    return l[step:] + l[:step]


def Subkey(key):    # 生成子密钥
    keyresult = []
    key0 = [0 for i in range(56)]

    for i in range(len(key_table1)):
        key0[i] = key[key_table1[i]-1]

    # 生成16个密钥
    for i in range(MaxTime):
        key1 = [0 for i in range(48)]
        # 确定每次左移的步数
        if i == 0 or i == 1 or i == 8 or i == 15:
            step = 1
        else:
            step = 2
        # 分成两组
        tmp1 = key0[0:28]
        tmp2 = key0[28:56]
        # 循环左移
        tmp1 = Listmove(tmp1, step)
        tmp2 = Listmove(tmp2, step)
        # 左右连接
        key0 = tmp1 + tmp2
        # 置换选择
        for i in range(len(key_table2)):
            key1[i] = key0[key_table2[i]-1]
        # 生成密钥
        keyresult.append(key1)
    # 返回的是一个集合包含了每次的密钥
    return keyresult


def int2bit(n): # 0~15整数转比特
    a = []
    for i in range(0,4):
        a.insert(0,str(n%2))
        n=int(n/2)
    return a


# IP置换部分，op为0表示正置换，op为1表示逆置换
def IP(text, op):
    tmp = [0 for i in range(64)]
    if op == 0:
        for i in range(64):
            tmp[i] = text[IP_table[i]-1]
        return tmp
    if op == 1:
        for i in range(64):
            tmp[i] = text[Inv_IP_table[i]-1]
        return tmp


# 进行扩展，将32位扩展为48位
def Extend(text):
    extend = [0 for i in range(48)]
    for i in range(48):
        extend[i] = text[extend_table[i] - 1]
    return extend


# S盒变换部分
def S_replace(text):
    Sresult = [0 for k in range(32)]
    for k in range(8):
        row = 2*int(text[k*6]) + int(text[k*6+5])
        column = 8*int(text[k*6+1]) + 4*int(text[k*6+2]) + 2*int(text[k*6+3]) + int(text[k*6+4])
        tmp = S[k][row*16+column]

        for i in range(4):
            Sresult[4 * k + i] = int2bit(tmp)[i]
    return Sresult


# P置换部分
def P_replace(text):
    Presult = [0 for i in range(32)]
    for i in range(32):
        Presult[i] = text[P_table[i]-1]
    return Presult


# 异或运算
def Xor(bit1, bit2):
    Xorresult = [0 for i in range(len(bit1))]
    for i in range(len(bit1)):
        Xorresult[i] = str(int(bit1[i]) ^ int(bit2[i]))
    return Xorresult


# 十六进制转二进制比特串
def Hex2bin(text):
    result = []
    for i in range(len(text)):
        result.extend(int2bit(int(text[i], 16)))
    return result


# 二进制比特串转十六进制
def bin2Hex(text):
    result = []
    q = len(text)//4
    for i in range(q):
        dec = int(text[4*i])*8 + int(text[4*i+1])*4 + int(text[4*i+2])*2 + int(text[4*i+3])*1
        x = hex(dec)[2:].upper()
        result.extend(x)
    rs = ''.join(result)
    return rs


# 按照DES算法的流程图进行运算
def Encryption(text, keybit):
    keylist = Subkey(keybit)
    text1 = IP(text, 0)  # IP置换
    L = [text1[i] for i in range(32)]
    R = [text1[i] for i in range(32, 64)]
    for i in range(16):
        tmp = R
        tmp = Extend(tmp)
        tmp = Xor(tmp, keylist[i])
        tmp = S_replace(tmp)
        tmp = P_replace(tmp)
        tmp = Xor(tmp, L)
        L = R
        R = tmp
    L, R = R, L
    ctext = L
    ctext.extend(R)
    ctext = IP(ctext, 1)
    return bin2Hex(ctext)


if __name__ == '__main__':
    plaintext = input('请输入用十六进制表示的明文：')
    key = input('请输入用十六进制表示的密钥：')
    ptext = Hex2bin(plaintext)
    keybit = Hex2bin(key)
    print('输出的密文为：' + Encryption(ptext, keybit))
