# -*- coding: utf-8 -*- 

import wx

app = wx.App()

window = wx.Frame(None, style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, title = 'Á¦¸ñ')
window.Show()

#frame = wx.Frame(None, -1, 'simple.py')
#frame.Show()

app.MainLoop()
