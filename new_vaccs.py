import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import datetime
from plot_util import x_fmt, plot_regression
import impfdashboad_api

days = []
new_vaccs = []
avg_new_vaccs = []

def plot_timeframe(plt, days, new_vaccs, num_days):
  used_days = days[:num_days]
  used_vaccs = new_vaccs[:num_days]
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
    new_vaccs.append(int(row[2]))

    i += 1

block_size = 14

for i in range(len(new_vaccs)):
  if i < block_size:
    avg_new_vaccs.append(new_vaccs[i])
    continue

  sum = 0
  for vaccs_day in new_vaccs[i-block_size:i]:
    sum += vaccs_day
  
  avg_new_vaccs.append(sum / block_size)

fig, ax = plt.subplots()
ax.scatter(days, avg_new_vaccs)
ax.set_ylim([0, 1e6])

# for deg in range(1, 5):
#   plot_regression(ax, days, avg_new_vaccs, deg)

# plot_regression(ax, days, new_vaccs, 2)

ax.xaxis.set_major_formatter(tick.FuncFormatter(x_fmt))

ax.grid()
plt.show()
