#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""多线程异步处理逻辑"""
import binascii
import threading
import subprocess
import logging
import csv
import time
from pubsub import pub
from socket import *
from RyanTools import Hsm

KEY_ALG_FLAGS = ['Z', 'X', 'Y', 'R', 'P', 'L', 'M', 'N', 'U', 'T']


def win_cmd(command):
    sub_p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, encoding="gbk")
    sub_p.wait(2)
    if sub_p.poll() == 0:
        return sub_p.communicate()[0][:-1]
    else:
        return "failed"


class ThreadScanIPs(threading.Thread):
    def __init__(self, ip_seg, ip_from, ip_to):
        self.logger = logging.getLogger("MainFrame.ScanIpTools")

        """Init Worker Thread Class."""
        threading.Thread.__init__(self)
        self.ip_segment = ip_seg
        self.ip_from = int(ip_from)
        self.ip_to = int(ip_to)
        self.start()

    def run(self):
        """Run Worker Thread."""
        pub.sendMessage("scan_ip", info='Start scan %s.x...\n' % self.ip_segment)
        reachable_ip_cnt, unreachable_ip_cnt = self.ScanIPs(self.ip_segment, self.ip_from, self.ip_to)
        pub.sendMessage("scan_ip", info="Finish!\n")
        pub.sendMessage("scan_ip", info="Total: There are %d reachable IP(s).\n" % reachable_ip_cnt)
        pub.sendMessage("scan_ip", info="Total: There are %d unreachable IP(s).\n" % unreachable_ip_cnt)
        pub.sendMessage("scan_ip", info='done\n')

    def ScanIPs(self, ip_segment, ip_from, ip_to):
        reachable_ip_cnt = 0
        unreachable_ip_cnt = 0
        for i in range(ip_from, ip_to):
            command = "ping -n 1 -w 2 %s.%d | find \"回复\"" % (ip_segment, i)
            self.logger.debug("ping 命令:[%s]." % command)
            # res = os.popen(command).read()    # 使用os.popen，打包exe如果关闭命令行菜单会导致命令无法运行

            """
            解决办法:
            使用subprocess.Popen方法调用windows命令，并添加参数
            shell=True, 
            stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
            """
            res = win_cmd(command)
            self.logger.debug("ping 结果:[%s]." % res)
            # if res != "":                     # 使用os.popen，打包exe如果关闭命令行菜单会导致命令无法运行
            if res != "failed":
                detect_ip_hints = res + "\n"
                pub.sendMessage("scan_ip", info='{}'.format(detect_ip_hints))
                reachable_ip_cnt += 1
            else:
                rest_ip_hints = "%s.%d can not reach.\n" % (ip_segment, i)
                pub.sendMessage("scan_ip", info='{}'.format(rest_ip_hints))
                unreachable_ip_cnt += 1
        return reachable_ip_cnt, unreachable_ip_cnt


