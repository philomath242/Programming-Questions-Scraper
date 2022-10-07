from urllib.request import proxy_bypass
from bs4 import BeautifulSoup
import os
import csv

url = "main.html"

# response = urllib.request.urlopen(url, timeout=1)
html = open(url, "r")
soup = BeautifulSoup(html, "html.parser")

mainlist = []

for elem in soup.find_all("tr"):
    prob = {}

    # https://leetcode.com/problems/3sum-closest
    data = []
    # ['16', '3Sum Closest', '46.1%', 'Medium', 'https://leetcode.com/problems/3sum-closest']
    for td in elem.find_all("td"):
        data.append(td.text)

    for link in elem.find_all("a"):
        data.append("https://leetcode.com" + link.get("href"))
        data.append(link.text)

    del data[0]
    del data[4]

    prob["tag"] = "Binary Tree"
    prob["number"] = data[0]
    prob["title"] = data[1]
    prob["link"] = data[4]
    prob["acceptance"] = data[2]
    prob["difficulty"] = data[3]

    mainlist.append(prob)
    print(len(mainlist))


# print(mainlist)

keys = mainlist[0].keys()

if os.path.exists("result.csv"):
    os.remove("result.csv")

with open("result.csv", "w", newline="") as output:
    dwriter = csv.DictWriter(output, keys)
    dwriter.writeheader()
    dwriter.writerows(mainlist)
