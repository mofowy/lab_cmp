import matplotlib.pyplot as plt
from ..exporter import Exporter

class LineChart:
    def __init__(self, data, x_col, y_col):
        self.data = data
        self.x_col = x_col
        self.y_col = y_col

    def plot(self):
        if self.x_col not in self.data.columns or self.y_col not in self.data.columns:
            print(f"Columns {self.x_col} or {self.y_col} not found in data!")
            return
        
        plt.figure()
        plt.plot(self.data[self.x_col], self.data[self.y_col])
        plt.title(f"Line chart: {self.x_col} vs {self.y_col}")
        plt.xlabel(self.x_col)
        plt.ylabel(self.y_col)
        plt.grid(True)
        Exporter.export_plot(f'output/{self.x_col}_vs_{self.y_col}_line_chart.png')
        plt.show()