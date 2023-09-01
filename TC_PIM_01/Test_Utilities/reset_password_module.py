from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from Test_Data import credentials
from Test_Locators.reset_password_locators import LoginPageLocators


class Orangehrm:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.my_wait = WebDriverWait(self.driver, 10)
        self.locators = LoginPageLocators
        self.url = credentials.url
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(5)



    def reset_password(self):
        """
        1. click on forgot password link
        2. provide username
        3. click on reset password
        :return: link text
        """
        forget_password_webelement = self.my_wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.forgot_password_xpath)))
        forget_password_webelement.click()

        username_webelement = self.my_wait.until(
            EC.visibility_of_element_located((By.NAME, self.locators.username_locator_name_tag)))
        username_webelement.send_keys(credentials.username)

        reset_password_webelement = self.my_wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.reset_password_xpath)))
        reset_password_webelement.click()

        reset_text_webelement = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.reset_text_xpath)))
        text1 = reset_text_webelement.text
        return text1

obj = Orangehrm()
obj.reset_password()