import hou
import sys
try:
    from PySide2.QtWidgets import*
    from PySide2.QtGui import*
    from PySide2.QtCore import*

except ImportError:
    from PySide.QtGui import*
    from PySide.QtCore import*

        
class Saori(QMainWindow,QWidget):
    def __init__(self, parent = None):
        super(Saori, self).__init__(parent)
        self.setObjectName("M_Tool_Window")
        self.setWindowTitle("MonkeyWork CacheOut Window")
        self._initUI()
        self.errorDialog = QErrorMessage(self) # QErrorMessageインスタンスの保持
        
    def _initUI(self):
        wrapper = QWidget()
        self.setCentralWidget(wrapper)
        
        self.setStyleSheet(hou.qt.styleSheet())#houdini UI Style
        self.setProperty("houdiniStyle", True)#houdini UI Style  


        #-----------------------------------------------------------------------
        # First row
        #-----------------------------------------------------------------------  
        firstHolizontalArea = QHBoxLayout()
        self.setGeometry(500, 300, 400, 300)
        
        labelEditArea = QHBoxLayout()
        
        
        lineName = QLabel("name")
        labelEditArea.addWidget(lineName)
               
        label = QLineEdit()
        labelEditArea.addWidget(label)
        
        labelEditArea.addWidget(self._makeHorizontalLine())
        
        firstHolizontalArea.addLayout(labelEditArea)
        

        #-----------------------------------------------------------------------
        # Second row
        #----------------------------------------------------------------------- 

        secondVerticalArea = QVBoxLayout()
        secondVerticalArea.setSpacing(20)

        radioArea = QHBoxLayout()
        secondVerticalArea.addLayout(radioArea)

        radioGroup = QButtonGroup(self)
        radioBtn1 = QRadioButton("Lucky 1")
        radioArea.addWidget(radioBtn1)
        radioGroup.addButton(radioBtn1)
        radioBtn2 = QRadioButton("Lucky 2")
        radioArea.addWidget(radioBtn2)
        radioGroup.addButton(radioBtn2)
        radioBtn1.setChecked(True)

        secondVerticalArea.addWidget(self._makeHorizontalLine())

        #-----------------------------------------------------------------------
        # Third row
        #----------------------------------------------------------------------- 

        thirdHolizontalArea = QVBoxLayout()
        thirdHolizontalArea.setSpacing(20)

        radioArea = QVBoxLayout()
        thirdHolizontalArea.addLayout(radioArea)

        radioGroup = QButtonGroup(self)
        radioBtn1 = QRadioButton("Yeah! 1")
        radioArea.addWidget(radioBtn1)
        radioGroup.addButton(radioBtn1)
        radioBtn2 = QRadioButton("Yeah! 2")
        radioArea.addWidget(radioBtn2)
        radioGroup.addButton(radioBtn2)
        radioBtn3 = QRadioButton("Yeah! 3")
        radioArea.addWidget(radioBtn3)
        radioGroup.addButton(radioBtn3)
        radioBtn1.setChecked(True)

        thirdHolizontalArea.addWidget(self._makeHorizontalLine())    
        
        parentLayout = QVBoxLayout()
        parentLayout.setSpacing(20)
        parentLayout.addLayout(firstHolizontalArea)
        parentLayout.addLayout(secondVerticalArea)
        parentLayout.addLayout(thirdHolizontalArea)

        wrapper.setLayout(parentLayout)
        
    def _makeHorizontalLine(self):
        hline = QFrame()
        hline.setFrameShape(QFrame.HLine)
        hline.setFrameShadow(QFrame.Sunken)
        return hline
                
        
dialog = Saori()
dialog.show()