class ThreadAsySndExpCmd(threading.Thread):
    def __init__(self, client, idx_start, idx_end, zmk):

        self.logger = logging.getLogger("MainFrame.HsmCmd")

        threading.Thread.__init__(self)
        self.cli = client
        self.idx_start = idx_start
        self.idx_end = idx_end
        self.zmk = zmk
        self.start()

    def run(self):
        self.AsySndExpCmd(self.cli, self.idx_start, self.idx_end, self.zmk)
        pub.sendMessage("AsyExpCmd", info="done\n")

    def AsySndExpCmd(self, client, idx_start, idx_end, zmk):
        for idx in range(idx_start, idx_end):
            req_KG = Hsm.cmd_KG(idx)
            client.send(req_KG)
            res_KG_full = client.recv(1024)
            res_KG_effective = res_KG_full[2:]
            res_KG_err = res_KG_effective[2:4].decode('ascii')

            """KG 查看指定索引密钥信息"""
            if res_KG_err != "00":
                resp = "索引位置[%0.4d], KG指令响应出错，错误码为[%s]\n" % (idx, res_KG_err)
                pub.sendMessage("AsyExpCmd", info=resp)

            else:
                key_type = res_KG_effective[4:7].decode('ascii')
                key_alg = res_KG_effective[7:8].decode('ascii')
                if key_alg == 'Z':
                    zmk_plain = zmk[0:16]
                elif key_alg == 'Y' or key_alg == 'M' or key_alg == 'T':
                    zmk_plain = zmk.zfill(48)
                elif key_alg == 'N':
                    zmk_plain = zmk.zfill(64)
                else:
                    zmk_plain = zmk

                """AM 明文合成ZMK密钥"""
                req_AM = Hsm.cmd_AM(zmk_plain, key_alg)
                client.send(req_AM)
                rcv_AM_full = client.recv(1024)
                rcv_AM_effective = rcv_AM_full[2:]
                res_AM_err = rcv_AM_effective[2:4].decode('ascii')
                if res_AM_err != "00":
                    resp = "索引位置[%0.4d], AM指令响应出错，错误码为[%s]\n" % (idx, res_AM_err)
                    pub.sendMessage("AsyExpCmd", info=resp)
                else:
                    if key_alg == "Z":
                        zmk_by_lmk = rcv_AM_effective[4:21]
                    elif key_alg == 'Y' or key_alg == 'M' or key_alg == 'T':
                        zmk_by_lmk = rcv_AM_effective[4:53]
                    elif key_alg == "N":
                        zmk_by_lmk = rcv_AM_effective[4:69]
                    else:
                        zmk_by_lmk = rcv_AM_effective[4:37]

                    """A8 ZMK保护导出指定索引密钥"""
                    req_A8 = Hsm.cmd_A8(idx, zmk_by_lmk.decode('ascii'), key_type, key_alg)

                    self.logger.debug("Export Command:[%s]." % req_A8[2:].decode("ascii"))

                    client.send(req_A8)
                    rcv_A8_full = client.recv(1024)
                    rcv_A8_effective = rcv_A8_full[2:]
                    rcv_A8_err = rcv_A8_effective[2:4].decode('ascii')
                    if rcv_A8_err != "00":
                        resp = "索引位置[%0.4d], A8指令响应出错，错误码为[%s]\n" % (idx, rcv_A8_err)
                        pub.sendMessage("AsyExpCmd", info=resp)
                    else:
                        if key_alg == "Z":
                            rcv_exp_key_by_zmk = rcv_A8_effective[4:21]
                        elif key_alg == 'Y' or key_alg == 'M' or key_alg == 'T':
                            rcv_exp_key_by_zmk = rcv_A8_effective[4:53]
                        elif key_alg == "N":
                            rcv_exp_key_by_zmk = rcv_A8_effective[4:69]
                        else:
                            rcv_exp_key_by_zmk = rcv_A8_effective[4:37]

                        rcv_exp_key_chk = rcv_A8_effective[-16:]
                        resp = "索引位置:[%0.4d], 密钥类型:[%s], 导出密钥密文:[%s], 导出密钥校验值:[%s]\n" \
                               % (idx, key_type, rcv_exp_key_by_zmk.decode('ascii'), rcv_exp_key_chk.decode('ascii'))
                        pub.sendMessage("AsyExpCmd", info=resp)

            # req_A8 = Hsm.cmd_A8(idx, zmk, key_type, key_alg)
            # client.send(req_A8)
            # rcv_full = client.recv(1024)
            # rcv_resp = rcv_full[2:]
            # rcv_err = rcv_resp[2:4].decode('ascii')
            # if rcv_err != "00":
            #     resp = "索引位置[%0.4d], 指令响应出错，错误码为[%s]\n" % (idx, rcv_err)
            #     pub.sendMessage("AsyCmd", info=resp)
            # else:
            #     rcv_exp_key_by_zmk = rcv_resp[4:37]
            #     rcv_exp_key_chk = rcv_resp[-16:]
            #     resp = "索引位置[%0.4d], 导出密钥密文:[%s], 导出密钥校验值:[%s]\n" \
            #         % (idx, rcv_exp_key_by_zmk.decode('ascii'), rcv_exp_key_chk.decode('ascii'))
            #     pub.sendMessage("AsyCmd", info=resp)


