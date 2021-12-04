import csv

# membaca baris per baris
with open("/program/file_io/siswa.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)


