from app.utils.csv_reader import CSVReader
from app.utils.excel_reader import ExcelReader


class DataProvider:
    @staticmethod
    def login_data():
        """
        Return login test data from CSV.
        """
        return CSVReader.read_data("test_data/login_data.csv")

    @staticmethod
    def login_excel_data():
        """
        Return login test data from Excel.
        """
        return ExcelReader.read_data("test_data/login_data.xlsx")