import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import threading
import keyboard

websites = {
    '1': 'https://www.ebay.com',
    '2': 'https://github.com',
    '3': 'https://www.twitch.tv',
    '4': 'https://id2.rtu.lv/'
}

wait = threading.Lock()

def open_site(site_key):
    with wait:
        url = websites[site_key]
        service = Service()
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)

        if site_key == '1':
            try:
                btn1 = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "user-agreement-banner-decline"))
                )
                driver.execute_script("arguments[0].scrollIntoView(true);", btn1) 
                driver.execute_script("arguments[0].click();", btn1)

            except Exception as e:
                print("Error1", e)

        if site_key == '3':
            try:
                btn3 = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-a-target="consent-banner-accept"]'))
                )
                driver.execute_script("arguments[0].click();", btn3)

                search = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-a-target="tw-input"]'))
                )
                search.send_keys("rostislav_999")
                search.send_keys(Keys.ENTER)
            except Exception as e:
                print("Error3", e)


        input()
        driver.quit()

for site_key in websites:
    keyboard.add_hotkey(site_key, lambda k=site_key: threading.Thread(target=open_site, args=(k,)).start())

print("1-Ebay\n2-Github\n3-Twitch\n4-Ortus\n\nEsc-end programm")
keyboard.wait('esc')