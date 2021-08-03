import wx
import time
import logging
import binascii
import RyanTools.Hsm
from RyanTools import ThreadsComm
from socket import *
from pubsub import pub


class PageTest(wx.Panel):

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
        Notebook Export Key
        """
        self.pExpKey = wx.Panel(self.nb, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.nb.AddPage(self.pExpKey, u"Export Keys", True)

        bSizerExpFull = wx.BoxSizer(wx.VERTICAL)

        bSizerExpL1 = wx.BoxSizer(wx.HORIZONTAL)
        self.st_exp_key = wx.StaticText(self.pExpKey, label='Export Keys')
        self.tc_idx_range_start = wx.TextCtrl(self.pExpKey, size=(125, 24), value='0')
        self.tc_idx_range_end = wx.TextCtrl(self.pExpKey, size=(125, 24), value='100')
        self.bt_exp_key = wx.Button(self.pExpKey, size=(125, 24), label="Run...")
        self.bt_clear = wx.Button(self.pExpKey, size=(125, 24), label="Clear...")

        bSizerExpL1.Add(self.st_exp_key, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        bSizerExpL1.Add(self.tc_idx_range_start, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        bSizerExpL1.Add(self.tc_idx_range_end, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        bSizerExpL1.Add(self.bt_exp_key, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        bSizerExpL1.Add(self.bt_clear, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        bSizerExpL2 = wx.BoxSizer(wx.HORIZONTAL)
        self.st_zmk = wx.StaticText(self.pExpKey, label='ZMK')
        self.tc_zmk = wx.TextCtrl(self.pExpKey, size=(250, 24), value='R6FD5184A73490208F40765CDF1E2AAAA')
        self.st_key_type = wx.StaticText(self.pExpKey, label='Exp Key Type')
        key_type = ["000 - ZMK",
                    "00A - DEK/ZEK",
                    "109 - MDK"]
        self.ch_key_type = wx.Choice(self.pExpKey, size=(125, 24), choices=key_type, name='key_types')

        bSizerExpL2.Add(self.st_zmk, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        bSizerExpL2.Add(self.tc_zmk, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        bSizerExpL2.Add(self.st_key_type, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        bSizerExpL2.Add(self.ch_key_type, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        bSizerExpL3 = wx.BoxSizer(wx.HORIZONTAL)
        self.tc_resp_display = wx.TextCtrl(self.pExpKey, size=(680, 180), style=wx.TE_READONLY | wx.TE_MULTILINE)

        bSizerExpL3.Add(self.tc_resp_display, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        bSizerExpFull.Add(bSizerExpL1, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
        bSizerExpFull.Add(bSizerExpL2, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
        bSizerExpFull.Add(bSizerExpL3, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
        self.pExpKey.SetSizer(bSizerExpFull)

        """
        Notebook Import Key
        """
        self.m_panel2 = wx.Panel(self.nb, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.nb.AddPage(self.m_panel2, u"Import Keys", False)

        self.bt_disconn.Enable(False)

        self.Bind(wx.EVT_BUTTON, self.EvtConnHsm, self.bt_connect)
        self.Bind(wx.EVT_BUTTON, self.EvtDisConnHsm, self.bt_disconn)

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
            print("Connect failed!")
            self.logger.debug("Connect [%s:%s] failed.", ip, port)
            self.st_conn_stat.SetLabel("Status: " + "Failed.")
        else:
            self.logger.debug("Connect [%s:%s] successful.", ip, port)
            self.st_conn_stat.SetLabel("Status: " + "Successful.")
            self.bt_disconn.Enable(True)
            self.sp_exp_key.bt_exp_key.Enable(True)

    def EvtDisConnHsm(self, event):
        """Disconnect Hsm"""
        self.cli.close()
        self.st_conn_stat.SetLabel("Status: ")
        self.bt_disconn.Enable(False)
        self.sp_exp_key.bt_exp_key.Enable(False)


# class SubPageExpKeys(wx.Panel):
#
#     def __init__(self, parent, cli):
#         wx.Panel.__init__(self, parent)
#         self.cli = cli
#
#         self.st_exp_key = wx.StaticText(self, label='Export Keys')
#         self.tc_idx_range_start = wx.TextCtrl(self, size=(125, 24), value='0')
#         self.tc_idx_range_end = wx.TextCtrl(self, size=(125, 24), value='100')
#         self.bt_exp_key = wx.Button(self, size=(125, 24), label="Run...")
#         self.bt_clear = wx.Button(self, size=(125, 24), label="Clear...")
#
#         self.bt_exp_key.Enable(False)
#         self.Bind(wx.EVT_BUTTON, self.EvtExpKey, self.bt_exp_key)
#         self.Bind(wx.EVT_BUTTON, self.EvtClear, self.bt_clear)
#
#         self.st_zmk = wx.StaticText(self, label='ZMK')
#         self.tc_zmk = wx.TextCtrl(self, size=(250, 24), value='R6FD5184A73490208F40765CDF1E2AAAA')
#         self.st_key_type = wx.StaticText(self, label='Exp Key Type')
#         key_type = ["000 - ZMK",
#                     "00A - DEK/ZEK",
#                     "109 - MDK"]
#         self.ch_key_type = wx.Choice(self, size=(125, 24), choices=key_type, name='key_types')
#
#         self.tc_resp_display = wx.TextCtrl(self, size=(680, 180), style=wx.TE_READONLY | wx.TE_MULTILINE)
#
#         self.bs_second_line = wx.BoxSizer(wx.HORIZONTAL)
#         self.bs_second_line.Add(self.st_exp_key, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
#         self.bs_second_line.Add(self.tc_idx_range_start, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
#         self.bs_second_line.Add(self.tc_idx_range_end, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
#         self.bs_second_line.Add(self.bt_exp_key, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
#         self.bs_second_line.Add(self.bt_clear, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
#
#         self.bs_third_line = wx.BoxSizer(wx.HORIZONTAL)
#         self.bs_third_line.Add(self.st_zmk, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
#         self.bs_third_line.Add(self.tc_zmk, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
#         self.bs_third_line.Add(self.st_key_type, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
#         self.bs_third_line.Add(self.ch_key_type, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
#
#         self.bs_fourth_line = wx.BoxSizer(wx.HORIZONTAL)
#         self.bs_fourth_line.Add(self.tc_resp_display, wx.SizerFlags().Border(wx.LEFT, 25))
#
#         self.bs_panel = wx.BoxSizer(wx.VERTICAL)
#         self.bs_panel.Add(self.bs_second_line, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
#         self.bs_panel.Add(self.bs_third_line, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
#         self.bs_panel.Add(self.bs_fourth_line, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
#
#         pub.subscribe(self.DisplayRespone, "AsyCmd")
#         self.SetSizer(self.bs_panel)
#
#     def EvtExpKey(self, event):
#         idx_start = int(self.tc_idx_range_start.GetValue())
#         idx_end = int(self.tc_idx_range_end.GetValue()) + 1
#         zmk = self.tc_zmk.GetValue()
#         key_type = self.ch_key_type.GetStringSelection()[0:3]
#         print(key_type)
#         ThreadsComm.ThreadAsySndCmd(client=self.cli, idx_start=idx_start, idx_end=idx_end,
#                                     zmk=zmk, key_type=key_type)
#
#     def EvtClear(self, event):
#         """Clear Screen"""
#         self.tc_resp_display.SetValue("")
#
#     def DisplayRespone(self, info):
#         if info.find("索引") >= 0:
#             self.tc_resp_display.write(info)


# class SubPageImpKeys(wx.Panel):
#     def __init__(self, parent):
#         wx.Panel.__init__(self, parent)
