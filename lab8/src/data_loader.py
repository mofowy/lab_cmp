import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
            print("Data loaded successfully")
        except Exception as e:
            print(f"Error loading data: {e}")

        # Перевірка на пропущені значення
        if self.data.isnull().sum().any():
            print("Warning: There are missing values in the dataset.")
        return self.data
