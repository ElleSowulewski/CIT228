import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'temps.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)

dates = []
highs = []
lows = []
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header_row=next(csv_reader)
    for row in csv_reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        highs.append(row[4])
        lows.append(row[5])
        dates.append(current_date)

plt.scatter(dates, lows, color = "blue")
plt.scatter(dates, highs, color = "red")
plt.ylabel('Temperature')
plt.xlabel('Date')
plt.title('San Fransisco Temps')

plt.show()