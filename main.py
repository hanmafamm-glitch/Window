
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First Window")
        self.resize(400, 300)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())