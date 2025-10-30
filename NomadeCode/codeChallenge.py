from playwright.sync_api import sync_playwright
import time #대기시간 생성
from bs4 import BeautifulSoup
import csv

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)

page = browser.new_page()

keywords = [
    "flutter",
    "nextjs",
    "kotlin"
]

for keyword in keywords:
    url = f"https://www.wanted.co.kr/search?query={keyword}&tab=position"
    print(url)
    page.goto(url)

    time.sleep(3)

    for x in range(5):
        page.keyboard.down("End")

    content = page.content()

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

    file = open(f"{keyword}.csv", "w")
    writer = csv.writer(file)
    writer.writerow(["Title","Company", "Link"])

    for job in jobs_db:
        writer.writerow(job.values())
    file.close()

p.stop()
