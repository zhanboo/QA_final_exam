from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def run_login_test(username_input, password_input):
    # Launch a new Chrome browser window
    driver = webdriver.Chrome()

    # Go to the login page
    driver.get("https://letsusedata.com/index.html")
    time.sleep(5)  # Let the page load

    # Enter username and password using correct field IDs
    driver.find_element(By.ID, "txtUser").send_keys(username_input)
    driver.find_element(By.ID, "txtPassword").send_keys(password_input + Keys.RETURN)

    time.sleep(3)  # Wait for the result page to load

    # Check the current URL or page content to determine success
    current_url = driver.current_url.lower()

    if "dashboard" in current_url or "account" in current_url:
        print(f"✅ SUCCESS: Login worked for {username_input}")
    else:
        print(f"❌ FAIL: Login failed for {username_input}")

    # Keep the browser open briefly before closing
    time.sleep(3)
    driver.quit()

# Test case 1 – Correct credentials
run_login_test("test1", "Test12456")

# Test case 2 – Incorrect password
run_login_test("test1", "test1234")
