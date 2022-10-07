from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import os
import csv

with open("leetcode_links.txt") as file:
    lines = file.readlines()
    links = [line.rstrip() for line in lines]

# print(links)


def getproblemsbytag(tagname):
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

        prob["tag"] = tagname
        prob["number"] = data[0]
        prob["title"] = data[1]
        prob["link"] = data[4]
        prob["acceptance"] = data[2]
        prob["difficulty"] = data[3]

        mainlist.append(prob)

    return mainlist


count = 1


with open("result.csv", "w", newline="") as output:
    dwriter = csv.DictWriter(
        output, ["tag", "number", "title", "link", "acceptance", "difficulty"]
    )
    dwriter.writeheader()

    for link in links[25:]:
        # open the link

        options = Options()
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )
        driver.get(link)

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "tbody",
                )
            )
        )

        # get the tag

        tag = driver.find_element(By.TAG_NAME, "h3").text

        # get tbody html

        html_source = driver.find_element(By.TAG_NAME, "tbody").get_attribute(
            "innerHTML"
        )

        # print(html_source)

        with open("main.html", "w") as f:
            f.write(html_source)
            f.close()

        probs = getproblemsbytag(tag)

        # use csv to write in file

        dwriter.writerows(probs)

        print(links.index(link) + 1, tag, len(probs))

        driver.quit()


# mainlist = []


# for elem in driver.find_elements(By.CSS_SELECTOR, "tbody > tr"):
#     prob = {}
#     prob["number"] = elem.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
#     prob["title"] = elem.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text
#     prob["link"] = elem.find_element(By.TAG_NAME, "a").get_attribute("href")
#     prob["acceptance"] = elem.find_element(By.CSS_SELECTOR, "td:nth-child(4)").text
#     prob["difficulty"] = elem.find_element(By.CSS_SELECTOR, "span").text

#     mainlist.append(prob)

#     print(len(mainlist))

# # keys = mainlist[0].keys()


# driver.quit()
