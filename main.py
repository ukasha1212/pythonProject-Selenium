import asyncore
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from shutil import copyfile


def capture_screenshot(webdriver, file_path):
    try:
        screenShot = webdriver.get_screenshot_as_file(file_path)
        print("Screenshot saved successfully")
    except Exception as e:
        print("error occured wihile taking screenshot", str(e))


def login_via_email(username, password):
    global driver
    try:
        # creating new instance of Chrome Web Driver
        driver = webdriver.Chrome()

        # Sending URL to open 'Jibb.ai' webpage.
        driver.get("https://app.jibb.ai/login")

        # printing title of our driver to confirm that we reached the requested page.

        print(driver.title)

        # Assigning the web element from webpage to local Web-element
        user_name = driver.find_element(By.ID, "username")
        pass_word = driver.find_element(By.ID, "password")
        xpath_expression = "//button[contains(@class, 'oval-but') and text()='LOGIN']"
        user_name.send_keys(username)
        pass_word.send_keys(password)
        submit_button = driver.find_element(By.XPATH, xpath_expression)
        submit_button.click()
        # waiting here for 30 seconds for elements and page to be loaded before we assign the element.
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//strong[text()='my space 2']")))

        # Click on the element
        element.click()
        print(driver.title)
        time.sleep(20)
        # Perform additional actions or close the browser as needed
        print(driver.current_url)

    except Exception as e:
        capture_screenshot(driver, "error_screenshot.png")
        print("Error occurred:", str(e))
    driver.quit()


username = "ahmed.ukasha@jibb.ai"
password = "workOmania@1212"
login_via_email(username, password)
