from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # 크롬 창 표시 (headless=True면 숨김) - 브라우저를 생성하기는 하지만 눈에 보이지 않는 상태
    page = browser.new_page()
    page.goto("https://google.com")

    page.screenshot(path="screenshot.png")
