import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service

options = EdgeOptions()
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=options)

event_url = "https://www.eventbrite.com/e/introduction-to-project-management-tickets-55968945623?aff=erelexpmlt&keep_tld=1"
driver.get(event_url)
time.sleep(4)  # Wait for the page to load

try:
    # Locate the iframe by a partial match of its 'data-automation' attribute
    iframe = driver.find_element(By.CSS_SELECTOR, "iframe[data-automation*='checkout-widget-iframe']")
    driver.switch_to.frame(iframe)

    # Update the selector for the checkout button based on a more consistent attribute
    checkout_button = driver.find_element(By.CSS_SELECTOR, "button[data-automation='eds-modal__primary-button']")
    checkout_button.click()

    time.sleep(1300)  # Wait to manually complete the process

except Exception as e:
    print(f"Error: {e}")

# Keep the browser window open for manual completion of the process
