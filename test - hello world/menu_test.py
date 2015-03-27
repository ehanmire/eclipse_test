# -*- coding: utf-8 -*- 

import wx

class Example(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs) 
            
        self.InitUI()
        
    def InitUI(self):    
        
        # 메뉴 만들기
        menubar = wx.MenuBar()
        
        # 메뉴 추가하기
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_EXIT, '&Start', 'Start Job')
        fileMenu.Append(wx.ID_EXIT, '&End', 'End Job')
        qmi = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')
        
        menubar.Append(fileMenu, '&Record')
        self.SetMenuBar(menubar)
        
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

        self.SetSize((300, 200))
        self.SetTitle('Simple menu')
        
        # text 상자 넣어보기
        #self.control = wx.TextCtrl(self, pos = (120,150))
        
        # 단순 텍스트 보이기
        panel = wx.Panel(self)
        wx.StaticText(panel, label = "test", pos=(20,30))
        wx.TextCtrl(panel, pos=(50,30))
        
        # 상태줄 추가
        self.CreateStatusBar()
        
        
        self.Centre()
        self.Show(True)
        
    def OnQuit(self, e):
        self.Close()

def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()