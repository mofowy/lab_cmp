import matplotlib.pyplot as plt
from .base import Visualizer
from ..exporter import Exporter

class MultiPlotVisualizer(Visualizer):
    def __init__(self, data):
        super().__init__(data)

    def plot_subplots(self, plots):
        fig, axes = plt.subplots(1, len(plots), figsize=(15, 5))
        for ax, (plot_type, x_col, y_col) in zip(axes, plots):
            if plot_type == 'line':
                ax.plot(self.data[x_col], self.data[y_col])
            elif plot_type == 'bar':
                ax.bar(self.data[x_col], self.data[y_col])
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
        plt.tight_layout()
        Exporter.export_plot('output/MixedPlot.png')
        self.show()
