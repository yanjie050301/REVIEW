#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import binascii
import struct

IP: str = '192.168.19.192'
PORT: int = 8018


# 计算指令报文长度，用于放到报文头
def cal_len(Data):
    length = len(Data)
    if length > 65535:
        print("length too long.")
    else:
        data_length = struct.pack('>H', length)
        return data_length


def data_encode(Data):
    data = Data.encode('utf-8')
    return data


def rsa_exp_key_tv(key_idx, pubkey_mac):
    key_idx_str = "K%04d" % key_idx

    cmd = data_encode("TV")
    pad = data_encode("01")
    key_type = data_encode("00A")
    key_exp_idx = data_encode(key_idx_str)
    dis_rank = data_encode("00")
    dis_fact = data_encode("")
    rsa_idx = data_encode("K9999")
    rsa_pub = bytes().fromhex(
        '30818902818100BD9973A3F0D38E8F377AEC581E1F0FF7901FE22A274594C8FCEB8B05FC021A2CFD37D04A077DD5B85EE0A75CE4A3E9830568D1A24CAAC86E1778D14D04E5ED45D53AB7BFE9A2AFF02074ABD3EBD13AFCADEFE0424267DA99381C9C9519699F810690E5E90C42AD1305D0F3B6EE8B770E2EBC431893E7C1405337854821C4F4B50203010001')
    auth_dat = data_encode("1;")
    pub_mac = bytes().fromhex(pubkey_mac)
    # pub_mac = bytes().fromhex('04FFE6A3')

    data = cmd + pad + key_type + key_exp_idx + dis_rank + dis_fact + rsa_idx + rsa_pub + auth_dat + pub_mac
    data_len = cal_len(data)
    # print(data_len, type(data_len), len(data_len))
    message = data_len + data
    # print("请求指令:\n", data)
    # print("请求指令(十六进制):\n", binascii.b2a_hex(data))
    return message


def cmd_KG(key_idx):
    key_idx_str = "%04d" % key_idx

    cmd = data_encode("KG")
    cmd_key_idx = data_encode(key_idx_str)

    cmd_snd = cmd + cmd_key_idx
    cmd_snd_len = cal_len(cmd_snd)

    req = cmd_snd_len + cmd_snd

    return req


def cmd_AM(zmk, key_alg):
    cmd = data_encode("AM")
    cmd_key_type = data_encode("000")
    cmd_key_alg = data_encode(key_alg)
    cmd_xor_flg = data_encode("00")
    cmd_xor_count = data_encode("02")
    cmd_xor_component1 = data_encode(zmk)
    len_zmk = len(zmk)
    cmd_xor_component2 = data_encode("00".zfill(len_zmk))

    cmd_snd = cmd + cmd_key_type + cmd_key_alg + cmd_xor_flg + cmd_xor_count + cmd_xor_component1 + cmd_xor_component2
    cmd_snd_len = cal_len(cmd_snd)

    req = cmd_snd_len + cmd_snd

    return req


def cmd_A8(index, zmk, key_type, key_alg):
    key_idx_str = "K%04d" % index

    cmd = data_encode("A8")
    # exp_key_type = data_encode("000")
    cmd_exp_key_type = data_encode(key_type)
    cmd_zmk_by_lmk = data_encode(zmk)
    cmd_exp_key_idx = data_encode(key_idx_str)
    cmd_key_alg = data_encode(key_alg)

    cmd_snd = cmd + cmd_exp_key_type + cmd_zmk_by_lmk + cmd_exp_key_idx + cmd_key_alg
    cmd_snd_len = cal_len(cmd_snd)

    req = cmd_snd_len + cmd_snd

    return req


def cmd_A6(index, zmk, key_by_zmk, key_type, key_alg):
    key_idx_str = "K%04d" % index

    cmd = data_encode("A6")
    # exp_key_type = data_encode("000")
    cmd_key_type = data_encode(key_type)
    cmd_zmk_by_lmk = data_encode(zmk)
    cmd_key_by_zmk = data_encode(key_by_zmk)
    cmd_key_alg = data_encode(key_alg)
    cmd_key_idx = data_encode(key_idx_str)
    cmd_label_len = data_encode("00")
    cmd_label = data_encode("")

    cmd_snd = cmd + cmd_key_type + cmd_zmk_by_lmk + cmd_key_by_zmk + cmd_key_alg + cmd_key_idx + cmd_label_len
    cmd_snd_len = cal_len(cmd_snd)

    req = cmd_snd_len + cmd_snd

    return req


