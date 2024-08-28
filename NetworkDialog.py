import sys
import socket
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit
from PyQt6.QtCore import QTimer, Qt
from concurrent.futures import ThreadPoolExecutor, TimeoutError

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("IP Checker")
        self.setGeometry(100, 100, 400, 200)

        self.hostname_input = QLineEdit(self)
        self.hostname_input.setPlaceholderText("Enter hostname")

        self.result_label = QLabel(self)
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.hostname_input)
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_ip)
        self.timer.start(1000)  # هر ۱ ثانیه بررسی می‌کند

        self.executor = ThreadPoolExecutor(max_workers=1)

    def check_ip(self):
        hostname = self.hostname_input.text()
        if not hostname:
            self.result_label.setText("Please enter a hostname.")
            return
        
        future = self.executor.submit(self.resolve_hostname, hostname)
        try:
            ip_address = future.result(timeout=1)  # محدود کردن زمان به ۱ ثانیه
            self.result_label.setText(f'The IP address of {hostname} is {ip_address}')
        except TimeoutError:
            self.result_label.setText(f'Timeout: Could not resolve {hostname} within 1 second.')
        except socket.gaierror:
            self.result_label.setText(f'Error: Could not resolve {hostname}.')

    @staticmethod
    def resolve_hostname(hostname):
        return socket.gethostbyname(hostname)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())