class ThreadAsySndImpCmd(threading.Thread):
    def __init__(self, client, path, zmk):

        self.logger = logging.getLogger("MainFrame.HsmCmd")

        threading.Thread.__init__(self)
        self.cli = client
        self.file_path = path
        self.zmk = zmk
        self.start()

    def run(self):
        self.AsySndImpCmd(self.cli, self.file_path, self.zmk)
        pub.sendMessage("AsyImpCmd", info="done\n")

    def AsySndImpCmd(self, client, path, zmk):
        # with open(file_path, 'r', encoding='utf-8') as f:
        #     contents = f.readlines()
        #     for i in range(len(contents)):
        #         # print(i)
        #         key_idx = int(contents[i][1:5])
        #         key_type = contents[i][8:11]
        #         key_alg = contents[i][14]

        with open(path, 'r') as f:
            content = csv.reader(f)
            for record in content:
                key_idx = int(record[0])
                key_type = record[1]
                key_alg = record[2][0]
                key_by_zmk = record[2]
                if key_alg == "Z":
                    zmk_plain = zmk[0:16]
                elif key_alg == 'Y' or key_alg == 'M' or key_alg == 'T':
                    zmk_plain = zmk.zfill(48)
                elif key_alg == "N":
                    zmk_plain = zmk.zfill(64)
                else:
                    zmk_plain = zmk
                # print(key_idx, key_type, key_alg, key_by_zmk, zmk_plain)

                """AM 明文合成ZMK密钥"""
                req_AM = Hsm.cmd_AM(zmk_plain, key_alg)
                client.send(req_AM)
                rcv_AM_full = client.recv(1024)
                rcv_AM_effective = rcv_AM_full[2:]
                res_AM_err = rcv_AM_effective[2:4].decode('ascii')
                if res_AM_err != "00":
                    resp = "索引位置[%0.4d], AM指令响应出错，错误码为[%s]\n" % (key_idx, res_AM_err)
                    pub.sendMessage("AsyImpCmd", info=resp)
                else:
                    if key_alg == "Z":
                        zmk_by_lmk = rcv_AM_effective[4:21]
                    elif key_alg == 'Y' or key_alg == 'M' or key_alg == 'T':
                        zmk_by_lmk = rcv_AM_effective[4:53]
                    elif key_alg == "N":
                        zmk_by_lmk = rcv_AM_effective[4:69]
                    else:
                        zmk_by_lmk = rcv_AM_effective[4:37]

                    req_A6 = Hsm.cmd_A6(key_idx, zmk_by_lmk.decode("ascii"), key_by_zmk, key_type, key_alg)
                    self.logger.debug("Import Command:[%s]." % req_A6[2:].decode("ascii"))

                    client.send(req_A6)
                    rcv_A6_full = client.recv(1024)
                    rcv_A6_effective = rcv_A6_full[2:]
                    rcv_A6_err = rcv_A6_effective[2:4].decode('ascii')
                    if rcv_A6_err != "00":
                        resp = "索引位置[%0.4d], A6指令响应出错，错误码为[%s]\n" % (key_idx, rcv_A6_err)
                        pub.sendMessage("AsyImpCmd", info=resp)
                    else:
                        if key_alg == "Z":
                            rcv_imp_key_by_lmk = rcv_A6_effective[4:21]
                        elif key_alg == 'Y' or key_alg == 'M' or key_alg == 'T':
                            rcv_imp_key_by_lmk = rcv_A6_effective[4:53]
                        elif key_alg == "N":
                            rcv_imp_key_by_lmk = rcv_A6_effective[4:69]
                        else:
                            rcv_imp_key_by_lmk = rcv_A6_effective[4:37]

                        rcv_imp_key_chk = rcv_A6_effective[-16:]
                        resp = "索引位置:[%0.4d], 密钥类型:[%s], 导入密钥密文:[%s], 导入密钥校验值:[%s]\n" \
                               % (
                                   key_idx, key_type, rcv_imp_key_by_lmk.decode('ascii'),
                                   rcv_imp_key_chk.decode('ascii'))
                        pub.sendMessage("AsyImpCmd", info=resp)


