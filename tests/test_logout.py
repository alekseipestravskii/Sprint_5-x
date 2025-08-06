from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from locators import Locators

class TestLogoutFromAccount:

    def login(self, driver, main_site):
        """Выполняет вход в личный кабинет."""
        driver.get(main_site)
        driver.find_element(*Locators.ACCOUNT_HEADER_LINK).click()
        
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        # Ждем, пока личный кабинет обновится
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ACCOUNT_HEADER_LINK))

    def test_logout_from_main_page_login_page(self, driver):
        """Тест: выход из аккаунта на главной странице после входа."""
        # Arrange
        main_site = "your_main_site_url_here"
        self.login(driver, main_site)

        # Act: выход из аккаунта
        driver.find_element(*Locators.ACCOUNT_HEADER_LINK).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ACCOUNT_LOGOUT_BUTTON))
        driver.find_element(*Locators.ACCOUNT_LOGOUT_BUTTON).click()

        # Assert: проверяем, что пользователь вышел
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        assert driver.current_url == "expected_account_login_url_here"
