import wx


class HexValidator(wx.Validator):
    """Hex string validator setting"""
    def __init__(self):
        wx.Validator.__init__(self)
        self.valid_input = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'A', 'B', 'C', 'D', 'E', 'F'
        ]
        self.str_len = 0
        # 绑定字符输入事件
        self.Bind(wx.EVT_CHAR, self.EvtInputChar)

    def EvtInputChar(self, event):
        # 得到输入字符的 ASCII 码
        key_code = event.GetKeyCode()

        # 退格（ASCII 码 为8），删除一个字符。
        if key_code == 8:
            self.str_len -= 1
            event.Skip()
            return

        if 96 < key_code < 103:
            key_code -= 32
            event.SetKeyCode(key_code)

        # 把 ASII 码 转成字符
        input_char = chr(key_code)
        # print(key_code)
        if input_char in self.valid_input:
            event.Skip()
            self.str_len += 1
            return True
        return False

    def Clone(self):
        """Required Validator method"""
        return HexValidator()

    def Validate(self, win):  # 1 使用验证器方法
        return True

    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True


class DecValidator(wx.Validator):
    """Hex string validator setting"""
    def __init__(self):
        wx.Validator.__init__(self)
        self.valid_input = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
        ]
        self.str_len = 0
        # 绑定字符输入事件
        self.Bind(wx.EVT_CHAR, self.EvtInputChar)

    def EvtInputChar(self, event):
        # 得到输入字符的 ASCII 码
        key_code = event.GetKeyCode()

        # 退格（ASCII 码 为8），删除一个字符。
        if key_code == 8:
            self.str_len -= 1
            event.Skip()
            return

        # 把 ASII 码 转成字符
        input_char = chr(key_code)
        # print(key_code)
        if input_char in self.valid_input:
            event.Skip()
            self.str_len += 1
            return True
        return False

    def Clone(self):
        """Required Validator method"""
        return DecValidator()

    def Validate(self, win):  # 1 使用验证器方法
        return True

    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True
