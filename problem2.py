import csv
import matplotlib.pyplot as plt


data = []
with open(r"/home/ubuntu/Projects/project3/population-estimates_csv.csv", "r") as k:
    read = csv.reader(k)
    for i in read:
        data.append(i)


ind_year = data[0].index("Year")
ind_population = data[0].index("Population")

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


d2 = {}
for i in range(1, len(data)):
    if data[i][0] in asean_countries and data[i][ind_year] == "2014":
        d2[data[i][0]] = data[i][ind_population]


plt.bar(list(d2.keys()), list(d2.values()))
plt.xticks(rotation=45)
plt.show()
