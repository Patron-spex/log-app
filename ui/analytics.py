from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class AnalyticsWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.plot_example()
    
    def plot_example(self):
        data = [20, 40, 15, 25]
        labels = ["Fahrzeug 1", "Fahrzeug 2", "Fahrzeug 3", "Fahrzeug 4"]
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.bar(labels, data)
        ax.set_title("Fahrzeugauslastung")
        self.canvas.draw()