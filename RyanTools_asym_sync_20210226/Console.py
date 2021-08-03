#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
import time
import logging
import os
from RyanTools import PageHsmCmd
from RyanTools import PageScanIpTools
from RyanTools import PageHsmConn
from RyanTools import PageSync
from RyanTools import PageCalcChkVal
from RyanTools import PageMathTools
from RyanTools import PageTest

# class ToolsConsole(wx.Frame):
#
#     def __init__(self, *args, **kw):
#         super(ToolsConsole, self).__init__(*args, **kw)
#
#         pn = wx.Panel(self)
#
#         # socket with hsm initial setting
#         self.cli = socket()
#         NC_cmd = Hsm.data_encode("NC")
#         cmd_len = Hsm.cal_len(NC_cmd)
#         self.msg = cmd_len + NC_cmd
#
#         # ip label
#         self.st_ip_label = wx.StaticText(pn, label="Hsm IP")
#         # ip address
#         self.tc_ip_addr = wx.TextCtrl(pn, size=(125, 24))
#         # port label
#         self.st_port_label = wx.StaticText(pn, label="Port")
#         # port
#         self.tc_port_num = wx.TextCtrl(pn, size=(60, 24))
#         # connect button
#         self.bt_connect = wx.Button(pn, size=(80, 24), label="Connect")
#         # disconnect button
#         self.bt_disconn = wx.Button(pn, size=(80, 24), label="Disconnect")
#         # hsm status
#         self.st_hsm_stat = wx.StaticText(pn, label="Connection Status:")
#
#         # Bind events
#         self.Bind(wx.EVT_BUTTON, self.EvtConnHsm, self.bt_connect)
#         self.Bind(wx.EVT_BUTTON, self.EvtDisConnHsm, self.bt_disconn)
#
#         # Horizontal sizer for ip connection info
#         self.bs_ip_conn = wx.BoxSizer(wx.HORIZONTAL)
#         self.bs_ip_conn.Add(self.st_ip_label, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
#         self.bs_ip_conn.Add(self.tc_ip_addr, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
#         self.bs_ip_conn.Add(self.st_port_label, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
#         self.bs_ip_conn.Add(self.tc_port_num, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
#         self.bs_ip_conn.Add(self.bt_connect, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
#         self.bs_ip_conn.Add(self.bt_disconn, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
#
#         # Horizontal sizer for ip connection status
#         self.bs_hsm_stat = wx.BoxSizer(wx.HORIZONTAL)
#         self.bs_hsm_stat.Add(self.st_hsm_stat, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
#
#         # Vertical sizer for full panel
#         self.bs_panel = wx.BoxSizer(wx.VERTICAL)
#         self.bs_panel.Add(self.bs_ip_conn, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
#         self.bs_panel.Add(self.bs_hsm_stat, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
#         pn.SetSizer(self.bs_panel)
#
#     def EvtConnHsm(self, event):
#         ip = self.tc_ip_addr.GetValue()
#         port = int(self.tc_port_num.GetValue())
#         time.sleep(1)
#
#         # rebuild a socket object for avoiding error caused by TCP 2MSL
#         self.cli = socket(AF_INET, SOCK_STREAM)
#         stat = self.cli.connect_ex((ip, port))
#         if stat != 0:
#             print("Connect failed!")
#         else:
#             self.cli.send(self.msg)
#             rcv = self.cli.recv(1024)[2:].decode('ascii')
#             DMK_chk = rcv[4:20]
#             print(rcv)
#             self.st_hsm_stat.SetLabel("Connection Status: " + DMK_chk)
#
#     def EvtDisConnHsm(self, event):
#         self.cli.close()


if __name__ == '__main__':
    app = wx.App()
    # frm = ToolsConsole(None, title="Ryan's Hsm Tools", pos=(200, 200), size=(780, 400))
    frm = wx.Frame(None, title="Ryan's Hsm Tools", pos=(200, 200), size=(780, 600))

    logger = logging.getLogger("MainFrame")
    logger.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    log_path = ".\\log"
    if not os.path.exists(log_path):  # 如果路径不存在
        os.makedirs(log_path)
    loc_time = time.strftime("%Y%m%d_%H.%M.%S", time.localtime())
    log_file_name = "ToolsLog_{0}.log".format(loc_time)

    handler = logging.FileHandler(".\\log\\{0}".format(log_file_name))
    handler.setLevel(level=logging.DEBUG)
    handler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setLevel(level=logging.DEBUG)
    console.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(console)

    logger.info("Creating main frame.")
    nb_frame = wx.Notebook(frm)
    nb_frame.AddPage(PageHsmConn.PageHsmConn(nb_frame), "Hsm Overview")
    nb_frame.AddPage(PageHsmCmd.PageHsmCmd(nb_frame), "Export/Import Key")
    nb_frame.AddPage(PageSync.PageSync(nb_frame), "Hsm Sync")
    nb_frame.AddPage(PageScanIpTools.PageScanIpTools(nb_frame), "IP Scan")
    # nb_frame.AddPage(PageCalcChkVal.PageChkVal(nb_frame), "Check Value")
    # math_tools = PageMathTools.PageMathTools(nb_frame)
    # nb_frame.AddPage(math_tools, "Math Tools")
    # nb_frame.AddPage(PageTest.PageTest(nb_frame), "test")
    frm.Show()
    logger.info("Creating main frame. Finish.")
    app.MainLoop()
    logger.info("Close.")
