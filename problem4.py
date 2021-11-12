import csv
import matplotlib.pyplot as plt


data = []
with open(r"/home/ubuntu/Projects/project3/population-estimates_csv.csv", "r") as k:
    read = csv.reader(k)
    for i in read:
        data.append(i)
ind_year = data[0].index("Year")
ind_population = data[0].index("Population")
r = {}
for i in range(1, len(data)):
    if data[i][0] in r:
        if data[i][ind_year] in r[data[i][0]]:
            r[data[i][0]][data[i][ind_year]] += float(data[i][ind_population])
        else:
            r[data[i][0]][data[i][ind_year]] = float(data[i][ind_population])
    else:
        r[data[i][0]] = {}


asean_countries = [
    "Brunei Darussalam",
    "Cambodia",
    "Indonesia",
    "Lao People's Democratic Republic",
    "Malaysia",
    "Myanmar",
    "Philippines",
    "Singapore",
    "Thailand",
    "Viet Nam",
]


r1 = {}
for i in asean_countries:
    r1[i] = r[i]


l1 = [[] for i in range(2004, 2015)]
for j in range(2004, 2015):
    for i in asean_countries:
        l1[j - 2004].append(r1[i][str(j)])


l = [[] for i in range(0, 10)]
for i in range(0, len(l1[0])):
    for j in range(0, len(l1)):
        l[i].append(l1[j][i])


years = [i for i in range(2004, 2015)]


def p(l, a):
    o = []
    for i in range(len(l)):
        o.append(l[i] + a)
    return o


plt.figure(figsize=(10, 10))
width = 0.2
for i in range(len(l)):
    plt.bar(p(years, i * 0.05), l[i], width=0.1)
plt.legend(asean_countries, bbox_to_anchor=(1.05, 1))
plt.xticks(years)
plt.show()
