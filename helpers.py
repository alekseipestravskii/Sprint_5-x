from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Credentials

def wait_and_fill_login_fields(driver):
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))

    driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

class RegistrationHelper:
    def __init__(self, driver):
        self.driver = driver

    def register_user(self, name, email, password, registration_url):
        self.driver.get(registration_url)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(Locators.REGISTER_BUTTON))

        self.driver.find_element(*Locators.REG_NAME).send_keys(name)
        self.driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        self.driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        self.driver.find_element(*Locators.REGISTER_BUTTON).click()
