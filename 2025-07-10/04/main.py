from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Open the webpage
    driver.get("https://svencionys.lt/apklausa/")

    # Wait for the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Scroll down (slowly)
    for _ in range(3):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

    # Example: click a button (replace with actual button selector)
    try:
        button = driver.find_element(By.CSS_SELECTOR, "button")
        button.click()
        print("Button clicked!")
    except Exception as e:
        print("Button not found or click failed:", e)



    # Example: fill out a form field (replace 'input[name=\"name\"]' with actual selector)
    try:
        input_field = driver.find_element(By.CSS_SELECTOR, "input[name='name']")
        input_field.send_keys("John Doe")

        submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        submit_button.click()
        print("Form submitted!")
    except Exception as e:
        print("Form fields not found or fill failed:", e)

    # Wait to see the result
    time.sleep(5)

finally:
    driver.quit()

