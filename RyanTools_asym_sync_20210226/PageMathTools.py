import logging
import math
import wx
import RyanTools.Validator

ALG_LIST = ["阶乘 Factorial", "幂指数 Power"]
FAC_FLAG = ALG_LIST.index("阶乘 Factorial")
POW_FLAG = ALG_LIST.index("幂指数 Power")


class PageMathTools(wx.Panel):

    def __init__(self, parent):

        self.logger = logging.getLogger("MainFrame.MathTools")
        # self.logger.debug("Init math tools page. Start.")

        wx.Panel.__init__(self, parent)

        """Define controls"""
        # self.sb_calc_factorial = wx.StaticBox(self, label="Calc Factorial")
        self.tc_first_args = wx.TextCtrl(self, validator=RyanTools.Validator.DecValidator(), name='first_args')
        self.ch_alg_list = wx.Choice(self, size=(125, 24), choices=ALG_LIST, name='algorithm_list')
        self.tc_second_args = wx.TextCtrl(self, validator=RyanTools.Validator.DecValidator(), name='second_args')
        self.bt_calculate = wx.Button(self, label="计算 Calculate")
        self.tc_calc_result = wx.TextCtrl(self, name="result")
        self.bt_calculate.Enable(False)
        self.tc_calc_result.SetEditable(False)
        # print(self.tc_first_args.GetBackgroundColour())  //(r=255, g=255, b=255, alpha=255)
        self.tc_calc_result.SetBackgroundColour(self.tc_first_args.GetBackgroundColour())

        """Define events"""
        self.Bind(wx.EVT_BUTTON, self.EvtCalculate, self.bt_calculate)
        self.Bind(wx.EVT_CHOICE, self.EvtChoiceSetting, self.ch_alg_list)

        """Set layout"""
        self.bs_first_line = wx.BoxSizer(wx.HORIZONTAL)
        self.bs_first_line.Add(self.tc_first_args, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.ch_alg_list, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.tc_second_args, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.bt_calculate, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        self.bs_first_line.Add(self.tc_calc_result, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        self.bs_panel = wx.BoxSizer(wx.VERTICAL)
        self.bs_panel.Add(self.bs_first_line, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 10))

        self.SetSizer(self.bs_panel)
        # self.logger.debug("Creating math tools page. Finish.")

    def EvtChoiceSetting(self, event):
        """ Set button bt_calculate enable and textctrl tc_second_args enable"""
        if self.ch_alg_list.GetSelection() != -1:
            self.bt_calculate.Enable(True)

        if self.ch_alg_list.GetSelection() == FAC_FLAG:
            self.tc_second_args.Enable(False)

        if self.ch_alg_list.GetSelection() == POW_FLAG:
            self.tc_second_args.Enable(True)

    def EvtCalculate(self, event):
        if self.ch_alg_list.GetSelection() == FAC_FLAG:
            self.CalcFactorial()

        if self.ch_alg_list.GetSelection() == POW_FLAG:
            self.CalcPower()

    def CalcFactorial(self):
        try:
            self.tc_calc_result.SetValue(str(math.factorial(int(self.tc_first_args.GetValue()))))
        except ValueError:
            self.logger.error("阶乘 Factorial, 参数异常")

    def CalcPower(self):
        try:
            x = int(self.tc_first_args.GetValue())
            y = int(self.tc_second_args.GetValue())
            self.tc_calc_result.SetValue(str(math.pow(x, y)))
        except ValueError:
            self.logger.error("幂指数 Power, 参数异常")
