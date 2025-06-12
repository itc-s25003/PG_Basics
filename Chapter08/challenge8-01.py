import statistics

data = [1, 2, 3, 4, 5]
va = statistics.variance(data)
sd = statistics.stdev(data)

print("SD: {}".format(sd))
print("Variance: {}".format(va))
