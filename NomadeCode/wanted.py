from playwright.sync_api import sync_playwright
import time #대기시간 생성
from bs4 import BeautifulSoup
import csv


p = sync_playwright().start()
browser = p.chromium.launch(headless=False)

page = browser.new_page()

#page.goto("https://www.wanted.co.kr/")
page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")

time.sleep(5)

page.click("button.Aside_searchButton__Ib5Dn")
#page.locator("button.Aside_searchButton__Ib5Dn").click()

time.sleep(5)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

time.sleep(5)

page.keyboard.down("Enter")

time.sleep(5)

page.click("a#search_tab_position")

time.sleep(5)

for x in range(5):
    time.sleep(5)
    page.keyboard.down("End")

content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="JobCard_container__zQcZs")

jobs_db = []

for job in jobs:
    link = f"https://www.wanted.co.kr/{job.find('a')['href']}"
    title = job.find("strong", class_="JobCard_title___kfvj").text
    company_name = job.find("span", class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__company__ByVLu wds-nkj4w6").text
    job = {
        "title": title,
        "company": company_name,
        "link": link
    }
    jobs_db.append(job)

file = open("wanted.csv", "w")

writer = csv.writer(file)
writer.writerow(["Title","Company", "Link"])

for job in jobs_db:
    writer.writerow(job.values())

file.close()









