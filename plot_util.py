import datetime
import numpy

def x_fmt(x, y):
    return datetime.datetime.fromtimestamp(x).strftime("%Y-%m-%d")

def plot_regression(plt, days, total_vaccs, deg):
  mymodel = numpy.poly1d(numpy.polyfit(days, total_vaccs, deg))
  myline = numpy.linspace(1.609e9, 1.628e9, 10000)
  # print(mymodel)

  print(mymodel)

  # r-squared
  # fit values, and mean
  yhat = mymodel(days)                         # or [p(z) for z in x]
  ybar = numpy.sum(total_vaccs)/len(total_vaccs)          # or sum(y)/len(y)
  ssreg = numpy.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
  sstot = numpy.sum((total_vaccs - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
  rsquared = ssreg / sstot
  print(rsquared)

  x = myline 
  y = mymodel(myline)

  plt.plot(x,y)
