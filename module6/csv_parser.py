import csv

class CsvParser:
    def __init__(self, file_name):
        self.r_file = file_name

    def save_as(self, new_file_name, delimiter):

        with open(self.r_file, "r") as r_file:
            with open(new_file_name, "w") as w_file:
                csv_reader = csv.reader(r_file)
                csv_writer = csv.writer(w_file, delimiter=delimiter)
                for line in csv_reader:
                    csv_writer.writerow(line)

    def get_country_profit(self, country):
        with open(self.r_file, "r") as r_file:
            csv_reader = csv.reader(r_file)
            total = 0
            for line in csv_reader:
                if line[1].startswith(country):
                    total = total + float(line[-1])
            return round(total, 2)

    def sell_over(self, item_type: str, threshold: int):
        with open(self.r_file, "r") as r_file:
            csv_reader = csv.reader(r_file)
            lst = []
            for line in csv_reader:
                if line[2].startswith(item_type) and int(line[-6]) > threshold:
                    lst.append(line[1])
            lst.sort()
        return lst

