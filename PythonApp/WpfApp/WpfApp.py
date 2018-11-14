import wpf

from System.Windows import Application, Window,MessageBox

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'WpfApp.xaml')
        
    def Button_Click(self, sender, e):
        MessageBox.Show(str('fdsfdsfds'))
        pass


if __name__ == '__main__':
    Application().Run(MyWindow())
