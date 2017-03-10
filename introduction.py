# -*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore


class HelpWindow(QtGui.QDialog):
    'help window'
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.initUI()

    def initUI(self):
        self.resize(400,400)
        self.setWindowTitle('Introduction')
        self.intro_text= u'这是一款人机对战游戏\n玩家(P)使用W/A/S/D键\n' \
                         u'控制一条逐渐增长的巨龙，\n与敌人(E)决一死战，' \
                         u'\n在将对手逼上梁山的同时\n要避免自己无路可走。' \
                         u'\n按R键重新开局。\n祝游戏愉快～\n\n\n\n\n' \
                         u'Designed by Xuetao Chen & Haohong Wang'

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
# or use label?
        back_button = QtGui.QPushButton('Back',parent=self)
        back_button.clicked.connect(self.reject)
        vbox.addWidget(back_button)

        self.setLayout(vbox)

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawText(event,qp)
        qp.end()

    def drawText(self, event, qp):
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont('Decorative', 13))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.intro_text)


class EndWindow(QtGui.QDialog):
    'game finished window'
    def __init__(self,signal,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.end_text = setEndText(signal)
        self.initUI()

    def initUI(self):
        self.resize(200,200)
        self.setWindowTitle('Game Over')

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        # or use label?
        return_button = QtGui.QPushButton('Return', parent=self)
        return_button.clicked.connect(self.reject)
        vbox.addWidget(return_button)

        self.setLayout(vbox)

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawText(event,qp)
        qp.end()

    def drawText(self, event, qp):
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont('Decorative', 13))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.end_text)


def setEndText(signal):
    'set the end_text according to the game signal.'
    win_text = 'Congratulations!\n :D'
    defeat_text = 'Sorry\nDefeat >_<'
    if signal == 1:
        return win_text
    elif signal == 2:
        return defeat_text