def cmd_TR(index, zmk):
    key_idx_str = "K%04d" % index

    cmd_code = "TR"    # 命令代码
    cmd_enc_mode = "00"             # 加密算法模式 00-ECB; 01-CBC
    cmd_protect_key_type = "000"    # 保护密钥类型 000-KEK; 109-MDK
    cmd_protect_key = zmk           # 保护密钥密文
    cmd_disperse_level = "00"       # 保护密钥分散级数
    cmd_disperse_factor = ""        # 保护密钥分散因子
    cmd_key_index = key_idx_str     # 被导出密钥索引标识 + 被导出密钥索引号
    cmd_pri_key_cipher_len = ""     # 被导出密钥私钥长度
    cmd_pri_key_cipher = ""         # 被导出密钥私钥数据
    cmd_exp_flg = ""                # 扩展标识
    cmd_padding_flg = ""            # PAD 标识
    cmd_output_fmt = ""             # 输出格式
    cmd_iv = ""                     # IV

    cmd_snd = cmd_code + cmd_enc_mode + cmd_protect_key_type + cmd_protect_key + cmd_disperse_level \
              + cmd_disperse_factor + cmd_key_index + cmd_pri_key_cipher_len + cmd_pri_key_cipher \
              + cmd_exp_flg + cmd_padding_flg + cmd_output_fmt + cmd_iv

    cmd_snd_byte = data_encode(cmd_snd)
    cmd_snd_len_byte = cal_len(cmd_snd_byte)

    req = cmd_snd_len_byte + cmd_snd_byte
    return req


def cmd_TS(index, zmk, export_body):
    key_idx_str = "K%04d" % index

    cmd_code = "TS"                 # 命令代码
    cmd_enc_mode = "00"             # 加密算法模式 00-ECB; 01-CBC
    cmd_protect_key_type = "000"    # 保护密钥类型 000-KEK; 109-MDK
    cmd_protect_key = zmk           # 保护密钥密文
    cmd_disperse_level = "00"       # 保护密钥分散级数
    cmd_disperse_factor = ""        # 保护密钥分散因子
    cmd_key_index = key_idx_str     # 被导出密钥索引标识 + 被导出密钥索引号
    cmd_label = ""
    cmd_label_len = "%02d" % len(cmd_label)
    cmd_pri_key_cipher = bytes.fromhex(export_body)     # 公钥明文 + 私钥d/P/Q/dP/dQ/Qinv

    if 1 <= index <= 64:
        cmd_snd = cmd_code + cmd_enc_mode + cmd_protect_key_type + cmd_protect_key + cmd_disperse_level \
                  + cmd_disperse_factor + cmd_key_index + cmd_label_len + cmd_label
    else:
        cmd_snd = cmd_code + cmd_enc_mode + cmd_protect_key_type + cmd_protect_key + cmd_disperse_level \
                  + cmd_disperse_factor + cmd_key_index

    cmd_snd_byte = data_encode(cmd_snd) + cmd_pri_key_cipher
    cmd_snd_len_byte = cal_len(cmd_snd_byte)

    req = cmd_snd_len_byte + cmd_snd_byte
    return req


def cmd_TT(index, zmk):
    key_idx_str = "%04d" % index

    cmd_code = "TT"                 # 命令代码
    cmd_enc_mode = "00"             # 加密算法模式 00-ECB; 01-CBC
    cmd_protect_key_type = "000"    # 保护密钥类型 000-KEK; 109-MDK
    cmd_protect_key = zmk           # 保护密钥密文
    cmd_disperse_level = "00"       # 保护密钥分散级数
    cmd_disperse_factor = ""        # 保护密钥分散因子
    cmd_curve_id = "07"             # 曲线标识
    cmd_key_index = key_idx_str     # 被导出密钥索引标识 + 被导出密钥索引号
    cmd_pri_key_cipher_len = ""     # 被导出密钥私钥长度
    cmd_pri_key_cipher = ""         # 被导出密钥私钥数据

    cmd_snd = cmd_code + cmd_enc_mode + cmd_protect_key_type + cmd_protect_key + cmd_disperse_level \
              + cmd_disperse_factor + cmd_curve_id + cmd_key_index + cmd_pri_key_cipher_len + cmd_pri_key_cipher

    cmd_snd_byte = data_encode(cmd_snd)
    cmd_snd_len_byte = cal_len(cmd_snd_byte)

    req = cmd_snd_len_byte + cmd_snd_byte
    return req


