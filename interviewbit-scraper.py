from bs4 import BeautifulSoup
import os
import csv
import re

url = "interview_problems.html"

# response = urllib.request.urlopen(url, timeout=1)
html = open(url, "r")
soup = BeautifulSoup(html, "html.parser")

probs = []


def title_to_link(title):
    ltitle = title.lower()
    ltitle = ltitle.split(" ")
    return "https://www.interviewbit.com/problems/" + "-".join(ltitle)


for prob in soup.find_all("div", {"class": "pl-problem-tile"}):
    p = {}
    data = prob.text.split("\n")
    data = [s.strip() for s in data if re.search(r"\w+", s)]

    # print(data)

    # ['Gas Station', 'Greedy Algorithm', 'medium', '56 Mins', '46809', 'Asked in']

    p["title"] = data[0]
    p["tag"] = data[1]
    p["difficulty"] = data[2]
    p["avg_time"] = data[3]
    p["link"] = title_to_link(p["title"])
    p["company"] = "NS"

    probs.append(p)


print(probs[len(probs) // 2])
print(len(probs))

with open("all" + ".csv", "w", newline="") as output:
    dwriter = csv.DictWriter(
        output, ["title", "tag", "difficulty", "avg_time", "link", "company"]
    )
    dwriter.writeheader()
    dwriter.writerows(probs)
