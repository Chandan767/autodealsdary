import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome()
    driver.get("https://demo.dealsdray.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_function_testing(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    user = driver.find_element(By.XPATH, "//input[@id='mui-1']")
    user.clear()
    user.send_keys("prexo.mis@dealsdray.com")

    passw = driver.find_element(By.XPATH, "//input[@id='mui-2']")
    passw.clear()
    passw.send_keys("prexo.mis@dealsdray.com")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

    assert 'dashboard' in driver.current_url, "Login unsuccessful or not on the dashboard"
    print("Successfully logged in and on the dashboard")

    order = driver.find_element(By.XPATH, '//span[text()="Order"]')
    order.click()
    orders = driver.find_element(By.XPATH, '//span[text()="Orders"]')
    orders.click()

    bulk_or = driver.find_element(By.XPATH, '//button[text()="Add Bulk Orders"]')
    bulk_or.click()
    time.sleep(2)

    ch_fil = driver.find_element(By.XPATH, '//input[@type="file"]')
    ch_fil.send_keys("C:\\Users\\LENOVIO\\Desktop\\demo-data.xlsx")
    time.sleep(2)

    imp_file = driver.find_element(By.XPATH, '//button[text()="Import"]')
    imp_file.click()
    time.sleep(2)

    validate_data = driver.find_element(By.XPATH, '//button[text()="Validate Data"]')
    validate_data.click()
    time.sleep(2)
    alert = Alert(driver)
    alert.accept()
    driver.get_screenshot_as_file("full_screen.png")
    #screenshot_path = f"../Screenshots/{screenshot_name}"
    #driver.save_screenshot("full screen")
    print("Test completed successfully")

