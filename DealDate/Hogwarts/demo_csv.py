import csv


def get_csv():
    with open('demo.csv', 'r',encoding='utf-8') as file:
        raw = csv.reader(file)

        for line in raw:
            print(line)

if __name__ == '__main__':
    get_csv()