def cmd_TU(index, zmk, export_body):
    key_idx_str = "%04d" % index

    cmd_code = "TU"                 # 命令代码
    cmd_enc_mode = "00"             # 加密算法模式 00-ECB; 01-CBC
    cmd_protect_key_type = "000"    # 保护密钥类型 000-KEK; 109-MDK
    cmd_protect_key = zmk           # 保护密钥密文
    cmd_disperse_level = "00"       # 保护密钥分散级数
    cmd_disperse_factor = ""        # 保护密钥分散因子
    cmd_curve_id = "07"             # 曲线标识
    cmd_key_index = key_idx_str     # 被导出密钥索引标识 + 被导出密钥索引号
    cmd_label = ""
    cmd_label_len = "%02d" % len(cmd_label)
    cmd_pri_key_cipher = bytes.fromhex(export_body)     # 公钥明文 + 私钥

    if index != 9999:
        cmd_snd = cmd_code + cmd_enc_mode + cmd_protect_key_type + cmd_protect_key + cmd_disperse_level \
                  + cmd_disperse_factor + cmd_curve_id + cmd_key_index + cmd_label_len + cmd_label
    else:
        cmd_snd = cmd_code + cmd_enc_mode + cmd_protect_key_type + cmd_protect_key + cmd_disperse_level \
                  + cmd_disperse_factor + cmd_curve_id + cmd_key_index

    cmd_snd_byte = data_encode(cmd_snd) + cmd_pri_key_cipher
    cmd_snd_len_byte = cal_len(cmd_snd_byte)

    req = cmd_snd_len_byte + cmd_snd_byte
    return req