class ThreadSyncKeys(threading.Thread):
    def __init__(self, source, destination: list):

        self.logger = logging.getLogger("MainFrame.Sync")

        threading.Thread.__init__(self)
        self.cli_source = source
        self.cli_destin = destination
        self.symm_key_list = []
        self.asym_rsa_list = []
        self.asym_sm2_list = []
        self.start()

    def run(self):
        self.SyncKeys(self.cli_source, self.cli_destin)
        pub.sendMessage("SyncHsms", info="done\n")

    def SyncKeys(self, source, destination: list):

        zmk_init = "1111111111111111111111111111111111111111111111111111111111111111"
        zmk_plain = ""
        # single_symm_key_list = []

        dict_source_zmk = {}

        """连接源加密机，AM 明文合成ZMK密钥，存入dict_source_zmk中"""
        for key_flg in KEY_ALG_FLAGS:
            response_err, zmk_plain = TRIM_KEY(zmk_init, key_flg)
            if response_err != "":
                self.logger.error(response_err)
            else:
                ret = HSM_AM(source, zmk_plain, key_flg)
                if ret[0] != "00":
                    err_msg = ret[1]
                    pub.sendMessage("SyncHsms", info=err_msg)
                    self.logger.error(err_msg)
                else:
                    zmk_by_lmk = ret[2]
                    dict_source_zmk.setdefault(key_flg, zmk_by_lmk)
        # print(dict_source_zmk)

        """SYMMETRIC KEYS"""
        for idx in range(1, 2048 + 1):       # 对称密钥索引范围
            single_symm_key_list = []

            """KG指令探测目标对称密钥索引，并根据对称密钥算法标识截取相应的ZMK明文"""
            ret = HSM_KG(source, idx, zmk_init)

            if ret[0] != "00":
                err_msg = ret[1]
                pub.sendMessage("SyncHsms", info=err_msg)
                continue
            else:
                key_type = ret[2]
                key_alg = ret[3]

                zmk_by_lmk = dict_source_zmk.get(key_alg)       # 从字典中根据密钥标识的类型获取ZMK值

                """A8 ZMK保护导出指定索引密钥"""
                ret = HSM_A8(source, idx, zmk_by_lmk, key_type, key_alg)
                if ret[0] != "00":
                    err_msg = ret[1]
                    pub.sendMessage("SyncHsms", info=err_msg)
                    self.logger.error(err_msg)
                else:
                    exp_key_by_zmk = ret[2]
                    exp_key_chk_val = ret[3]
                    # resp = "索引位置:[%0.4d], 密钥类型:[%s], 导出密钥密文:[%s], 导出密钥校验值:[%s]\n" \
                    #        % (idx, key_type, exp_key_by_zmk, exp_key_chk_val)
                    resp = "源密码机扫描, 索引位置:[%0.4d], 密钥类型:[%s], 密钥校验值:[%s]\n" \
                           % (idx, key_type, exp_key_chk_val)
                    pub.sendMessage("SyncHsms", info=resp)

                    single_symm_key_list.append(idx)
                    single_symm_key_list.append(key_type)
                    single_symm_key_list.append(exp_key_by_zmk)
                    single_symm_key_list.append(exp_key_chk_val)

                    self.symm_key_list.append(single_symm_key_list)

        """RSA"""
        zmk_by_lmk = dict_source_zmk.get('X')   # 从字典中根据密钥标识的类型获取ZMK值

        for idx in range(1, 64 + 1):         # RSA密钥索引范围
            single_asym_key_list = []

            """TR ZMK导出RSA"""
            ret = HSM_TR(source, idx, zmk_by_lmk)
            if ret[0] != "00":
                if ret[0] != "45":
                    err_msg = ret[1]
                    pub.sendMessage("SyncHsms", info=err_msg)
                    self.logger.error(err_msg)
                else:
                    err_msg = ret[1]
                    pub.sendMessage("SyncHsms", info=err_msg)
            else:
                rsa_export_body = ret[2]
                resp = "源密码机扫描, 索引位置:[%0.4d], 密钥类型:[%s]\n" \
                       % (idx, "RSA")
                pub.sendMessage("SyncHsms", info=resp)

                single_asym_key_list.append(idx)
                single_asym_key_list.append(rsa_export_body)

                self.asym_rsa_list.append(single_asym_key_list)

        """SM2"""
        zmk_by_lmk = dict_source_zmk.get('R')  # 从字典中根据密钥标识的类型获取ZMK值

        for idx in range(1, 64 + 1):     # SM2密钥索引范围
            single_asym_key_list = []

            """TT ZMK导出SM2"""
            ret = HSM_TT(source, idx, zmk_by_lmk)
            if ret[0] != "00":
                if ret[0] != "45":
                    err_msg = ret[1]
                    pub.sendMessage("SyncHsms", info=err_msg)
                    self.logger.error(err_msg)
                else:
                    err_msg = ret[1]
                    pub.sendMessage("SyncHsms", info=err_msg)
            else:
                sm2_export_body = ret[2]
                resp = "源密码机扫描, 索引位置:[%0.4d], 密钥类型:[%s]\n" \
                       % (idx, "SM2")
                pub.sendMessage("SyncHsms", info=resp)

                single_asym_key_list.append(idx)
                single_asym_key_list.append(sm2_export_body)

                self.asym_sm2_list.append(single_asym_key_list)

        for skt_list in destination:

            separator = "====="
            sync_notice = "同步至: "
            socket_handle = skt_list[0]
            ip_remote = socket_handle.getpeername()[0]          # 通过socket类型数据获取对端IP地址
            port_remote = str(socket_handle.getpeername()[1])   # 通过socket类型数据获取对端端口
            sync_notice_msg = separator + sync_notice + ip_remote + separator + "\n"
            pub.sendMessage("SyncHsms", info=sync_notice_msg)

            dict_destin_zmk = {}

            """连接目标加密机，AM 明文合成ZMK密钥，存入dict_destin_zmk中"""
            for key_flg in KEY_ALG_FLAGS:
                response_err, zmk_plain = TRIM_KEY(zmk_init, key_flg)
                if response_err != "":
                    self.logger.error(response_err)
                else:
                    ret = HSM_AM(socket_handle, zmk_plain, key_flg)
                    if ret[0] != "00":
                        err_msg = ret[1]
                        pub.sendMessage("SyncHsms", info=err_msg)
                        self.logger.error(err_msg)
                    else:
                        zmk_by_lmk = ret[2]
                        dict_destin_zmk.setdefault(key_flg, zmk_by_lmk)

            for i_key in self.symm_key_list:
                sync_idx = i_key[0]
                key_type = i_key[1]
                key_by_zmk = i_key[2]
                key_alg = i_key[2][0]
                key_chk_val = i_key[3]
                zmk_by_lmk = dict_destin_zmk.get(key_alg)   # 从字典中根据密钥标识的类型获取ZMK值

                ret = HSM_A6(socket_handle, sync_idx, zmk_by_lmk, key_by_zmk, key_type, key_alg)
                if ret[0] != "00":
                    err_msg = ret[1]
                    self.logger.error(err_msg)
                    pub.sendMessage("SyncHsms", info=err_msg)
                else:
                    imp_key_chk_val = ret[2]
                    if imp_key_chk_val != key_chk_val:
                        err_msg = "对称密钥导入密码机, 索引位置:[%0.4d], 同步失败: [%s, 密钥校验值不一致]" \
                                  % (sync_idx, imp_key_chk_val)
                        pub.sendMessage("SyncHsms", info=err_msg)
                        self.logger.error(err_msg)
                    else:
                        resp = "对称密钥导入密码机, 索引位置:[%0.4d], 密钥类型:[%s], 密钥校验值:[%s]\n" \
                               % (sync_idx, key_type, imp_key_chk_val)
                        pub.sendMessage("SyncHsms", info=resp)

            # print(self.asym_rsa_list)
            for r_key in self.asym_rsa_list:
                sync_idx = r_key[0]
                rsa_exp_body = r_key[1]
                zmk_by_lmk = dict_destin_zmk.get('X')       # 从字典中根据密钥标识的类型获取ZMK值

                """TS ZMK导入RSA"""
                ret = HSM_TS(socket_handle, sync_idx, zmk_by_lmk, rsa_exp_body)
                if ret[0] != "00":
                    err_msg = ret[1]
                    self.logger.error(err_msg)
                    pub.sendMessage("SyncHsms", info=err_msg)
                else:
                    rsa_private_by_lmk = ret[2]
                    resp = "RSA导入密码机, 索引位置:[%0.4d]\n" \
                           % sync_idx
                    pub.sendMessage("SyncHsms", info=resp)
                    # print(rsa_private_by_lmk)

            # print(self.asym_sm2_list)
            for s_key in self.asym_sm2_list:
                sync_idx = s_key[0]
                sm2_exp_body = s_key[1]
                zmk_by_lmk = dict_destin_zmk.get('R')       # 从字典中根据密钥标识的类型获取ZMK值

                """TU ZMK导入SM2"""
                ret = HSM_TU(socket_handle, sync_idx, zmk_by_lmk, sm2_exp_body)
                if ret[0] != "00":
                    err_msg = ret[1]
                    self.logger.error(err_msg)
                    pub.sendMessage("SyncHsms", info=err_msg)
                else:
                    sm2_private_by_lmk = ret[2]
                    resp = "SM2导入密码机, 索引位置:[%0.4d]\n" \
                           % sync_idx
                    pub.sendMessage("SyncHsms", info=resp)
                    # print(sm2_private_by_lmk)


