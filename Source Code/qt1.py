from qtGui import *
class FormHello(QWidget):
   def __init__(self):
    QWidget.__init__(self)
    self.setCaption("Hello World !")
    self.show()
    app = QApplication([])
    fm = FormHello()
    app.setMainWidget(fm)
    app.exec_loop()
