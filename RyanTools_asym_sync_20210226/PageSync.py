#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
import logging
# import csv
# import binascii
# import RyanTools.Hsm
from RyanTools import ThreadsComm
from socket import *
from pubsub import pub


class DialogIp(wx.Dialog):
    def __init__(self, title):
        wx.Dialog.__init__(self, None, -1, title=title, size=(300, 150))
        self.tc_ip_addr = wx.TextCtrl(self, size=(125, 30), value="192.168.19.192",
                                      style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(15, 15))
        self.tc_port = wx.TextCtrl(self, size=(60, 30), value="8018",
                                   style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(155, 15))
        self.bt_ok = wx.Button(self, wx.ID_OK, "OK", pos=(15, 60))
        self.bt_ok.SetDefault()
        self.bt_cancel = wx.Button(self, wx.ID_CANCEL, "Cancel", pos=(115, 60))


class PageSync(wx.Panel):

    def __init__(self, parent):

        self.logger = logging.getLogger("MainFrame.Sync")
        # self.logger.debug("Init hsm command page. Start.")

        wx.Panel.__init__(self, parent)

        self.font = wx.Font()
        self.font.SetPixelSize((0, 15))
        self.font.SetFamily(wx.FONTFAMILY_TELETYPE)

        self.cli_source = socket()
        self.cli_destination = socket()
        self.cli_destination_single_list = []
        self.cli_destination_total_list = []

        self.sym_keys = []
        self.asy_keys_rsa = []
        self.asy_keys_sm2 = []
        self.dict_keys = {}

        # Horizontal sizer for source HSM connection info
        self.st_ip_label_source = wx.StaticText(self, label="Source\nHsm IP", size=(70, 30))
        self.bt_edit_ip_list_source = wx.Button(self, size=(80, 30), label="Edit")
        self.bt_connect_source = wx.Button(self, size=(80, 30), label="Connect")
        self.bt_disconn_source = wx.Button(self, size=(80, 30), label="Disconnect")
        self.lc_ip_source = wx.ListCtrl(self, style=wx.LC_REPORT, size=(235, 60))
        self.lc_ip_source.InsertColumn(col=0, heading='IP address', format=wx.LIST_FORMAT_LEFT, width=125)
        self.lc_ip_source.InsertColumn(col=1, heading='Port', format=wx.LIST_FORMAT_LEFT, width=60)
        self.lc_ip_source.InsertColumn(col=2, heading='Status', format=wx.LIST_FORMAT_LEFT, width=50)
        self.list_init_insert = self.lc_ip_source.InsertItem(0, "")
        self.list_top_index = self.lc_ip_source.GetTopItem()    # listctrl的头部索引

        self.bs_first_line = wx.BoxSizer(wx.HORIZONTAL)
        self.bs_first_line.Add(self.st_ip_label_source, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.lc_ip_source, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.bt_edit_ip_list_source, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.bt_connect_source, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.bt_disconn_source, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        # Horizontal sizer for destination HSM connection info
        self.st_ip_label_destination = wx.StaticText(self, label="Destination\nHsm IP", size=(70, 30))
        self.bt_connect_destination = wx.Button(self, size=(80, 30), label="Connect")
        self.bt_disconn_destination = wx.Button(self, size=(80, 30), label="Disconnect")
        self.lc_ip_destination = wx.ListCtrl(self, style=wx.LC_REPORT, size=(235, 140))
        self.lc_ip_destination.InsertColumn(col=0, heading='IP address', format=wx.LIST_FORMAT_LEFT, width=125)
        self.lc_ip_destination.InsertColumn(col=1, heading='Port', format=wx.LIST_FORMAT_LEFT, width=60)
        self.lc_ip_destination.InsertColumn(col=2, heading='Status', format=wx.LIST_FORMAT_LEFT, width=50)
        self.bt_add_ip_list_destination = wx.Button(self, size=(80, 30), label="Add")
        self.bt_delete_ip_list_destination = wx.Button(self, size=(80, 30), label="Delete")
        self.bt_edit_ip_list_destination = wx.Button(self, size=(80, 30), label="Edit")

        self.bs_second_line = wx.BoxSizer(wx.HORIZONTAL)
        self.bs_sub_second_sizer = wx.BoxSizer(wx.VERTICAL)
        self.bs_second_line.Add(self.st_ip_label_destination, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_second_line.Add(self.lc_ip_destination, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_sub_second_sizer.Add(self.bt_add_ip_list_destination, wx.SizerFlags().Border(wx.LEFT, 25))
        self.bs_sub_second_sizer.Add(self.bt_edit_ip_list_destination, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_sub_second_sizer.Add(self.bt_delete_ip_list_destination, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_second_line.Add(self.bs_sub_second_sizer, wx.SizerFlags().Border(wx.TOP, 25))
        self.bs_second_line.Add(self.bt_connect_destination, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_second_line.Add(self.bt_disconn_destination, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        # Horizontal sizer for showing sync of HSMs.
        self.tc_process_display = wx.TextCtrl(self, size=(280, 200),
                                              style=wx.TE_READONLY | wx.TE_MULTILINE | wx.HSCROLL)
        self.tc_process_display2 = wx.TextCtrl(self, size=(280, 200),
                                               style=wx.TE_READONLY | wx.TE_MULTILINE | wx.HSCROLL)
        self.bt_sync = wx.Button(self, size=(80, 30), label="Sync")
        self.bt_clear = wx.Button(self, size=(80, 30), label="Clear")

        self.bs_third_line = wx.BoxSizer(wx.HORIZONTAL)
        self.bs_sub_third_sizer = wx.BoxSizer(wx.VERTICAL)
        self.bs_third_line.Add(self.tc_process_display, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_third_line.Add(self.tc_process_display2, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_sub_third_sizer.Add(self.bt_sync, wx.SizerFlags().Border(wx.LEFT, 0))
        self.bs_sub_third_sizer.Add(self.bt_clear, wx.SizerFlags().Border(wx.TOP, 25))
        self.bs_third_line.Add(self.bs_sub_third_sizer, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        self.bt_connect_source.Enable(False)
        self.bt_disconn_source.Enable(False)
        self.bt_connect_destination.Enable(False)
        self.bt_disconn_destination.Enable(False)
        self.bt_sync.Enable(False)

        # Bind Events to Buttons
        self.Bind(wx.EVT_BUTTON, self.EvtEditSource, self.bt_edit_ip_list_source)
        self.Bind(wx.EVT_BUTTON, self.EvtConnHsmSource, self.bt_connect_source)
        self.Bind(wx.EVT_BUTTON, self.EvtDisConnHsmSource, self.bt_disconn_source)

        self.Bind(wx.EVT_BUTTON, self.EvtAddDestin, self.bt_add_ip_list_destination)
        self.Bind(wx.EVT_BUTTON, self.EvtEditDestin, self.bt_edit_ip_list_destination)
        self.Bind(wx.EVT_BUTTON, self.EvtDelDestin, self.bt_delete_ip_list_destination)
        self.Bind(wx.EVT_BUTTON, self.EvtConnHsmDestin, self.bt_connect_destination)
        self.Bind(wx.EVT_BUTTON, self.EvtDisConnHsmDestin, self.bt_disconn_destination)

        self.Bind(wx.EVT_BUTTON, self.EvtSyncHsm, self.bt_sync)
        self.Bind(wx.EVT_BUTTON, self.EvtClrText, self.bt_clear)

        # Vertical sizer for full panel
        self.bs_panel = wx.BoxSizer(wx.VERTICAL)
        self.bs_panel.Add(self.bs_first_line, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
        self.bs_panel.Add(self.bs_second_line, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
        self.bs_panel.Add(self.bs_third_line, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))

        pub.subscribe(self.DisplayProcess, "SyncHsms")
        self.SetSizer(self.bs_panel)

    def EvtEditSource(self, event):
        """Edit ip and port in source ip list, only single object"""
        dlg = DialogIp("Edit Source IP")
        result = dlg.ShowModal()
        if result == wx.ID_OK:
            self.lc_ip_source.SetItem(self.list_init_insert, 0, dlg.tc_ip_addr.GetValue())
            self.lc_ip_source.SetItem(self.list_init_insert, 1, dlg.tc_port.GetValue())
            self.bt_connect_source.Enable(True)
        dlg.Destroy()

    def EvtConnHsmSource(self, event):
        """Connect to Source Hsm."""
        ip = ""
        port = ""
        count = self.lc_ip_source.GetItemCount()
        # index = self.lc_ip_source.GetTopItem()
        for i in range(count):
            ip = self.lc_ip_source.GetItemText(i, col=0)
            port = self.lc_ip_source.GetItemText(i, col=1)

        # rebuild a socket object for avoiding error caused by TCP 2MSL
        self.logger.debug("Trying to connect source HSM [%s:%s].", ip, port)
        self.cli_source = socket(AF_INET, SOCK_STREAM)
        file_no = self.cli_source.fileno()                  # 获取当前socket对象的问题file_no标识
        title = "Socket_%s" % str(file_no)                  # 将file_no作为pubsub的title唯一标识, 避免title冲突
        self.lc_ip_source.SetItem(self.list_top_index, 2, "...")
        ThreadsComm.ThreadSocketConnect(self.cli_source, ip, port, file_no)     # 创建Socket连接修改为线程间通信
        pub.subscribe(self.DisplaySocketResultSource, title, ip=ip, port=port)

        self.bt_connect_source.Enable(False)

    def EvtDisConnHsmSource(self, event):
        """Disconnect Source Hsm"""
        self.cli_source.close()
        ip = self.lc_ip_source.GetItemText(0, col=0)
        port = self.lc_ip_source.GetItemText(0, col=1)
        self.logger.debug("Close source HSM [%s:%s] connection successful." % (ip, port))
        self.lc_ip_source.SetItem(self.list_top_index, 2, "")
        self.bt_edit_ip_list_source.Enable(True)
        self.bt_disconn_source.Enable(False)
        self.bt_sync.Enable(False)
        self.bt_connect_source.Enable(True)

    def EvtAddDestin(self, event):
        """Add new ip and port into destination list"""
        list_new_item = wx.ListItem()
        list_new_item.SetId(self.lc_ip_destination.GetItemCount())

        dlg = DialogIp("Add Destination IP")
        result = dlg.ShowModal()
        if result == wx.ID_OK:
            index = self.lc_ip_destination.InsertItem(list_new_item)
            self.lc_ip_destination.SetItem(index, 0, dlg.tc_ip_addr.GetValue())
            self.lc_ip_destination.SetItem(index, 1, dlg.tc_port.GetValue())
            self.bt_connect_destination.Enable(True)
        dlg.Destroy()

    def EvtDelDestin(self, event):
        """Delete selected object(s) in destination list"""
        sel_cnt = self.lc_ip_destination.GetSelectedItemCount()
        fst = self.lc_ip_destination.GetFirstSelected()
        lc_idx_list = []
        if sel_cnt != 0:
            for i in range(sel_cnt):
                nxt = self.lc_ip_destination.GetNextSelected(fst)
                lc_idx_list.append(fst)
                fst = nxt
        else:
            dlg = wx.MessageDialog(self, message="Please select at least one object.", caption="Delete Destination IP",
                                   style=wx.OK | wx.CENTRE | wx.ICON_INFORMATION)
            if dlg.ShowModal() == wx.ID_OK:
                self.Close(True)
            dlg.Destroy()
        lc_idx_list.sort(reverse=True)  # 从后向前删除
        for idx in lc_idx_list:
            self.lc_ip_destination.DeleteItem(idx)

        cnt = self.lc_ip_destination.GetItemCount()
        if cnt == 0:
            self.bt_connect_destination.Enable(False)

    def EvtEditDestin(self, event):
        """Edit single focused object in destination list"""
        focused_idx = self.lc_ip_destination.GetFocusedItem()
        if focused_idx != -1:
            dlg = DialogIp("Edit Destination IP")
            result = dlg.ShowModal()
            if result == wx.ID_OK:
                self.lc_ip_destination.SetItem(focused_idx, 0, dlg.tc_ip_addr.GetValue())
                self.lc_ip_destination.SetItem(focused_idx, 1, dlg.tc_port.GetValue())
            dlg.Destroy()
        else:
            dlg = wx.MessageDialog(self, message="Please select one object.", caption="Edit Destination IP",
                                   style=wx.OK | wx.CENTRE | wx.ICON_INFORMATION)
            if dlg.ShowModal() == wx.ID_OK:
                self.Close(True)
            dlg.Destroy()

    def EvtConnHsmDestin(self, event):
        """Connect to Destination Hsm(s)."""
        self.bt_connect_destination.Enable(False)
        ip = ""
        port = ""
        count = self.lc_ip_destination.GetItemCount()
        index = self.lc_ip_source.GetTopItem()
        index_list = []

        # 下面两个列表只在一个周期中使用
        index_list.clear()
        self.cli_destination_total_list.clear()

        for i in range(count):
            ip = self.lc_ip_destination.GetItemText(i, col=0)
            port = self.lc_ip_destination.GetItemText(i, col=1)
            # print(ip, port)
            index_list.append(index)

            # rebuild a socket object for avoiding error caused by TCP 2MSL
            self.logger.debug("Trying to connect destination HSM [%s:%s].", ip, port)
            self.cli_destination = socket(AF_INET, SOCK_STREAM)
            file_no = self.cli_destination.fileno()
            title = "Socket_%s" % str(file_no)
            self.lc_ip_destination.SetItem(index, 2, "...")

            ThreadsComm.ThreadSocketConnect(self.cli_destination, ip, port, file_no)     # 创建Socket连接修改为线程间通信
            pub.subscribe(self.DisplaySocketResultDestin, title, ip=ip, port=port, index=index,
                          socket_handle=self.cli_destination)

            index = self.lc_ip_destination.GetNextItem(index)

    def EvtDisConnHsmDestin(self, event):
        """Disconnect Destination Hsm(s)."""
        for i in self.cli_destination_total_list:
            socket_handle = i[0]    # socket通信句柄
            ip = i[1]               # IP地址
            port = i[2]             # 端口号
            index = i[3]            # ListCtrl中的索引号
            flg = i[4]              # 连接成功标识
            if flg != "Failed":
                socket_handle.close()
                self.logger.debug("Close destination HSM [%s:%s] connection successful." % (ip, port))
                self.lc_ip_destination.SetItem(index, 2, "")
            else:
                continue
        self.bt_disconn_destination.Enable(False)
        self.bt_edit_ip_list_destination.Enable(True)
        self.bt_delete_ip_list_destination.Enable(True)
        self.bt_sync.Enable(False)
        self.bt_connect_destination.Enable(True)

    def EvtSyncHsm(self, event):
        """Sync Keys in Hsm(s)"""
        # ThreadsComm.ThreadSyncKeys(self.cli_source, self.cli_destination)
        ThreadsComm.ThreadSyncKeys(self.cli_source, self.cli_destination_total_list)

    def EvtClrText(self, event):
        """Clear Text"""
        self.tc_process_display.Clear()
        self.tc_process_display2.Clear()

    def DisplaySocketResultSource(self, info, ip, port):
        if info.find("Socket Connection Failed\n") >= 0:
            self.logger.debug("Connect source HSM [%s:%s] failed.", ip, port)
            self.lc_ip_source.SetItem(self.list_top_index, 2, "×")
            self.bt_connect_source.Enable(True)
        if info.find("Socket Connection Successful\n") >= 0:
            self.logger.debug("Connect source HSM [%s:%s] successful.", ip, port)
            self.lc_ip_source.SetItem(self.list_top_index, 2, "✔")
            self.bt_edit_ip_list_source.Enable(False)
            self.bt_disconn_source.Enable(True)
            self.bt_connect_source.Enable(False)
            if self.bt_disconn_source.IsEnabled() and self.bt_disconn_destination.IsEnabled():
                self.bt_sync.Enable(True)

    def DisplaySocketResultDestin(self, info, ip, port, index, socket_handle):
        if info.find("Socket Connection Failed\n") >= 0:
            self.logger.debug("Connect destination HSM [%s:%s] failed.", ip, port)
            self.lc_ip_destination.SetItem(index, 2, "×")

            self.bt_connect_destination.Enable(True)

        if info.find("Socket Connection Successful\n") >= 0:
            self.logger.debug("Connect destination HSM [%s:%s] successful.", ip, port)
            self.lc_ip_destination.SetItem(index, 2, "✔")

            self.cli_destination_single_list.append(socket_handle)
            self.cli_destination_single_list.append(ip)
            self.cli_destination_single_list.append(port)
            self.cli_destination_single_list.append(index)
            self.cli_destination_single_list.append("Successful")
            self.cli_destination_total_list.append(self.cli_destination_single_list)
            self.cli_destination_single_list = []       # 不能用clear方法, 否则数据全部变为空

            self.bt_edit_ip_list_destination.Enable(False)
            self.bt_delete_ip_list_destination.Enable(False)
            self.bt_disconn_destination.Enable(True)
            self.bt_connect_destination.Enable(False)
            if self.bt_disconn_source.IsEnabled() and self.bt_disconn_destination.IsEnabled():
                self.bt_sync.Enable(True)

    def DisplayProcess(self, info):
        if info.find("源密码机扫描") >= 0 and not info.find("指令响应出错") >= 0:
            self.tc_process_display.write(info)
        if info.find("同步至: ") >= 0:
            self.tc_process_display2.write(info)
        if info.find("导入密码机") >= 0:
            self.tc_process_display2.write(info)
        if info.find("done") >= 0:
            self.logger.debug("Sync Hsm keys, done.")
            dlg = wx.MessageDialog(self, message="Sync Hsm keys successfully.",
                                   caption="Sync Keys", style=wx.OK | wx.CENTRE)
            if dlg.ShowModal() == wx.ID_OK:
                self.Close(True)
            dlg.Destroy()

