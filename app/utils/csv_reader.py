import csv


class CSVReader:
    @staticmethod
    def read_data(file_path):
        """
        Read test data from a CSV file.

        Returns:
            List of dictionaries.
        """
        data = []

        with open(file_path, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                data.append(row)

        return data