class ThreadSocketConnect(threading.Thread):
    def __init__(self, socket_handle: socket, ip: str, port: str, fileno: int):

        self.logger = logging.getLogger("Socket")

        threading.Thread.__init__(self)
        self.socket_handle = socket_handle
        self.ip = ip
        self.port = int(port)
        self.fileno = fileno
        self.start()

    def run(self):
        self.socket_handle.settimeout(5)    # 设置超时时间, 5s
        # rebuild a socket object for avoiding error caused by TCP 2MSL
        time.sleep(1)
        stat = self.socket_handle.connect_ex((self.ip, self.port))
        title = "Socket_%s" % str(self.fileno)
        if stat != 0:
            pub.sendMessage(title, info="Socket Connection Failed\n")
        else:
            pub.sendMessage(title, info="Socket Connection Successful\n")


def TRIM_KEY(key_init, key_alg):
    response = ""
    key_plain = ""

    if key_alg == 'Z':
        key_plain = key_init[0:16]
    elif key_alg == 'X' or key_alg == 'R' or key_alg == 'P' or key_alg == 'L' or key_alg == 'U':
        key_plain = key_init[0:32]
    elif key_alg == 'Y' or key_alg == 'M' or key_alg == 'T':
        key_plain = key_init[0:48]
    elif key_alg == 'N':
        key_plain = key_init
    else:
        response = "Key algorithm flag is 'Undefined'."

    return response, key_plain


