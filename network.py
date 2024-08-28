import os, sys, time, socket
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class Ui_WaitingNetworkDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("WaitingNetworkDialog")
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.resize(875, 619)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Frame_Waiting_Background = QtWidgets.QFrame(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Frame_Waiting_Background.sizePolicy().hasHeightForWidth())
        self.Frame_Waiting_Background.setSizePolicy(sizePolicy)
        self.Frame_Waiting_Background.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Frame_Waiting_Background.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Frame_Waiting_Background.setObjectName("Frame_Waiting_Background")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Frame_Waiting_Background)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Frame_Waiting_Content = QtWidgets.QFrame(parent=self.Frame_Waiting_Background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Frame_Waiting_Content.sizePolicy().hasHeightForWidth())
        self.Frame_Waiting_Content.setSizePolicy(sizePolicy)
        self.Frame_Waiting_Content.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Frame_Waiting_Content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Frame_Waiting_Content.setObjectName("Frame_Waiting_Content")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Frame_Waiting_Content)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Waiting_Network_Label_Content = QtWidgets.QLabel(parent=self.Frame_Waiting_Content)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setStrikeOut(False)
        self.Waiting_Network_Label_Content.setFont(font)
        self.Waiting_Network_Label_Content.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Waiting_Network_Label_Content.setObjectName("Waiting_Network_Label_Content")
        self.verticalLayout_2.addWidget(self.Waiting_Network_Label_Content)
        self.verticalLayout_4.addWidget(self.Frame_Waiting_Content)
        self.Frame_Waiting_Logo = QtWidgets.QFrame(parent=self.Frame_Waiting_Background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Frame_Waiting_Logo.sizePolicy().hasHeightForWidth())
        self.Frame_Waiting_Logo.setSizePolicy(sizePolicy)
        self.Frame_Waiting_Logo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Frame_Waiting_Logo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Frame_Waiting_Logo.setObjectName("Frame_Waiting_Logo")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Frame_Waiting_Logo)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Waiting_Network_Label_Logo = QtWidgets.QLabel(parent=self.Frame_Waiting_Logo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Waiting_Network_Label_Logo.sizePolicy().hasHeightForWidth())
        self.Waiting_Network_Label_Logo.setSizePolicy(sizePolicy)
        self.Waiting_Network_Label_Logo.setText("")
        self.Waiting_Network_Label_Logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Waiting_Network_Label_Logo.setObjectName("Waiting_Network_Label_Logo")
        self.verticalLayout_3.addWidget(self.Waiting_Network_Label_Logo)
        self.verticalLayout_4.addWidget(self.Frame_Waiting_Logo)
        self.frame = QtWidgets.QFrame(parent=self.Frame_Waiting_Background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Waiting_Network_Label_Ip = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.Waiting_Network_Label_Ip.setFont(font)
        self.Waiting_Network_Label_Ip.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Waiting_Network_Label_Ip.setObjectName("Waiting_Network_Label_Ip")
        self.horizontalLayout_2.addWidget(self.Waiting_Network_Label_Ip)
        self.verticalLayout_4.addWidget(self.frame)
        self.Frame_Waiting_Buttons = QtWidgets.QFrame(parent=self.Frame_Waiting_Background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Frame_Waiting_Buttons.sizePolicy().hasHeightForWidth())
        self.Frame_Waiting_Buttons.setSizePolicy(sizePolicy)
        self.Frame_Waiting_Buttons.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Frame_Waiting_Buttons.setMinimumSize(QtCore.QSize(16777215, 50))
        self.Frame_Waiting_Buttons.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Frame_Waiting_Buttons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Frame_Waiting_Buttons.setObjectName("Frame_Waiting_Buttons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Frame_Waiting_Buttons)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_reset = QtWidgets.QPushButton(parent=self.Frame_Waiting_Buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_reset.sizePolicy().hasHeightForWidth())
        self.pushButton_reset.setSizePolicy(sizePolicy)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.horizontalLayout.addWidget(self.pushButton_reset)
        self.pushButton_continues = QtWidgets.QPushButton(parent=self.Frame_Waiting_Buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_continues.sizePolicy().hasHeightForWidth())
        self.pushButton_continues.setSizePolicy(sizePolicy)
        self.pushButton_continues.setObjectName("pushButton_continues")
        self.horizontalLayout.addWidget(self.pushButton_continues)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_4.addWidget(self.Frame_Waiting_Buttons)
        self.verticalLayout.addWidget(self.Frame_Waiting_Background)

        self.Waiting_Network_Label_Content.setText("Waiting For Network ...")
        self.Waiting_Network_Label_Ip.setText("000.000.000.000")
        self.pushButton_reset.setText("Reboot")
        self.pushButton_reset.clicked.connect(self.function_reset)
        self.pushButton_continues.setText("Continuse with out network")
        self.pushButton_continues.clicked.connect(self.function_continues)

        gif = QtGui.QMovie("Loading_3.gif")
        self.Waiting_Network_Label_Logo.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.Waiting_Network_Label_Logo.setMovie(gif)
        gif.start()

        self.setStyleSheet("""
             #Frame_Waiting_Background{
            background-color:  white;
            borde: 1px solid white;
            border-radius: 15px;
            }
            #Waiting_Network_Label_Content{
                color: black;
            }
            QPushButton{
                color: white;
                background-color: #3868a7;
                border: 1px solid white;
                border-radius: 9px;
            }
            QPushButton:hover{
                color: black;
                background-color: #afc3dc;
                border: 0px solid blabk;
                border-radius: 9px;
            }
            """)
        
        self.hostname = "googles.com"
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_ip)
        self.timer.start(1000)
        self.executor = ThreadPoolExecutor(max_workers=1)

        self.timer_close = QTimer(self)
        self.timer_close.timeout.connect(self.close_window)


        
    def check_ip(self):
        
        if not self.hostname:
            return
        
        future = self.executor.submit(self.resolve_hostname, self.hostname)
        try:
            ip_address = future.result(timeout=1)  # محدود کردن زمان به ۱ ثانیه
            self.Waiting_Network_Label_Ip.setText(f' {ip_address}')
            self.timer_close.start(1000)
        except TimeoutError:
            self.Waiting_Network_Label_Ip.setText(f'Could not resolve {self.hostname}')
        except socket.gaierror:
            self.Waiting_Network_Label_Ip.setText(f'Could not resolve {self.hostname}.')

    def function_reset(self):
        print("function_reset")

    def function_continues(self):
        print("function_continues")
        self.hostname = "google.com"

    @staticmethod
    def resolve_hostname(hostname):
        return socket.gethostbyname(hostname)

    def close_window(self):
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_WaitingNetworkDialog()
    ui.show()
    sys.exit(app.exec())