if __name__ == '__main__':
    # 建立连接
    cln = socket.socket()
    cln.connect((IP, PORT))

    for idx in range(1, 1 + 1):

        # msg = rsa_exp_key_tv(idx, "04FFE6A3")
        #
        # # 指令响应
        # cln.send(msg)
        # rcv_full = cln.recv(1024)
        # rcv = rcv_full[2:]
        # rcv_full_hex = binascii.b2a_hex(rcv)
        # rcv_cmd = rcv[0:2].decode('ascii')
        # rcv_err = rcv[2:4].decode('ascii')
        # # 响应指令十六进制输出
        # # print("响应报文:\n", rcv_full_hex)
        # # print(rcv_cmd, rcv_err, rcv_cipher_len)
        # if rcv_err != "00":
        #     print("索引位置[%d], 指令响应出错，错误码为[%s]" % (idx, rcv_err))
        # else:
        #     rcv_cipher_len = rcv[4:8]
        #     rcv_cipher = rcv[8:int(rcv_cipher_len, 16) + 8]
        #     rcv_chk = rcv[-16:]
        #
        #     print("索引位置[%d], RSA加密密钥密文:\n" % idx, binascii.b2a_hex(rcv_cipher).decode('ascii'))
        #     print("对称密钥校验值:\n", rcv_chk.decode('ascii'))
        """"""
        # msg_TR = cmd_TR(idx, "X48864EA979EE933748864EA979EE9337")
        # cipher = ""
        #
        # cln.send(msg_TR)
        # rcv_full_byte = cln.recv(2048)
        # rcv_resp_byte = rcv_full_byte[2:]
        # rcv_resp_hex = binascii.b2a_hex(rcv_resp_byte).decode('ascii')
        # rcv_cmd_asc = rcv_resp_byte[0:2].decode('ascii')
        # rcv_err_asc = rcv_resp_byte[2:4].decode('ascii')
        # # print(rcv_cmd_asc, rcv_err_asc)
        # if rcv_err_asc != "00":
        #     print("索引位置[%d], 指令响应出错，错误码为[%s]" % (idx, rcv_err_asc))
        # else:
        #     # rcv_exp_key_by_zmk = rcv_resp[4:37]
        #     # rcv_exp_key_chk = rcv_resp[-16:]
        #     # print("索引位置[%d], 导出密钥密文:[%s], 导出密钥校验值:[%s]\n"
        #     #       % (idx, rcv_exp_key_by_zmk.decode('ascii'), rcv_exp_key_chk.decode('ascii')))
        #     print("索引位置[%d], 指令响应(Hex):[%s]\n"
        #           % (idx, rcv_resp_hex))
        #
        #     offset = 0
        #     offset += 4
        #
        #     len_t = 1
        #     pub_der_t = binascii.b2a_hex(rcv_resp_byte[offset: offset + len_t])
        #     offset += len_t
        #
        #     len_l_1st = 1
        #     pub_der_l_1st = binascii.b2a_hex(rcv_resp_byte[offset: offset + len_l_1st])
        #     offset += len_l_1st
        #
        #     len_l_other = 0
        #     if pub_der_l_1st == b'81':
        #         len_l_other = 1
        #     if pub_der_l_1st == b'82':
        #         len_l_other = 2
        #     else:
        #         print("error")
        #
        #     der_l_other = binascii.b2a_hex(rcv_resp_byte[offset: offset + len_l_other])
        #     offset += len_l_other
        #
        #     len_v = int(der_l_other.decode('ascii'), 16)
        #     # print(len_v)
        #     pub_der_v = binascii.b2a_hex(rcv_resp_byte[offset: offset + len_v])
        #     offset += len_v
        #     # print(pub_der_v.decode('ascii'))
        #
        #     pri_cipher = binascii.b2a_hex(rcv_resp_byte[offset:])
        #     # print(pri_cipher.decode('ascii'))
        #
        #     cipher = binascii.b2a_hex(rcv_resp_byte[4:]).decode('ascii')
        #     print(cipher)
        #
        # msg_TS = cmd_TS(9999, "X48864EA979EE933748864EA979EE9337", cipher)
        # print(msg_TS)
        #
        # cln.send(msg_TS)
        # rcv_full_byte_TS = cln.recv(2048)
        # rcv_resp_byte_TS = rcv_full_byte_TS[2:]
        # rcv_resp_hex_TS = binascii.b2a_hex(rcv_resp_byte_TS).decode('ascii')
        # rcv_cmd_asc_TS = rcv_resp_byte_TS[0:2].decode('ascii')
        # rcv_err_asc_TS = rcv_resp_byte_TS[2:4].decode('ascii')
        # if rcv_err_asc_TS != "00":
        #     print("索引位置[%d], 指令响应出错，错误码为[%s]" % (idx, rcv_err_asc_TS))
        # else:
        #     # rcv_exp_key_by_zmk = rcv_resp[4:37]
        #     # rcv_exp_key_chk = rcv_resp[-16:]
        #     # print("索引位置[%d], 导出密钥密文:[%s], 导出密钥校验值:[%s]\n"
        #     #       % (idx, rcv_exp_key_by_zmk.decode('ascii'), rcv_exp_key_chk.decode('ascii')))
        #     print("索引位置[%d], 指令响应(Hex):[%s]\n"
        #           % (idx, rcv_resp_hex_TS))
        #
        #     cipher_TS = binascii.b2a_hex(rcv_resp_byte_TS[8:]).decode('ascii')
        #     print(cipher_TS)
        """"""
        msg_TT = cmd_TT(idx, "RC8E2CD5E7944ACEDC8E2CD5E7944ACED")
        cipher = ""
        print(msg_TT)

        cln.send(msg_TT)
        rcv_full_byte = cln.recv(2048)
        rcv_resp_byte = rcv_full_byte[2:]
        rcv_resp_hex = binascii.b2a_hex(rcv_resp_byte).decode('ascii')
        rcv_cmd_asc = rcv_resp_byte[0:2].decode('ascii')
        rcv_err_asc = rcv_resp_byte[2:4].decode('ascii')
        print(rcv_cmd_asc, rcv_err_asc)

        if rcv_err_asc != "00":
            print("索引位置[%d], 指令响应出错，错误码为[%s]" % (idx, rcv_err_asc))
        else:
            # rcv_exp_key_by_zmk = rcv_resp[4:37]
            # rcv_exp_key_chk = rcv_resp[-16:]
            # print("索引位置[%d], 导出密钥密文:[%s], 导出密钥校验值:[%s]\n"
            #       % (idx, rcv_exp_key_by_zmk.decode('ascii'), rcv_exp_key_chk.decode('ascii')))
            print("索引位置[%d], 指令响应(Hex):[%s]\n"
                  % (idx, rcv_resp_hex))

            cipher = binascii.b2a_hex(rcv_resp_byte[4:]).decode('ascii')
            print(cipher)

            msg_TU = cmd_TU(1, "RC8E2CD5E7944ACEDC8E2CD5E7944ACED", cipher)
            print(msg_TU)

            cln.send(msg_TU)
            rcv_full_byte_TU = cln.recv(2048)
            rcv_resp_byte_TU = rcv_full_byte_TU[2:]
            rcv_resp_hex_TU = binascii.b2a_hex(rcv_resp_byte_TU).decode('ascii')
            rcv_cmd_asc_TU = rcv_resp_byte_TU[0:2].decode('ascii')
            rcv_err_asc_TU = rcv_resp_byte_TU[2:4].decode('ascii')
            if rcv_err_asc_TU != "00":
                print("索引位置[%d], 指令响应出错，错误码为[%s]" % (idx, rcv_err_asc_TU))
            else:
                # rcv_exp_key_by_zmk = rcv_resp[4:37]
                # rcv_exp_key_chk = rcv_resp[-16:]
                # print("索引位置[%d], 导出密钥密文:[%s], 导出密钥校验值:[%s]\n"
                #       % (idx, rcv_exp_key_by_zmk.decode('ascii'), rcv_exp_key_chk.decode('ascii')))
                print("索引位置[%d], 指令响应(Hex):[%s]\n"
                      % (idx, rcv_resp_hex_TU))

                cipher_TS = binascii.b2a_hex(rcv_resp_byte_TU[8:]).decode('ascii')
                print(cipher_TS)

    # 关闭连接
    cln.close()