def HSM_KG(socket_handle, index, zmk_init):
    """KG指令探测目标对称密钥索引，并根据对称密钥算法标识截取相应的ZMK明文"""
    req_KG = Hsm.cmd_KG(index)
    # Socket Send
    socket_handle.send(req_KG)
    # Socket Receive
    res_KG_full = socket_handle.recv(2048)
    # Receive message analysis
    res_KG_effective = res_KG_full[2:]
    res_KG_err = res_KG_effective[2:4].decode('ascii')

    response = ""
    key_type = ""
    key_alg = ""
    zmk_plain = ""

    if res_KG_err != "00":
        response = "索引位置[%0.4d], KG指令响应出错，错误码为[%s]\n" % (index, res_KG_err)
    else:
        key_type = res_KG_effective[4:7].decode('ascii')
        key_alg = res_KG_effective[7:8].decode('ascii')

        ret = TRIM_KEY(zmk_init, key_alg)
        if ret[0] is "":
            zmk_plain = ret[1]
        else:
            response = ret[0]

    return res_KG_err, response, key_type, key_alg, zmk_plain


def HSM_AM(socket_handle, key_plain, key_alg):
    """AM指令根据密钥算法标识和密钥明文合成ZMK"""
    """
    目前版本，如果A8指令的待导出密钥为M类型，则A8指令会报错97，估计是指令层面的BUG。
    经测试可以使用X类型ZMK密钥将M类型的应用密钥导出。所以在AM合成ZMK的时候，如果KG检查到当前密钥为M类型，则生成X类型的ZMK。
    """
    if key_alg != 'M':
        req_AM = Hsm.cmd_AM(key_plain, key_alg)
    else:
        key_plain = "11111111111111111111111111111111"
        key_alg = 'X'
        req_AM = Hsm.cmd_AM(key_plain, key_alg)
    # Socket Send
    socket_handle.send(req_AM)
    # Socket Receive
    res_AM_full = socket_handle.recv(2048)
    # Receive message analysis
    res_AM_effective = res_AM_full[2:]
    res_AM_err = res_AM_effective[2:4].decode('ascii')

    response = ""
    key_by_lmk = ""

    if res_AM_err != "00":
        response = "AM指令响应出错，错误码为[%s]; 请求命令: [%s]\n" % (res_AM_err, req_AM[2:].decode("ascii"))
    else:
        if key_alg == "Z":
            # 密钥长度  8 字节
            key_by_lmk = res_AM_effective[4:21].decode("ascii")
        elif key_alg == 'Y' or key_alg == 'T':
            # 密钥长度 24 字节
            key_by_lmk = res_AM_effective[4:53].decode("ascii")
        elif key_alg == "N":
            # 密钥长度 32 字节
            key_by_lmk = res_AM_effective[4:69].decode("ascii")
        elif key_alg == 'M':
            key_by_lmk = res_AM_effective[4:37].decode("ascii")
        else:
            # 密钥长度 16 字节
            key_by_lmk = res_AM_effective[4:37].decode("ascii")

    return res_AM_err, response, key_by_lmk


