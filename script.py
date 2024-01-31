import requests
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service
from typing import List


options = EdgeOptions()
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=options)

driver.get("https://www.eventbrite.com/e/introduction-to-thai-yoga-massage-tickets-776225129257?aff=erelexpmlt&keep_tld=1")
time.sleep(4)

checkout_button = driver.find_element(By.XPATH, "/html/body/div/div/section/div[2]/button")

checkout_button.click()