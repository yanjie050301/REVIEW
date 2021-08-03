#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
import time
import logging
from socket import *
from RyanTools import Hsm


class PageHsmConn(wx.Panel):

    def __init__(self, parent):

        self.logger = logging.getLogger("MainFrame.HsmConnTools")
        # self.logger.debug("Init hsm connect tools page. Start.")

        wx.Panel.__init__(self, parent)

        """Set Font"""
        font = wx.Font()
        font.SetPixelSize((0, 15))
        font.SetFamily(wx.FONTFAMILY_MODERN)

        """socket with hsm initial setting"""
        self.cli = socket()
        NC_cmd = Hsm.data_encode("NC")
        cmd_len = Hsm.cal_len(NC_cmd)
        self.msg = cmd_len + NC_cmd

        self.st_ip_label = wx.StaticText(self, label="Hsm IP")
        self.tc_ip_addr = wx.TextCtrl(self, size=(125, 24))
        self.st_port_label = wx.StaticText(self, label="Port")
        self.tc_port_num = wx.TextCtrl(self, size=(60, 24))
        self.bt_connect = wx.Button(self, size=(80, 24), label="Connect")
        self.bt_disconn = wx.Button(self, size=(80, 24), label="Disconnect")

        self.tc_ip_addr.SetFont(font)
        self.tc_port_num.SetFont(font)

        self.st_conn_stat = wx.StaticText(self, label="Connection Status:")
        self.st_conn_stat.SetFont(font)

        self.st_hsm_dmk = wx.StaticText(self, label="DMK Check Value:")
        self.st_hsm_dmk.SetFont(font)

        self.st_hsm_ver = wx.StaticText(self, label="Hsm Service Ver:")
        self.st_hsm_ver.SetFont(font)
        # HSM device SN num
        self.st_hsm_sn = wx.StaticText(self, label="Hsm Device SN:")
        self.st_hsm_sn.SetFont(font)

        # Bind events
        self.Bind(wx.EVT_BUTTON, self.EvtConnHsm, self.bt_connect)
        self.Bind(wx.EVT_BUTTON, self.EvtDisConnHsm, self.bt_disconn)

        # Horizontal sizer for ip connection info
        self.bs_ip_conn = wx.BoxSizer(wx.HORIZONTAL)
        self.bs_ip_conn.Add(self.st_ip_label, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_ip_conn.Add(self.tc_ip_addr, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_ip_conn.Add(self.st_port_label, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_ip_conn.Add(self.tc_port_num, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_ip_conn.Add(self.bt_connect, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_ip_conn.Add(self.bt_disconn, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        # Horizontal sizer for ip connection status
        self.bs_hsm_stat = wx.BoxSizer(wx.VERTICAL)
        self.bs_hsm_stat.Add(self.st_conn_stat, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_hsm_stat.Add(self.st_hsm_dmk, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_hsm_stat.Add(self.st_hsm_ver, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_hsm_stat.Add(self.st_hsm_sn, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        # Vertical sizer for full panel
        self.bs_panel = wx.BoxSizer(wx.VERTICAL)
        self.bs_panel.Add(self.bs_ip_conn, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
        self.bs_panel.Add(self.bs_hsm_stat, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
        self.SetSizer(self.bs_panel)

        # self.logger.debug("Init hsm connect tools page. Finish.")

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
            print("Connect failed!")
            self.logger.debug("Connect [%s:%s] failed.", ip, port)
            self.st_conn_stat.SetLabel("Connection Status: " + "Failed.")
        else:
            self.logger.debug("Connect [%s:%s] successful.", ip, port)
            self.cli.send(self.msg)
            rcv = self.cli.recv(1024)[2:].decode('ascii')
            DMK_chk = rcv[4:20]
            Serv_ver = rcv[20:44]
            Dev_Sn = rcv[44:]
            # print(rcv)  # print NC command received message to console.
            self.st_conn_stat.SetLabel("Connection Status: " + "Success.")
            self.st_hsm_dmk.SetLabel("DMK check value:   " + DMK_chk)
            self.st_hsm_ver.SetLabel("Hsm Service Ver:   " + Serv_ver)
            self.st_hsm_sn.SetLabel("Hsm Device SN:     " + Dev_Sn)
            self.logger.debug("DMK check value is [%s].", DMK_chk)
            self.logger.debug("Service version is [%s].", Serv_ver)
            self.logger.debug("Device SN is [%s].", Dev_Sn)

    def EvtDisConnHsm(self, event):
        """Disconnect Hsm"""
        self.cli.close()

        self.st_conn_stat.SetLabel("Connection Status: ")
        self.st_hsm_dmk.SetLabel("DMK check value:   ")
        self.st_hsm_ver.SetLabel("Hsm Service Ver:   ")
        self.st_hsm_sn.SetLabel("Hsm Device SN:     ")