import csv

def exp(strr):
    with open('tabl.csv', 'r', encoding='utf-8') as f:
        reader= csv.reader(f, delimiter = ".")
        count = 0
        for row in reader:
            if count == 0:
                print(", ".join(row))
            elif strr in row:
                print(f'{row[0]}.{row[1]}.{row[2]}.{row[3]}')
            count += 1





