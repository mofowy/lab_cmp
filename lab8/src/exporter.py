import os
import matplotlib.pyplot as plt

class Exporter:
    @staticmethod
    def export_plot(filename):
        base_dir = os.path.join(os.path.dirname(__file__), "..")
        output_dir = os.path.join(base_dir, os.path.dirname(filename))
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        plt.savefig(os.path.join(output_dir, os.path.basename(filename)), format="png")
        print(f"Plot saved to {os.path.join(output_dir, os.path.basename(filename))}")
        plt.show()
        plt.close()