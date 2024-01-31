import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service

def find_and_click_checkout_button(driver):
    try:
        iframe = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[data-automation*='checkout-widget-iframe']"))
        )
        driver.switch_to.frame(iframe)
        checkout_button = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-automation='eds-modal__primary-button']"))
        )
        checkout_button.click()
        return True
    except TimeoutException:
        return False
    finally:
        driver.switch_to.default_content()

options = EdgeOptions()
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=options)

event_url = "https://www.eventbrite.com/e/5-week-wheel-course-session-2-630-8-tickets-813283712477"
driver.get(event_url)

# Set your target time just before 11:30
target_time = datetime.now().replace(hour=10, minute=51, second=00, microsecond=500000)

while True:
    current_time = datetime.now()
    if current_time >= target_time:
        if find_and_click_checkout_button(driver):
            break  # Exit the loop if the button is found and clicked
        driver.refresh()
        time.sleep(0.5)  # Adjust the sleep time as necessary

# Keep the browser window open
time.sleep(6000)
