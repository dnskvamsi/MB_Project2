import csv
import matplotlib.pyplot as plt


data = []
with open(r"/home/ubuntu/Projects/project3/population-estimates_csv.csv", "r") as k:
    read = csv.reader(k)
    for i in read:
        data.append(i)


ind_year = data[0].index("Year")
ind_population = data[0].index("Population")
saarc_countries = [
    "Afghanistan",
    "Bangladesh",
    "Bhutan",
    "India",
    "Maldives",
    "Nepal",
    "Pakistan",
    "Sri Lanka",
]

d3 = {}
for i in range(1, len(data)):
    if data[i][0] in saarc_countries:
        if data[i][0] in d3:
            d3[data[i][0]] += float(data[i][ind_population])
        else:
            d3[data[i][0]] = float(data[i][ind_population])

plt.bar(list(d3.keys()), list(d3.values()))
plt.xticks(rotation=90)
plt.show()
