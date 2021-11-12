import csv
import matplotlib.pyplot as plt


data = []
with open(r"/home/ubuntu/Projects/project3/population-estimates_csv.csv", "r") as k:
    read = csv.reader(k)
    for i in read:
        data.append(i)


ind_year = data[0].index("Year")
ind_population = data[0].index("Population")


d = {}
for i in range(1, len(data)):
    if data[i][0] == "India":
        if data[i][ind_year] in d:
            d[data[i][ind_year]] += data[i][ind_population]
        else:
            d[data[i][ind_year]] = data[i][ind_population]


plt.figure(figsize=(20, 10))
plt.xticks(rotation=90)
plt.bar(list(d.keys()), list(d.values()))
plt.show()
