import requests
from bs4 import BeautifulSoup

all_jobs = []


def scrape_page(url):
    # print(response.content)

    print("fScraping {url}...")

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    jobs = soup.find("section",
                     class_="jobs").find_all("li")[1:-1]

    for job in jobs:
        title = job.find("span", class_="title").text
        company, position, region
        _ = job.find_all("span", class_="company")
        url = job.find("div", class_="tooltip").next_sibling["href"]
        # if url:
        #    url = url["href"]
        # company = company.text
        # position = position.text
        # region = region.text
        # print(title, company, position, region, sep="------\n")
        job_data = {
            "title": title,
            "company": company.text,
            "position": position.text,
            "region": region.text,
            "url": f"https://weworkremotely.com:{url}"
        }

        all_jobs.append(job_data)

def get_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return len(soup.find("div", class_="buttons").find_all("span", class_="page"))

total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")

for x in range(total_pages):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    scrape_page(url)

print(len(all_jobs))


# 사이트 차단시 브라우저에서 요청을 보낸 것처럼 처리
keyword = [
    "flutter",
    "python",
    "golang"
]

r = requests.get(
    "https://remoteok.com/",
    headers={
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
        }
    )

print(r.status_code)