def HSM_A8(socket_handle, index, zmk, key_type, key_alg):
    """A8指令通过ZMK导出对称密钥"""
    req_A8 = Hsm.cmd_A8(index, zmk, key_type, key_alg)
    # Socket Send
    socket_handle.send(req_A8)
    # Socket Receive
    res_A8_full = socket_handle.recv(1024)
    # Receive message analysis
    res_A8_effective = res_A8_full[2:]
    res_A8_err = res_A8_effective[2:4].decode('ascii')

    response = ""
    key_by_zmk = ""
    key_chk_val = ""

    if res_A8_err != "00":
        response = "索引位置[%0.4d], A8指令响应出错, 错误码为[%s]; 请求命令: [%s]\n" % \
                   (index, res_A8_err, req_A8[2:].decode('ascii'))
    else:
        key_chk_val = res_A8_effective[-16:].decode("ascii")
        if key_alg == "Z":
            key_by_zmk = res_A8_effective[4:20].decode("ascii")  # A8返回DES为8字节，没有Z字符头
        elif key_alg == 'Y' or key_alg == 'M' or key_alg == 'T':
            key_by_zmk = res_A8_effective[4:53].decode("ascii")
        elif key_alg == "N":
            key_by_zmk = res_A8_effective[4:69].decode("ascii")
        else:
            key_by_zmk = res_A8_effective[4:37].decode("ascii")

    return res_A8_err, response, key_by_zmk, key_chk_val


