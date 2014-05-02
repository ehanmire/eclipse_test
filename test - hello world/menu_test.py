# -*- coding: utf-8 -*- 

import wx

class Example(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs) 
            
        self.InitUI()
        
    def InitUI(self):    

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_EXIT, '&Start', 'Start Job')
        fileMenu.Append(wx.ID_EXIT, '&End', 'End Job')
        qmi = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')
        #fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')
        #fitem = fileMenu.Append(wx.ID_EXIT, 'Start', 'Start Job')
        #fitem = fileMenu.Append(wx.ID_EXIT, 'End', 'End Job')
        menubar.Append(fileMenu, '&Record')
        self.SetMenuBar(menubar)
        
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

        self.SetSize((300, 200))
        self.SetTitle('Simple menu')
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