import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDesktopWidget, QVBoxLayout, QCalendarWidget, QLabel, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDateTime, Qt, QDate


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        # self.initMenu()
        self.initMain()
        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()
        self.setStyleSheet("background-color : #E0D3F8;")


    def initMenu(self):

        #메뉴바
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        menubar.setStyleSheet("background-color:white;")

        menu = menubar.addMenu('Menu')
        setting = menubar.addMenu('Setting')
        check = menubar.addMenu('check')

        menu.addAction(self.buildMenu('프로그램 종료', 'Ctrl+Q', '프로그램을 종료합니다.'))
        menu.addAction(self.buildMenu('항상 위에 창 고정', 'Ctrl+A', '프로그램 창을 항상 맨 위에 유지합니다'))
        menu.addAction(self.buildMenu('저장된 스크린샷 보기', 'Ctrl+P', '지금까지의 예약 화면을 담은 스크린샷을 확인합니다.'))


        setting.addAction(self.buildMenu('월 다시 입력', 'Ctrl+M', '월을 다시 입력합니다.'))
        setting.addAction(self.buildMenu('날짜 다시 입력', 'Ctrl+D', '날짜를 다시 입력합니다.'))
        setting.addAction(self.buildMenu('시간 다시 입력', 'Ctrl+T', '시간을 다시 입력합니다.'))

        check.addAction(self.buildMenu('예약 로그 확인', 'Ctrl+L', '지금까지의 예약 기록을 확인합니다.')) 
        #메뉴바


    def initMain(self):
        
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()
        
        # self.lbl = QLabel(self)
        # date = cal.selectedDate()
        # self.lbl.setText(date.toString())

        # vbox.addWidget(cal)
        # vbox.addWidget(self.lbl)


    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()





    def showDate(self, date):
        self.lbl.setText(date.toString())

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def buildMenu(self, name, shortcut, text, triggerAct = qApp.quit):
        Action = QAction(QIcon('exit.png'), name, self)
        Action.setShortcut(shortcut)
        Action.setStatusTip(text)
        Action.triggered.connect(triggerAct)
        return Action

    def alwaysOnTop(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())