import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import datetime
import impfdashboad_api
from plot_util import x_fmt, plot_regression

days = []
total_vaccs = []
def plot_timeframe(plt, days, total_vaccs, num_days):
  used_days = days[:num_days]
  used_vaccs = total_vaccs[:num_days]
  plot_regression(ax, used_days, used_vaccs, 2)


impfdashboad_api.download_data();

with open("./data.csv") as f:
# with open("./Germany.csv") as f:
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
ax.scatter(days, total_vaccs)
ax.set_ylim([0, 1e8])

for deg in range(2, 5):
  plot_regression(ax, days, total_vaccs, deg)

# plot_regression(ax, days, total_vaccs, 2)

ax.xaxis.set_major_formatter(tick.FuncFormatter(x_fmt))

ax.grid()
plt.show()