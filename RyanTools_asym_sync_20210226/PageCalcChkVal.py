import logging
import wx
from Cryptodome.Cipher import DES
from Cryptodome.Cipher import AES
from Cryptodome.Cipher import DES3
import binascii
from RyanTools.Cipher import sm4_

ALG_LIST = ['DES & DES3', 'AES', 'SM4']
ALG_DES = ALG_LIST.index('DES & DES3')
ALG_AES = ALG_LIST.index('AES')
ALG_SM4 = ALG_LIST.index('SM4')

ENCRYPT = 0
DECRYPT = 1


class PageChkVal(wx.Panel):

    def __init__(self, parent):

        self.logger = logging.getLogger("MainFrame.CheckValueTools")
        # self.logger.debug("Init key check value tools page. Start.")

        wx.Panel.__init__(self, parent)

        self.font = wx.Font()
        self.font.SetPixelSize((0, 15))
        self.font.SetFamily(wx.FONTFAMILY_TELETYPE)

        self.st_alg_choice = wx.StaticText(self, label='algorithm')
        self.ch_alg_list = wx.Choice(self, size=(125, 24), choices=ALG_LIST, name='algorithm')
        self.bt_calc_chk = wx.Button(self, size=(125, 24), label="Check Value")
        self.st_key_value = wx.StaticText(self, label='key value')
        # self.tc_key_value = wx.TextCtrl(self, size=(460, 24), validator=Validator.HexValidator(), style=wx.TE_LEFT)
        self.tc_key_value = wx.TextCtrl(self, size=(530, 24), style=wx.TE_LEFT)
        self.tc_key_length = wx.TextCtrl(self, size=(48, 24), style=wx.TE_READONLY)
        self.st_chk_value = wx.StaticText(self, label='chk value')
        self.tc_chk_value = wx.TextCtrl(self, size=(530, 24), style=wx.TE_READONLY)
        self.tc_chk_length = wx.TextCtrl(self, size=(48, 24), style=wx.TE_READONLY)

        self.tc_key_value.SetFont(self.font)
        self.tc_chk_value.SetFont(self.font)
        self.bt_calc_chk.Enable(False)

        self.tc_chk_value.Bind(wx.EVT_TEXT, self.EvtShowCVLen)
        self.tc_key_value.Bind(wx.EVT_TEXT, self.EvtTextToUpper)
        self.Bind(wx.EVT_CHOICE, self.EvtChoiceSetting, self.ch_alg_list)
        self.Bind(wx.EVT_BUTTON, self.EvtCalcCV, self.bt_calc_chk)

        self.bs_first_line = wx.BoxSizer(wx.HORIZONTAL)
        self.bs_first_line.Add(self.st_alg_choice, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.ch_alg_list, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.bt_calc_chk, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        self.bs_second_line = wx.BoxSizer(wx.HORIZONTAL)
        self.bs_second_line.Add(self.st_key_value, wx.SizerFlags().Border(wx.LEFT, 25))
        self.bs_second_line.Add(self.tc_key_value, wx.SizerFlags().Border(wx.LEFT, 25))
        self.bs_second_line.Add(self.tc_key_length, wx.SizerFlags().Border(wx.LEFT, 25))

        self.bs_third_line = wx.BoxSizer(wx.HORIZONTAL)
        self.bs_third_line.Add(self.st_chk_value, wx.SizerFlags().Border(wx.LEFT, 25))
        self.bs_third_line.Add(self.tc_chk_value, wx.SizerFlags().Border(wx.LEFT, 25))
        self.bs_third_line.Add(self.tc_chk_length, wx.SizerFlags().Border(wx.LEFT, 25))

        self.bs_panel = wx.BoxSizer(wx.VERTICAL)
        self.bs_panel.Add(self.bs_first_line, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
        self.bs_panel.Add(self.bs_second_line, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))
        self.bs_panel.Add(self.bs_third_line, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))

        self.SetSizer(self.bs_panel)

        # self.logger.debug("Init key check value tools page. Finish.")

    def EvtTextToUpper(self, event):
        end_pos = self.tc_key_value.GetInsertionPoint()
        if end_pos <= 0:
            return
        content_value = self.tc_key_value.GetValue()
        replace_value = ''

        """ Determine if the value of tc_key_value is hex string """
        for i in content_value:
            if 48 <= ord(i) <= 57:  # 0-9
                replace_value += i
            elif 65 <= ord(i) <= 70:  # A-F
                replace_value += i
            elif 97 <= ord(i) <= 102:  # a-f
                replace_value += i
            else:
                replace_value += ''

        self.tc_key_value.ChangeValue(replace_value.upper())
        self.tc_key_value.SetInsertionPoint(end_pos)

        self.tc_key_length.SetValue(str(len(self.tc_key_value.GetValue())))

    """
    def EvtUpperDemo(self, e):
        end_pos = self.tc_key_value.GetInsertionPoint()  # 获取插入点的位置
        if end_pos <= 0:
            return  # 插入点为0代表是文本框的起始位置
        start_pos = end_pos - 1
        self.tc_key_value.SetSelection(start_pos, end_pos)  # 选取刚输入的字符
        char_value = self.tc_key_value.GetStringSelection()  # 获取字符的值
        if 97 <= ord(char_value) <= 102:  # 小写字母的ascii 码范围是97到122
            upper_case = char_value.upper()  # 转换成大写
            self.tc_key_value.Remove(start_pos, end_pos)  # 删除小写字母
            # time.sleep(.5)  # 等待0.5秒，为的是能看到删除的动作，可以删掉这一行
            self.tc_key_value.WriteText(upper_case)  # 填入大写字母
        else:
            self.tc_key_value.SetInsertionPoint(end_pos)  # 如果是其他字符，直接设置插入点，等待输入
    """

    def EvtShowKeyLen(self, event):
        self.tc_key_length.SetValue(str(len(self.tc_key_value.GetValue())))

    def EvtShowCVLen(self, event):
        self.tc_chk_length.SetValue(str(len(self.tc_chk_value.GetValue())))

    def EvtChoiceSetting(self, event):
        """ Set button bt_calc_chk enable and the max length of textctrl tc_key_value """
        if self.ch_alg_list.GetSelection() != -1:
            self.bt_calc_chk.Enable(True)

        if self.ch_alg_list.GetSelection() == ALG_DES:
            self.tc_key_value.SetMaxLength(48)
        if self.ch_alg_list.GetSelection() == ALG_AES:
            self.tc_key_value.SetMaxLength(64)
        if self.ch_alg_list.GetSelection() == ALG_SM4:
            self.tc_key_value.SetMaxLength(32)

    def EvtCalcCV(self, event):
        if self.ch_alg_list.GetSelection() == ALG_SM4:
            self.logger.debug("计算SM4密钥校验值")
            try:
                key_hex_str = self.tc_key_value.GetValue()
                key_hex_lst = [int(x) for x in bytes(bytes().fromhex(key_hex_str))]

                data_hex_lst = [0x00] * 16
                # print(key_hex_lst)

                sm4_ins = sm4_.Sm4()

                sm4_ins.sm4_set_key(key_hex_lst, ENCRYPT)
                enc_dat_int_lst, enc_dat_hex_str = sm4_ins.sm4_crypt_ecb(data_hex_lst)

                chk_value = enc_dat_hex_str[:16]
                self.tc_chk_value.SetValue(chk_value.upper())

                self.logger.debug("SM4 Key:[%s], Chk Value:[%s]" % (key_hex_str, chk_value.upper()))
            except (ValueError, IndexError) as e:
                self.logger.error(e)

        if self.ch_alg_list.GetSelection() == ALG_DES:
            self.logger.debug("计算DES密钥校验值")
            try:
                key_hex_str = self.tc_key_value.GetValue()
                key_hex_bytes = bytes().fromhex(key_hex_str)
                print(len(key_hex_bytes))

                zero_hex_bytes = b'\x00' * 8
                # print(zero_hex_bytes)

                # print(len(self.tc_key_value.GetValue()))
                if len(key_hex_bytes) == 8:
                    des_ins = DES.new(key_hex_bytes, DES.MODE_ECB)
                    enc_dat_hex_str = binascii.b2a_hex(des_ins.encrypt(zero_hex_bytes)).decode()
                    chk_value = enc_dat_hex_str[:16]
                else:
                    des3_ins = DES3.new(key_hex_bytes, DES3.MODE_ECB)
                    enc_dat_hex_str = binascii.b2a_hex(des3_ins.encrypt(zero_hex_bytes)).decode()
                    chk_value = enc_dat_hex_str[:16]

                self.tc_chk_value.SetValue(chk_value.upper())
                self.logger.debug("DES Key:[%s], Chk Value:[%s]" % (key_hex_str, chk_value.upper()))
            except ValueError as e:
                self.logger.error(e)

        if self.ch_alg_list.GetSelection() == ALG_AES:
            self.logger.debug("计算AES密钥校验值")
            try:
                key_hex_str = self.tc_key_value.GetValue()
                key_hex_bytes = bytes().fromhex(key_hex_str)

                zero_hex_bytes = b'\x00' * 16
                # print(data_hex_bytes)

                aes_ins = AES.new(key_hex_bytes, AES.MODE_ECB)
                enc_dat_hex_str = binascii.b2a_hex(aes_ins.encrypt(zero_hex_bytes)).decode()
                chk_value = enc_dat_hex_str[:16]
                self.tc_chk_value.SetValue(chk_value.upper())

                self.logger.debug("AES Key:[%s], Chk Value:[%s]" % (key_hex_str, chk_value.upper()))
            except ValueError as e:
                self.logger.error(e)


