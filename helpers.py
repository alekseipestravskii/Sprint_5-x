from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Credentials

def wait_and_fill_login_fields(driver):
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))

    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
