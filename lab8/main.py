from lab8.src.data_loader import DataLoader
from lab8.src.analyzer import DataAnalyzer
from lab8.src.visualizer.line_chart import LineChart
from lab8.src.visualizer.bar_chart import BarChart
from lab8.src.visualizer.scatter_plot import ScatterPlot
from lab8.src.visualizer.multi_plot import MultiPlotVisualizer
from lab8.src.exporter import Exporter

def main():
    loader = DataLoader('lab8/data/dataset.csv')
    data = loader.load_data()

    analyzer = DataAnalyzer(data)
    print("Extreme values:\n", analyzer.get_extreme_values())

    line_chart = LineChart(data, x_col='day', y_col='temperature')
    line_chart.plot()

    bar_chart = BarChart(data, x_col='day', y_col='rain_probability')
    bar_chart.plot()

    scatter_plot = ScatterPlot(data, x_col='temperature', y_col='rain_probability')
    scatter_plot.plot()

    multi_plot = MultiPlotVisualizer(data)
    multi_plot.plot_subplots([
        ('line', 'day', 'temperature'),
        ('bar', 'day', 'rain_probability'),
    ])
