import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import datetime
from plot_util import x_fmt
import impfdashboad_api

days = []
total_vaccs = []

impfdashboad_api.download_data();

with open("./data.csv") as f:
  csv_reader = csv.reader(f, delimiter='\t')
  i = 0
  for row in csv_reader:
    if i == 0:
      i += 1
      continue

    date = datetime.datetime.strptime(row[0], "%Y-%m-%d")
    days.append(datetime.datetime.timestamp(date))
    total_vaccs.append(int(row[1]))

    i += 1
  
fig, ax = plt.subplots()
ax.plot(days, total_vaccs)

ax.xaxis.set_major_formatter(tick.FuncFormatter(x_fmt))

ax.set(xlabel='Datum', ylabel='Gesamte Impfungen', title='Impfungen')
ax.grid()

plt.show()