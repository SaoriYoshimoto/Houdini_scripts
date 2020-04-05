import hou
import sys
try:
    from PySide2.QtWidgets import*
    from PySide2.QtGui import*
    from PySide2.QtCore import*

except ImportError:
    from PySide.QtGui import*
    from PySide.QtCore import*
    
class Saori(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
#        hbox = QHBoxLayout()
        hbox = QVBoxLayout()
        self.setLayout(hbox)
        
        self.setGeometry(500, 300, 350, 110)
        self.setWindowTitle('Saori')
        
        radioGroup = QButtonGroup()
        
        radioBtn1 = QRadioButton("Option 1")
        hbox.addWidget(radioBtn1)        
        radioGroup.addButton(radioBtn1)
        
        radioBtn2 = QRadioButton("Option 2")
        hbox.addWidget(radioBtn2)        
        radioGroup.addButton(radioBtn2)
        
        radioBtn3 = QRadioButton("Option 3")
        hbox.addWidget(radioBtn3)        
        radioGroup.addButton(radioBtn3)
        
        radioBtn4 = QRadioButton("Option 4")
        hbox.addWidget(radioBtn4)        
        radioGroup.addButton(radioBtn4)
        
        radioBtn5 = QRadioButton("Option 5")
        hbox.addWidget(radioBtn5)        
        radioGroup.addButton(radioBtn5)
        
        radioBtn1.setChecked(True)

        
dialog = Saori()
dialog.show()