def HSM_A6(socket_handle, index, zmk, key_cipher, key_type, key_alg):
    """A6指令通过ZMK导入对称密钥"""
    req_A6 = Hsm.cmd_A6(index, zmk, key_cipher, key_type, key_alg)
    socket_handle.send(req_A6)
    res_A6_full = socket_handle.recv(2048)
    res_A6_effective = res_A6_full[2:]
    res_A6_err = res_A6_effective[2:4].decode('ascii')

    response = ""
    key_chk_val = ""

    if res_A6_err != "00":
        response = "索引位置[%0.4d], A6指令响应出错，错误码为[%s]; 请求命令: [%s]\n" % \
                   (index, res_A6_err, req_A6[2:].decode("ascii"))
    else:
        key_chk_val = res_A6_effective[-16:].decode("ascii")

    return res_A6_err, response, key_chk_val


def HSM_TR(socket_handle, index, zmk):
    """TR指令通过ZMK导入RSA"""
    req_TR = Hsm.cmd_TR(index, zmk)
    socket_handle.send(req_TR)
    res_TR_full = socket_handle.recv(2048)
    res_TR_effective = res_TR_full[2:]
    res_TR_hex = binascii.b2a_hex(res_TR_effective).decode('ascii')
    res_TR_err = res_TR_effective[2:4].decode('ascii')

    response = ""
    rsa_export_body = ""
    public_key = ""

    if res_TR_err != "00":
        response = "索引位置[%0.4d], TR指令响应出错，错误码为[%s]; 请求命令: [%s]" % \
                   (index, res_TR_err, req_TR[2:].decode("ascii"))
    else:
        rsa_export_body = binascii.b2a_hex(res_TR_effective[4:]).decode("ascii")

    return res_TR_err, response, rsa_export_body


def HSM_TS(socket_handle, index, zmk, export_body):
    """TS指令通过ZMK导入RSA"""
    req_TS = Hsm.cmd_TS(index, zmk, export_body)
    socket_handle.send(req_TS)
    res_TS_full = socket_handle.recv(2048)
    res_TS_effective = res_TS_full[2:]
    res_TS_err = res_TS_effective[2:4].decode('ascii')

    response = ""
    pri_key_lmk = ""

    if res_TS_err != "00":
        response = "索引位置[%0.4d], TS指令响应出错，错误码为[%s]; 请求命令: [%s]" % \
                   (index, res_TS_err, req_TS[2:])
    else:
        pri_key_lmk = binascii.b2a_hex(res_TS_effective[8:]).decode("ascii")

    return res_TS_err, response, pri_key_lmk


def HSM_TT(socket_handle, index, zmk):
    """TT指令通过ZMK导入SM2"""
    req_TT = Hsm.cmd_TT(index, zmk)
    socket_handle.send(req_TT)
    res_TT_full = socket_handle.recv(2048)
    res_TT_effective = res_TT_full[2:]
    res_TT_hex = binascii.b2a_hex(res_TT_effective).decode('ascii')
    res_TT_err = res_TT_effective[2:4].decode('ascii')

    response = ""
    sm2_export_body = ""
    public_key = ""

    if res_TT_err != "00":
        response = "索引位置[%0.4d], TT指令响应出错，错误码为[%s]; 请求命令: [%s]" % \
                   (index, res_TT_err, req_TT[2:].decode("ascii"))
    else:
        sm2_export_body = binascii.b2a_hex(res_TT_effective[4:]).decode("ascii")

    return res_TT_err, response, sm2_export_body


def HSM_TU(socket_handle, index, zmk, export_body):
    """TU指令通过ZMK导入SM2"""
    req_TU = Hsm.cmd_TU(index, zmk, export_body)
    socket_handle.send(req_TU)
    res_TU_full = socket_handle.recv(2048)
    res_TU_effective = res_TU_full[2:]
    res_TU_err = res_TU_effective[2:4].decode('ascii')

    response = ""
    pri_key_lmk = ""

    if res_TU_err != "00":
        response = "索引位置[%0.4d], TU指令响应出错，错误码为[%s]; 请求命令: [%s]" % \
                   (index, res_TU_err, req_TU[2:])
    else:
        pri_key_lmk = binascii.b2a_hex(res_TU_effective[8:]).decode("ascii")

    return res_TU_err, response, pri_key_lmk
