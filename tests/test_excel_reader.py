from app.utils.excel_reader import ExcelReader


def test_excel_reader():
    data = ExcelReader.read_data("test_data/login_data.xlsx")

    print(data)

    assert len(data) == 3