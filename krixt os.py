from operator import truediv
from tkinter import font
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import sys, string, os


class Button(QPushButton):
    def __init__(self, button_text, parrent):
        super().__init__(button_text,parrent)
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            mimeData = QMimeData()
            drag = QDrag(self)
            drag.setMimeData(mimeData)
            drag.exec_(Qt.MoveAction)
  
class Window(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("KRIXT")
        self.setWindowIcon(QIcon("C:/Users/kim/Desktop/coding/KRIXT-os/kicon.png"))

        #fonts
        QFontDatabase.addApplicationFont("Coco Gothic.ttf")
        font = QFont("Coco Gothic", 10)

        self.resize(1920, 1080)
        self.setAcceptDrops(True)

        self.container = QWidget()
        self.container.setLayout(QGridLayout())
        
        self.container.setVisible(False)

        self.tbui = QLabel(" ", self)
        self.uih = QLabel(" ",self)
        self.cb = Button(" ", self)
        self.bb = QPushButton(" ",self)
        self.nb = QPushButton(" ",self)       
        self.nauih = QLabel(" ",self)
        self.note = QPlainTextEdit(" ",self)
        self.cnb = QPushButton(" ",self)
        self.tbui2 = QLabel(" ", self)
      
        self.button = QPushButton(" ", self)
        self.button.setGeometry(460,950,1000,10)
        self.button.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/white.png); border-radius : 20px")
        self.button.setVisible(True)

        self.button2 = QPushButton(" ", self)
        self.button2.setGeometry(485,950,1000,10)
        self.button2.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/white.png); border-radius : 20")
        self.button2.setVisible(False)

        self.uih.setVisible(False)
        self.nauih.setVisible(False)
        self.note.setVisible(False)
        self.cnb.setVisible(False)
        self.tbui.setVisible(True)
        self.tbui2.setVisible(True)
        self.button.clicked.connect(self.doAnimation)
        self.button2.clicked.connect(self.dostopAnimation)
        
        #self.uih.setGeometry(380,100,1180,820)
        self.cb.setFixedSize(100,100)
        self.bb.setFixedSize(100,100)
        self.nb.setFixedSize(100,100)
        self.nauih.setFixedSize(435,220)
        self.note.setFixedSize(410,195)
        self.cnb.setFixedSize(25,25)
        self.tbui.setFixedSize(120,840)
        self.tbui2.setFixedSize(120,840)

        self.cb.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/calcmedlogov6.png); border-radius : 10")
        self.bb.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/kiconv3.png); border-radius : 10")
        self.nb.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/nicon.png); border-radius : 10")
        self.uih.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/rbg3.png); border-radius : 20")
        self.nauih.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/rbg3.png); border-radius : 20")
        self.note.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/rbg3.png); border: none; color : white; font-size : 13pt") 
        self.note.setFont(font)
        self.cnb.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/sxc.png); border : none")
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.6)
        self.uih.setGraphicsEffect(self.opacity_effect)
        self.tbui.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/white.png); border-radius : 20")
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.7)
        self.tbui.setGraphicsEffect(self.opacity_effect)
        self.tbui2.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/white.png); border-radius : 20")
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0)
        self.tbui2.setGraphicsEffect(self.opacity_effect)

        
        self.cb.clicked.connect(self.click)
        self.bb.clicked.connect(self.openbrowser)
        self.nb.clicked.connect(self.opennotes)
        self.cnb.clicked.connect(self.closenotes)

        self.uih.move(380,100)
        self.cb.move(60,90)
        self.bb.move(60,200)
        self.nb.move(60,310)
        self.nauih.move(1110,680)
        self.note.move(1135,690)
        self.cnb.move(1120,690)
        self.tbui.move(50,80)


        self.btn_close = QPushButton(" ",clicked = self.closecalc)
        self.rf = self.result_field = QLineEdit()
        self.btn_result = QPushButton(' ',clicked = self.func_result)
        self.btn_clear = QPushButton(' ',clicked = self.clear_calc)
        self.btn_9 = QPushButton(' ',clicked = lambda:self.num_press('9'))
        self.btn_8 = QPushButton(' ',clicked = lambda:self.num_press('8'))
        self.btn_7 = QPushButton(' ',clicked = lambda:self.num_press('7'))
        self.btn_6 = QPushButton(' ',clicked = lambda:self.num_press('6'))
        self.btn_5 = QPushButton(' ',clicked = lambda:self.num_press('5'))
        self.btn_4 = QPushButton(' ',clicked = lambda:self.num_press('4'))
        self.btn_3 = QPushButton(' ',clicked = lambda:self.num_press('3'))
        self.btn_2 = QPushButton(' ',clicked = lambda:self.num_press('2'))
        self.btn_1 = QPushButton(' ',clicked = lambda:self.num_press('1'))
        self.btn_0 = QPushButton(' ',clicked = lambda:self.num_press('0'))
        self.btn_plus = QPushButton(' ',clicked = lambda:self.func_press('+'))
        self.btn_mins = QPushButton(' ',clicked = lambda:self.func_press('-'))
        self.btn_mult = QPushButton(' ',clicked = lambda:self.func_press('*'))
        self.btn_divd = QPushButton(' ',clicked = lambda:self.func_press('/'))


        self.container.setFixedSize(435,550) # set the window size of the container
        self.btn_9.setFixedSize(100,100)
        self.btn_8.setFixedSize(100,100)
        self.btn_7.setFixedSize(100,100)
        self.btn_6.setFixedSize(100,100)
        self.btn_5.setFixedSize(100,100)
        self.btn_4.setFixedSize(100,100)
        self.btn_3.setFixedSize(100,100)
        self.btn_2.setFixedSize(100,100)
        self.btn_1.setFixedSize(100,100)
        self.btn_0.setFixedSize(307,100)
        self.btn_plus.setFixedSize(100,100)
        self.btn_mins.setFixedSize(100,100)
        self.btn_mult.setFixedSize(100,100)
        self.btn_divd.setFixedSize(100,100)
        self.btn_result.setFixedSize(205,100)
        self.btn_clear.setFixedSize(205,100)
        self.btn_close.setFixedSize(25,25)

        self.container.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/rbg3.png); border-radius : 20")
        self.btn_close.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/sxc.png); border : none ")
        self.btn_9.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/9c.png); border : none")
        self.btn_8.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/8c.png); border : none")
        self.btn_7.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/7c.png); border : none")
        self.btn_6.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/6c.png); border : none")
        self.btn_5.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/5c.png); border : none")
        self.btn_4.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/4c.png); border : none")
        self.btn_3.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/3c.png); border : none")
        self.btn_2.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/2c.png); border : none")
        self.btn_1.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/1c.png); border : none")
        self.btn_0.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/0c.png); border : none")
        self.btn_plus.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/pc.png); border : none") 
        self.btn_mins.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/mc.png); border : none") 
        self.btn_mult.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/xc.png); border : none") 
        self.btn_divd.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/dc.png); border : none") 
        self.btn_result.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/ec.png); border : none") 
        self.btn_clear.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/rc.png); border : none")
        self.rf.setStyleSheet("color : white; border : none")

        self.container.layout().addWidget(self.btn_close,0,0)
        self.container.layout().addWidget(self.result_field,0,1,1,4)
        self.container.layout().addWidget(self.btn_result,1,0,1,2)
        self.container.layout().addWidget(self.btn_clear,1,2,1,2)
        self.container.layout().addWidget(self.btn_9,2,0)
        self.container.layout().addWidget(self.btn_8,2,1)
        self.container.layout().addWidget(self.btn_7,2,2)
        self.container.layout().addWidget(self.btn_plus,2,3)
        self.container.layout().addWidget(self.btn_6,3,0)
        self.container.layout().addWidget(self.btn_5,3,1)
        self.container.layout().addWidget(self.btn_4,3,2)
        self.container.layout().addWidget(self.btn_mins,3,3)
        self.container.layout().addWidget(self.btn_3,4,0)
        self.container.layout().addWidget(self.btn_2,4,1)
        self.container.layout().addWidget(self.btn_1,4,2)
        self.container.layout().addWidget(self.btn_mult,4,3)
        self.container.layout().addWidget(self.btn_0,5,0,1,3)
        self.container.layout().addWidget(self.btn_divd,5,3)
        self.layout().addWidget(self.container)

        self.container.move(1110,115) # how to move the entire program container

        #creating a grid in the uih window
       
        #wip


        self.showMaximized()
        #self.showFullScreen()
        self.setStyleSheet("background-image : url(C:/Users/kim/Desktop/coding/KRIXT-os/Krixtbg.png);")

        #self.setLayout(QVBoxLayout())
        self.temp_nums = []
        self.fin_num = []
        self.show()

    def doAnimation(self):
        self.button.setVisible(False)
        self.button2.setVisible(True)
        self.tbui2.setVisible(False)
        self.anim = QPropertyAnimation(self.uih, b"geometry")

        self.uih.setVisible(True)
        
        self.anim.setDuration(300)

        self.anim.setStartValue(QRect(380,1000,1180,820))
        self.anim.setEndValue(QRect(380,100,1180,820))

        self.anim.start()     

    def dostopAnimation(self):
        self.tbui2.setVisible(True)
        self.button.setVisible(True)
        self.button2.setVisible(False)
        self.container.setVisible(False)
        self.note.setVisible(False)
        self.cnb.setVisible(False)
        self.nauih.setVisible(False)
        self.anim = QPropertyAnimation(self.uih, b"geometry")

        self.uih.setVisible(True)

        self.anim.setDuration(300)

        self.anim.setStartValue(QRect(380,100,1180,820))
        self.anim.setEndValue(QRect(380,1000,1180,820))

        self.anim.start()

    def num_press(self,key_number):
        self.temp_nums.append(key_number)
        temp_string = ''.join(self.temp_nums)
        if self.fin_num:
            self.result_field.setText(''.join(self.fin_num) + temp_string)
        else :
            self.result_field.setText(temp_string)
    def func_press(self, operator):
        temp_strings = ''.join(self.temp_nums)
        self.fin_num.append(temp_strings)
        self.fin_num.append(operator)
        self.temp_nums = []
        self.result_field.setText(''.join(self.fin_num))
    def func_result(self):
        fin_string = ''.join(self.fin_num) + ''.join(self.temp_nums)
        result_string = eval(fin_string)
        fin_string += '='
        fin_string += str(result_string)
        self.result_field.setText(fin_string)
    def clear_calc(self):
        self.result_field.clear()
        self.temp_nums = []
        self.fin_num = []

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        positionn = event.pos()
        self.cb.move(positionn)
        event.accept()

    def closecalc(self):
        self.container.setVisible(False)


    def click(self):
        
        self.container.setVisible(True)
        
    def openbrowser(self):
        #os.system("C:/Users/kim/Desktop/coding/KRIXT-os/browser/browser.exe")
        print("this is bugged")
    def opennotes(self):
        self.nauih.setVisible(True)
        self.note.setVisible(True)
        self.cnb.setVisible(True)

    def closenotes(self):
        self.nauih.setVisible(False)
        self.note.setVisible(False)
        self.cnb.setVisible(False)


    

app = QApplication(sys.argv)
app.setStyle(QStyleFactory.create('Cleanlooks'))
window = Window()
window.show()
sys.exit(app.exec_())

'''
to do next:

custom browser

'''

# how i name my update
# [Version-changes(in short)-Version of the new update(optional or when added a new program here)-G/B/M(good or bad or mid)-p/np/r/F(prototype not prototype or release or fixes)]