import requests
from bs4 import BeautifulSoup


links = []

with open("interviewbit_links.txt", "r") as f:
    for line in f:
        links.append(line.rstrip())
    f.close()


indices = []


with open("output.txt", "r") as f:
    for line in f:
        nline = line.rstrip()
        if len(nline) > 9:
            indices.append(nline[0:3])


indices = [int(index) for index in indices]

newlinks = []

for index in indices:
    newlinks.append(links[index - 1])


print(*newlinks, sep="\n")
