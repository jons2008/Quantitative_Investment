import wx
from New import class1 as aa
if __name__ == '__main__':
    app = wx.App()
    frame = aa.Frame1(None)
    frame.Show()
    app.MainLoop()