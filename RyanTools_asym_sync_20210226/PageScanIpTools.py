#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
import logging
from socket import *
from RyanTools import ThreadsComm
from pubsub import pub


class PageScanIpTools(wx.Panel):

    def __init__(self, parent):

        self.logger = logging.getLogger("MainFrame.ScanIpTools")
        # self.logger.debug("Init scan IP tools page. Start.")

        wx.Panel.__init__(self, parent)

        self.st_ip_seg_label = wx.StaticText(self, label="IP segment")
        self.tc_ip_segment = wx.TextCtrl(self, size=(80, 24), value="192.168.19")
        self.st_ip_from = wx.StaticText(self, label="From")
        self.tc_ip_from = wx.TextCtrl(self, size=(32, 24), value="1")
        self.st_ip_to = wx.StaticText(self, label="To")
        self.tc_ip_to = wx.TextCtrl(self, size=(32, 24), value="255")
        self.bt_ip_seg_run = wx.Button(self, size=(80, 24), label="Run bat")
        self.bt_save_result = wx.Button(self, size=(80, 24), label="Save result")
        self.tc_ip_display = wx.TextCtrl(self, size=(380, 200), style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.tc_rest_ip = wx.TextCtrl(self, size=(250, 200), style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.cb_clr_pre_dat = wx.CheckBox(self, label="clear previous data")

        self.bt_save_result.Enable(False)

        self.Bind(wx.EVT_BUTTON, self.EvtRunBat, self.bt_ip_seg_run)
        self.Bind(wx.EVT_BUTTON, self.EvtSaveResult, self.bt_save_result)

        self.bs_first_line = wx.BoxSizer(wx.HORIZONTAL)
        self.bs_first_line.Add(self.st_ip_seg_label, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.tc_ip_segment, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.st_ip_from, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.tc_ip_from, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.st_ip_to, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.tc_ip_to, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.bt_ip_seg_run, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.bt_save_result, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        self.bs_second_line = wx.BoxSizer(wx.HORIZONTAL)
        self.bs_second_line.Add(self.cb_clr_pre_dat, wx.SizerFlags().Border(wx.LEFT, 25))

        self.bs_third_line = wx.BoxSizer(wx.HORIZONTAL)
        self.bs_third_line.Add(self.tc_ip_display, wx.SizerFlags().Border(wx.LEFT, 25))
        self.bs_third_line.Add(self.tc_rest_ip, wx.SizerFlags().Border(wx.LEFT, 25))

        self.bs_panel = wx.BoxSizer(wx.VERTICAL)
        self.bs_panel.Add(self.bs_first_line, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
        self.bs_panel.Add(self.bs_second_line, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
        self.bs_panel.Add(self.bs_third_line, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))

        self.SetSizer(self.bs_panel)

        pub.subscribe(self.DisplayIPs, "scan_ip")
        # self.logger.debug("Init scan IP tools page. Finish.")

    def EvtRunBat(self, event):
        """Run task between threads communication."""
        str_ip_seg = self.tc_ip_segment.GetValue()
        str_end_from = self.tc_ip_from.GetValue()
        str_end_to = self.tc_ip_to.GetValue()

        str_ip_from = str_ip_seg + '.' + str_end_from
        str_ip_to = str_ip_seg + '.' + str_end_to

        self.logger.debug("Detect ip from [%s] to [%s].", str_ip_from, str_ip_to)
        try:
            ThreadsComm.ThreadScanIPs(ip_seg=str_ip_seg, ip_from=str_end_from, ip_to=str_end_to)
        except Exception as e:
            self.logger.error(e)

    def DisplayIPs(self, info):
        """According to the specific thread status, set the panel attributes."""
        if info.find("Start") >= 0:
            if self.cb_clr_pre_dat.Get3StateValue() == 1:
                self.tc_ip_display.SetValue("")
                self.tc_rest_ip.SetValue("")
            self.bt_ip_seg_run.Enable(False)
            self.bt_save_result.Enable(False)
        if info.find("done") >= 0:
            self.logger.debug("Detect ip is done.")
            self.bt_ip_seg_run.Enable(True)
            self.bt_save_result.Enable(True)
        if info.find("can not reach") & info.find("unreachable") >= 0:
            self.tc_rest_ip.write(info)
        else:
            self.tc_ip_display.write(info)

    def EvtSaveResult(self, event):
        """Save the TextControl contents into a file"""
        with wx.FileDialog(self, message="Save result", wildcard="text files (*.txt)|*.txt",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            # fileDialog.SetDirectory("")
            # fileDialog.SetFilename("iplist_%s.txt" % self.tc_ip_segment.GetValue())
            pathname = fileDialog.GetPath()
            # print(pathname)
            self.logger.debug("Save ip address detection results to [%s]." % pathname)
            try:
                with open(pathname, 'w+') as file:
                    file.write(self.tc_ip_display.GetValue())
                file.close()
                with open(pathname, 'a+') as file:
                    file.write(self.tc_rest_ip.GetValue())
                file.close()
            except IOError:
                self.logger.error("Cannot save current data to [%s]." % pathname)
