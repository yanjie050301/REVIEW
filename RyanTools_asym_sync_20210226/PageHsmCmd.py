#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
import time
import logging
import csv
import binascii
import RyanTools.Hsm
from RyanTools import ThreadsComm
from socket import *
from pubsub import pub


class PageHsmCmd(wx.Panel):

    def __init__(self, parent):

        self.logger = logging.getLogger("MainFrame.HsmCmd")
        # self.logger.debug("Init hsm command page. Start.")

        wx.Panel.__init__(self, parent)

        self.font = wx.Font()
        self.font.SetPixelSize((0, 15))
        self.font.SetFamily(wx.FONTFAMILY_TELETYPE)

        self.cli = socket()

        self.st_ip_label = wx.StaticText(self, label="Hsm IP")
        self.tc_ip_addr = wx.TextCtrl(self, size=(125, 24), value="192.168.9.124")
        self.st_port_label = wx.StaticText(self, label="Port")
        self.tc_port_num = wx.TextCtrl(self, size=(60, 24), value="8018")
        self.bt_connect = wx.Button(self, size=(80, 24), label="Connect")
        self.bt_disconn = wx.Button(self, size=(80, 24), label="Disconnect")
        self.st_conn_stat = wx.StaticText(self, label="Status:")

        self.nb = wx.Notebook(self, wx.ID_ANY)

        """
        Notebook Export Key Page
        """
        self.pExpKey = wx.Panel(self.nb, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.nb.AddPage(self.pExpKey, u"Export Keys", True)

        bSizerExpFull = wx.BoxSizer(wx.VERTICAL)
        bSizerExpL1 = wx.BoxSizer(wx.HORIZONTAL)
        bSizerExpL2 = wx.BoxSizer(wx.HORIZONTAL)
        bSizerExpL3 = wx.BoxSizer(wx.HORIZONTAL)
        bSizerExpL4 = wx.BoxSizer(wx.HORIZONTAL)

        self.st_idx = wx.StaticText(self.pExpKey, label='Index')
        self.tc_idx_range_start = wx.TextCtrl(self.pExpKey, size=(125, 24), value='1')
        self.tc_idx_range_end = wx.TextCtrl(self.pExpKey, size=(125, 24), value='5')
        self.bt_exp_key = wx.Button(self.pExpKey, size=(125, 24), label="Run...")
        self.bt_clear = wx.Button(self.pExpKey, size=(125, 24), label="Clear...")

        bSizerExpL1.Add(self.st_idx, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        bSizerExpL1.Add(self.tc_idx_range_start, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        bSizerExpL1.Add(self.tc_idx_range_end, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        bSizerExpL1.Add(self.bt_exp_key, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        bSizerExpL1.Add(self.bt_clear, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        self.st_zmk = wx.StaticText(self.pExpKey, label='ZMK')
        self.tc_zmk = wx.TextCtrl(self.pExpKey, size=(250, 24), value='11111111111111111111111111111111')
        # self.st_key_type = wx.StaticText(self.pExpKey, label='Exp Key Type')
        # key_type = ["000 - ZMK",
        #             "00A - DEK/ZEK",
        #             "109 - MDK"]
        # self.ch_key_type = wx.Choice(self.pExpKey, size=(125, 24), choices=key_type, name='key_types')

        bSizerExpL2.Add(self.st_zmk, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        bSizerExpL2.Add(self.tc_zmk, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        # bSizerExpL2.Add(self.st_key_type, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        # bSizerExpL2.Add(self.ch_key_type, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        self.tc_exp_resp_display = wx.TextCtrl(self.pExpKey, size=(680, 180),
                                               style=wx.TE_READONLY | wx.TE_MULTILINE | wx.HSCROLL)

        bSizerExpL3.Add(self.tc_exp_resp_display, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        self.bt_exp_file_path = wx.Button(self.pExpKey, label="Choose Keys File Path")
        self.tc_exp_file_path = wx.TextCtrl(self.pExpKey, size=(200, 24), value='')
        self.bt_exp_file = wx.Button(self.pExpKey, label="Export")

        bSizerExpL4.Add(self.bt_exp_file_path, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        bSizerExpL4.Add(self.tc_exp_file_path, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        bSizerExpL4.Add(self.bt_exp_file, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        bSizerExpFull.Add(bSizerExpL1, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
        bSizerExpFull.Add(bSizerExpL2, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
        bSizerExpFull.Add(bSizerExpL3, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
        bSizerExpFull.Add(bSizerExpL4, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
        self.pExpKey.SetSizer(bSizerExpFull)

        """
        Notebook Import Key Page
        """
        self.pImpKey = wx.Panel(self.nb, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.nb.AddPage(self.pImpKey, u"Import Keys", False)

        bSizerImpFull = wx.BoxSizer(wx.VERTICAL)
        bSizerImpL1 = wx.BoxSizer(wx.HORIZONTAL)
        bSizerImpL2 = wx.BoxSizer(wx.HORIZONTAL)
        bSizerImpL3 = wx.BoxSizer(wx.HORIZONTAL)

        self.bt_imp_select_file = wx.Button(self.pImpKey, label="Select Import Keys File")
        self.tc_imp_file_path = wx.TextCtrl(self.pImpKey, size=(200, 24), value='')

        bSizerImpL1.Add(self.bt_imp_select_file, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        bSizerImpL1.Add(self.tc_imp_file_path, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        self.st_imp_zmk = wx.StaticText(self.pImpKey, label='ZMK')
        self.tc_imp_zmk = wx.TextCtrl(self.pImpKey, size=(250, 24), value='11111111111111111111111111111111')
        self.bt_imp_key = wx.Button(self.pImpKey, size=(125, 24), label="Run...")

        bSizerImpL2.Add(self.st_imp_zmk, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        bSizerImpL2.Add(self.tc_imp_zmk, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        bSizerImpL2.Add(self.bt_imp_key, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        self.tc_imp_resp_display = wx.TextCtrl(self.pImpKey, size=(680, 180),
                                               style=wx.TE_READONLY | wx.TE_MULTILINE | wx.HSCROLL)

        bSizerImpL3.Add(self.tc_imp_resp_display, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        bSizerImpFull.Add(bSizerImpL1, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
        bSizerImpFull.Add(bSizerImpL2, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
        bSizerImpFull.Add(bSizerImpL3, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))

        self.pImpKey.SetSizer(bSizerImpFull)

        self.bt_disconn.Enable(False)
        self.bt_exp_key.Enable(False)
        self.bt_imp_key.Enable(False)
        self.bt_exp_file.Enable(False)

        """Main page"""
        self.Bind(wx.EVT_BUTTON, self.EvtConnHsm, self.bt_connect)
        self.Bind(wx.EVT_BUTTON, self.EvtDisConnHsm, self.bt_disconn)

        """Export page"""
        self.Bind(wx.EVT_BUTTON, self.EvtExpKey, self.bt_exp_key)
        self.Bind(wx.EVT_BUTTON, self.EvtClear, self.bt_clear)
        self.Bind(wx.EVT_BUTTON, self.EvtChooseFilePath, self.bt_exp_file_path)
        self.Bind(wx.EVT_BUTTON, self.EvtExpKeysFile, self.bt_exp_file)

        """Import page"""
        self.Bind(wx.EVT_BUTTON, self.EvtSelectKeysFile, self.bt_imp_select_file)
        self.Bind(wx.EVT_BUTTON, self.EvtImpKey, self.bt_imp_key)

        self.bs_first_line = wx.BoxSizer(wx.HORIZONTAL)
        self.bs_first_line.Add(self.st_ip_label, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.tc_ip_addr, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.st_port_label, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.tc_port_num, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.bt_connect, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.bt_disconn, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.st_conn_stat, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        self.bs_panel = wx.BoxSizer(wx.VERTICAL)
        self.bs_panel.Add(self.bs_first_line, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
        self.bs_panel.Add(self.nb, 1, wx.ALL | wx.EXPAND, 5)

        pub.subscribe(self.DisplayExpRes, "AsyExpCmd")
        pub.subscribe(self.DisplayImpRes, "AsyImpCmd")
        self.SetSizer(self.bs_panel)

        # self.logger.debug("Init key check value tools page. Finish.")

    def EvtConnHsm(self, event):
        """Connect to Hsm and get the NC command receive message."""
        ip = self.tc_ip_addr.GetValue()
        port = int(self.tc_port_num.GetValue())
        time.sleep(1)

        # rebuild a socket object for avoiding error caused by TCP 2MSL
        self.logger.debug("Trying to connect [%s:%s].", ip, port)
        self.cli = socket(AF_INET, SOCK_STREAM)
        stat = self.cli.connect_ex((ip, port))
        if stat != 0:
            # print("Connect failed!")
            self.logger.debug("Connect [%s:%s] failed.", ip, port)
            self.st_conn_stat.SetLabel("Status: " + "Failed.")
        else:
            self.logger.debug("Connect [%s:%s] successful.", ip, port)
            self.st_conn_stat.SetLabel("Status: " + "Successful.")
            self.bt_disconn.Enable(True)
            self.bt_exp_key.Enable(True)
            self.bt_imp_key.Enable(True)
            self.bt_connect.Enable(False)

    def EvtDisConnHsm(self, event):
        """Disconnect Hsm"""
        self.cli.close()
        self.logger.debug("Close connection successful.")
        self.st_conn_stat.SetLabel("Status: ")
        self.bt_disconn.Enable(False)
        self.bt_exp_key.Enable(False)
        self.bt_imp_key.Enable(False)
        self.bt_exp_file.Enable(False)
        self.bt_connect.Enable(True)

    def EvtExpKey(self, event):
        # 原始单一现成逻辑，循环次数过多时，会出现假死的情况
        """
        # idx_start = int(self.tc_idx_range_start.GetValue())
        # idx_end = int(self.tc_idx_range_end.GetValue())
        # for idx in range(idx_start, idx_end):
        #     msg = RyanTools.Hsm.cmd_A8(idx, "R56DDE21CA44144D43C1F2D3EAB39943E")
        #
        #     self.cli.send(msg)
        #     rcv_full = self.cli.recv(1024)
        #     rcv_resp = rcv_full[2:]
        #     rcv_resp_hex = binascii.b2a_hex(rcv_resp)
        #     rcv_cmd = rcv_resp[0:2].decode('ascii')
        #     rcv_err = rcv_resp[2:4].decode('ascii')
        #     if rcv_err != "00":
        #         # print("索引位置[%d], 指令响应出错，错误码为[%s]" % (idx, rcv_err))
        #         self.tc_resp_display.write("索引位置[%d], 指令响应出错，错误码为[%s]\n" % (idx, rcv_err))
        #     else:
        #         rcv_exp_key_by_zmk = rcv_resp[4:37]
        #         rcv_exp_key_chk = rcv_resp[-16:]
        #         # print("索引位置[%d], 导出密钥密文:[%s], 导出密钥校验值:[%s]\n"
        #         #       % (idx, rcv_exp_key_by_zmk.decode('ascii'), rcv_exp_key_chk.decode('ascii')))
        #         self.tc_resp_display.write("索引位置[%d], 导出密钥密文:[%s], 导出密钥校验值:[%s]\n"
        #               % (idx, rcv_exp_key_by_zmk.decode('ascii'), rcv_exp_key_chk.decode('ascii')))
        """

        # 多线程通信，异步处理循环逻辑，不会出现假死情况
        idx_start = int(self.tc_idx_range_start.GetValue())
        idx_end = int(self.tc_idx_range_end.GetValue()) + 1
        zmk = self.tc_zmk.GetValue()
        # key_type = self.ch_key_type.GetStringSelection()[0:3]
        ThreadsComm.ThreadAsySndExpCmd(client=self.cli, idx_start=idx_start, idx_end=idx_end,
                                       zmk=zmk)

    def EvtClear(self, event):
        """Clear Screen"""
        self.tc_exp_resp_display.SetValue("")
        self.bt_exp_file.Enable(False)

    def DisplayExpRes(self, info):
        if info.find("索引") >= 0:
            self.tc_exp_resp_display.write(info)
        if info.find("done") >= 0:
            self.logger.debug("Export Keys is done.")
            self.bt_exp_file.Enable(True)

    def EvtChooseFilePath(self, event):
        loc_time = time.strftime("%Y%m%d_%H.%M.%S", time.localtime())
        filename = "ExportKeys_{0}.txt".format(loc_time)
        dlg = wx.DirDialog(self, "Choose input directory", "", wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.tc_exp_file_path.SetValue(path + '\\' + filename)
        dlg.Destroy()

    def EvtExpKeysFile(self, event):
        try:
            with open(self.tc_exp_file_path.GetValue(), 'w', newline='', encoding='utf-8') as f:
                for i1 in range(self.tc_exp_resp_display.GetNumberOfLines()):
                    str_full = self.tc_exp_resp_display.GetLineText(i1)

                    count = str_full.count('[')
                    list_extract = []
                    for i2 in range(count):
                        start = str_full.find('[')
                        end = str_full.find(']')
                        content = str_full[start + 1: end]
                        list_extract.append(content)
                        str_full = str_full[end + 1:]

                    if len(list_extract) == 0:
                        continue
                    elif len(list_extract[1]) != 3:
                        continue
                    csv_writer = csv.writer(f)
                    csv_writer.writerow(list_extract)
                    # print(i1, list_extract)
        except FileNotFoundError as e:
            dlg = wx.MessageDialog(self, message="No such file or directory.", caption="Export Keys",
                                   style=wx.OK | wx.CENTRE | wx.ICON_ERROR)
            if dlg.ShowModal() == wx.ID_OK:
                self.Close(True)
            dlg.Destroy()
        else:
            dlg = wx.MessageDialog(self, message="Keys write into file successfully.", caption="Export Keys",
                                   style=wx.OK | wx.CENTRE)
            if dlg.ShowModal() == wx.ID_OK:
                self.Close(True)
            dlg.Destroy()

    def EvtSelectKeysFile(self, event):
        dir_name = ''
        dlg = wx.FileDialog(self, "Choose Keys File", dir_name, "", "*.*", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetFilename()
            dirname = dlg.GetDirectory()
            self.tc_imp_file_path.SetValue(dirname + '\\' + filename)
        dlg.Destroy()

    def EvtImpKey(self, event):
        self.tc_imp_resp_display.SetValue("")
        file_path = self.tc_imp_file_path.GetValue()
        # self.tc_imp_resp_display.write(file_path)
        zmk = self.tc_imp_zmk.GetValue()

        try:
            with open(file_path, 'r') as f:
                csv.reader(f)
        except FileNotFoundError as e:
            dlg = wx.MessageDialog(self, message="No such file or directory.", caption="Import Keys",
                                   style=wx.OK | wx.CENTRE | wx.ICON_ERROR)
            if dlg.ShowModal() == wx.ID_OK:
                self.Close(True)
            dlg.Destroy()
        else:
            ThreadsComm.ThreadAsySndImpCmd(client=self.cli, path=file_path, zmk=zmk)

    def DisplayImpRes(self, info):
        if info.find("索引") >= 0:
            self.tc_imp_resp_display.write(info)
        if info.find("done") >= 0:
            self.logger.debug("Import Keys is done.")
            dlg = wx.MessageDialog(self, message="Keys import into Hsm successfully.", caption="Import Keys",
                                   style=wx.OK | wx.CENTRE)
            if dlg.ShowModal() == wx.ID_OK:
                self.Close(True)
            dlg.Destroy()
            self.bt_imp_key.Enable(True)
