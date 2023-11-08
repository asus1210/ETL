import yaml
import pandas as pd
from pathlib import Path

class ExtractData:
    def __init__(self) -> None:
        self.config_data = self.load_config_data()

    @staticmethod
    def load_config_data():
        with open("../config/config.yaml", "r") as f:
            return yaml.safe_load(f)

    def extract_csv(self) -> list:
        dataframe_list = []
        config_raw_data = self.config_data["file_paths"]["raw_data_path"]
        for csv_file in Path(config_raw_data).glob("*.csv"):
            dataframe_list.append(self.csv_to_dataframe(csv_file))
        return dataframe_list

    @staticmethod
    def csv_to_dataframe(csv_file_path: str) -> pd.DataFrame:
        return pd.read_csv(csv_file_path)

if __name__ == "__main__":
    obj = ExtractData()
    df_list = obj.extract_csv()
    print(len(df_list))