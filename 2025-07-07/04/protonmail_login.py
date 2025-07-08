from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_protonmail(username, password):
    # Start Chrome (you can also use Firefox etc.)
    driver = webdriver.Chrome()  # Make sure chromedriver is in PATH

    try:
        driver.get("https://account.proton.me/login")
        
        # Wait until the username field is present
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        
        # Fill in username
        user_input = driver.find_element(By.ID, "username")
        user_input.send_keys(username)
        
        # Click 'Next' button to go to password step
        next_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        next_button.click()

        # Wait until password field is present
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        
        # Fill in password
        pass_input = driver.find_element(By.ID, "password")
        pass_input.send_keys(password)
        
        # Click login
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # Wait until inbox loads (or another element specific to logged-in state)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.sidebar"))
        )
        
        print("Login successful! Navigated to ProtonMail.")

        # Example: stay logged in for 10 seconds so you can see
        time.sleep(10)

    except Exception as e:
        print("Something went wrong:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    # Replace with your test credentials (DO NOT use your real account)
    login_protonmail("your_test_username", "your_test_password")