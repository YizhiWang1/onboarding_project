from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json

# load username and password
with open("basic_config.json", "r") as f:
    creds = json.load(f)

USERNAME = creds["username"]
PASSWORD = creds["password"]

# start the browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://classic.liveauctioneers.com/auctioneers/post.html")

time.sleep(1)

# fill in the login
driver.find_element(By.ID,"uname").send_keys(USERNAME)
driver.find_element(By.ID, "passcode").send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, "input[value='SIGN IN']").click()

time.sleep(1)
print("Login Successful")

# cut-off time of scraping

cutoff = datetime.strptime("2025-03-13", "%Y-%m-%d")

data = []

# scrape items
driver.find_element(By.LINK_TEXT, "Post Auction").click()
stop = False # flag of either to stop or continue scraping

for page_num in range(1, 6):
    if stop:
        break
    time.sleep(1)
    
    driver.get(f"https://classic.liveauctioneers.com/auctioneers/post.html?pagenum={page_num}")

    print(f"Scraping page {page_num}")
    items = driver.find_elements(By.CSS_SELECTOR, "table.sortable tbody tr")

    for item in items:
        cells = item.find_elements(By.TAG_NAME, "td")
        date = cells[0].text.strip()
        raw_date = datetime.strptime(date, "%Y-%m-%d %I:%M%p")

        if raw_date <= cutoff:
            stop = True
            print ("Reached date of cutoff")
            break   

        record = {
            "date": cells[0].text.strip(),
            "auction title": cells[1].text.strip(),
            "timed": cells[2].text.strip(),
            "items": cells[3].text.strip(),
            "bids": cells[4].text.strip(),
            "bidders": cells[5].text.strip(),
            "sold": cells[6].text.strip()
        }
        data.append(record)


with open("post_auctions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)


driver.quit()
