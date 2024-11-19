import matplotlib.pyplot as plt
from .base import Visualizer
from ..exporter import Exporter

class ScatterPlot(Visualizer):
    def __init__(self, data, x_col, y_col):
        super().__init__(data)
        self.x_col = x_col
        self.y_col = y_col

    def plot(self):
        plt.scatter(self.data[self.x_col], self.data[self.y_col])
        plt.title(f"Scatter plot: {self.x_col} vs {self.y_col}")
        plt.xlabel(self.x_col)
        plt.ylabel(self.y_col)
        Exporter.export_plot(f'output/{self.x_col}_vs_{self.y_col}_scatter_plot.png')
        self.show()
