import wx
class Frame1(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self, parent=parent, title='Example', pos=(0, 0), size=(800, 800))
        self.panel = wx.Panel(self)
        #鼠标左键抬起时触发时间绑定带OnClick函数
        self.panel.Bind(wx.EVT_LEFT_UP, self.OnClick)
 
    def OnClick(self,event):
        posm=event.GetPosition()
        wx.StaticText(parent=self.panel,label='Hello World',pos=(posm.x,posm.y))