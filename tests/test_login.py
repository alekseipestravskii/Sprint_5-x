from helper import wait_and_fill_login_fields

class TestLoginFromAnyPlaces:

    # Тестирование входа по кнопке "Войти в аккаунт" на главной странице
    def test_from_login_button_main_page_success(self, driver):
        driver.get(main_site)

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ACCOUNT_LOGIN_BUTTON))
        driver.find_element(*Locators.ACCOUNT_LOGIN_BUTTON).click()

        wait_and_fill_login_fields(driver)

        main_button_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BURGER_CONSTRUCTOR_BUTTON)).text
        assert main_button_text == 'Оформить заказ'
        assert driver.current_url == main_site

    # Тестирование входа через кнопку "Личный Кабинет"
    def test_from_account_header_link_main_page_success(self, driver):
        driver.get(main_site)

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ACCOUNT_HEADER_LINK))
        driver.find_element(*Locators.ACCOUNT_HEADER_LINK).click()

        wait_and_fill_login_fields(driver)

        main_button_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BURGER_CONSTRUCTOR_BUTTON)).text
        assert main_button_text == 'Оформить заказ'
        assert driver.current_url == main_site

    # Тестирование входа через кнопку в форме регистрации
    def test_from_registration_form_link_success(self, driver):
        driver.get(registration_url)

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REGISTER_LOGIN_LINK))
        driver.find_element(*Locators.REGISTER_LOGIN_LINK).click()

        wait_and_fill_login_fields(driver)

        main_button_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BURGER_CONSTRUCTOR_BUTTON)).text
        assert main_button_text == 'Оформить заказ'
        assert driver.current_url == main_site

    # Тестирование входа через кнопку в форме восстановления пароля
    def test_from_forgot_password_form_link_success(self, driver):
        driver.get(forgot_password_url)

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.FORGOT_PASSWORD_LOGIN_LINK))
        driver.find_element(*Locators.FORGOT_PASSWORD_LOGIN_LINK).click()

        wait_and_fill_login_fields(driver)

        main_button_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BURGER_CONSTRUCTOR_BUTTON)).text
        assert main_button_text == 'Оформить заказ'
        assert driver.current_url == main_site
