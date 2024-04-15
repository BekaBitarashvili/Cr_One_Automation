import json
import unittest
import time

from selenium.webdriver.support.ui import Select
from pywinauto.keyboard import send_keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec, wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


class TestAuth(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_experimental_option("detach", True)

        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_01_incorrect_user_and_pass(self):
        self.driver.get("http://10.117.27.38:8090")
        time.sleep(3)
        self.driver.find_element(By.TAG_NAME, 'html').click()
        i = 5
        while i > 0:
            send_keys('{DOWN}')
            i -= 1
        time.sleep(2)

        username_field = WebDriverWait(self.driver, 3).until(
            ec.presence_of_element_located((By.ID, "username"))
        )
        username_field.send_keys("ARASWORI_USERNAME_DA_PASS")
        time.sleep(5)
        password_field = WebDriverWait(self.driver, 3).until(
            ec.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys("ARASWORI123")

        show_password = WebDriverWait(self.driver, 3).until(
            ec.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/section/div[2]/form/div/div[2]/div/div/div["
                                                  "1]/div/span/span[2]"))
        )
        show_password.click()
        time.sleep(3)
        login_button = WebDriverWait(self.driver, 3).until(
            ec.element_to_be_clickable((By.ID, "login-btn"))
        )
        login_button.click()
        time.sleep(3)

    def test_02_correct_user_and_incorrect_pass(self):
        self.driver.find_element(By.TAG_NAME, 'html').click()
        i = 5
        while i > 0:
            send_keys('{DOWN}')
            i -= 1
        time.sleep(2)

        elemento_to_triple_click = self.driver.find_element(By.ID, "username")

        actions = ActionChains(self.driver)
        actions.click(elemento_to_triple_click).click(elemento_to_triple_click).click(
            elemento_to_triple_click).perform()
        time.sleep(1.5)

        username_field = WebDriverWait(self.driver, 3).until(
            ec.presence_of_element_located((By.ID, "username"))
        )
        username_field.send_keys("testAkido")
        time.sleep(4)


        elemento_to_triple_click = self.driver.find_element(By.ID, "password")
        actions.click(elemento_to_triple_click).click(elemento_to_triple_click).click(
            elemento_to_triple_click).perform()
        time.sleep(1.5)
        password_field = WebDriverWait(self.driver, 3).until(
            ec.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys("ARASWORI789")

        time.sleep(5)
        login_button = WebDriverWait(self.driver, 3).until(
            ec.element_to_be_clickable((By.ID, "login-btn"))
        )
        login_button.click()
        status_code = self.driver.execute_script(
            """
        var entries = window.performance.getEntries();
        if (entries.length > 0 && entries[0].response) {
            return entries[0].response.status;
        } else {
            return null;
        }
        """
        )
        if status_code == 200:
            print(f'ავტორიზაცია განხორციელდა წარმატებით, სტატუსია: {status_code}')
        else:
            print(f'მომხმარებელმა ვერ გაიარა ავტორიზაცია, სტატუსია: {status_code}')
        time.sleep(3)

    def test_03_incorrect_user_and_correct_pass(self):
        self.driver.find_element(By.TAG_NAME, 'html').click()
        i = 5
        while i > 0:
            send_keys('{DOWN}')
            i -= 1
        time.sleep(2)

        elemento_to_triple_click = self.driver.find_element(By.ID, "username")

        actions = ActionChains(self.driver)
        actions.click(elemento_to_triple_click).click(elemento_to_triple_click).click(
            elemento_to_triple_click).perform()
        time.sleep(1.5)

        username_field = WebDriverWait(self.driver, 3).until(
            ec.presence_of_element_located((By.ID, "username"))
        )
        username_field.send_keys("ISEVARASWORI")
        time.sleep(4)

        elemento_to_triple_click = self.driver.find_element(By.ID, "password")
        actions.click(elemento_to_triple_click).click(elemento_to_triple_click).click(
            elemento_to_triple_click).perform()
        time.sleep(1.5)
        password_field = WebDriverWait(self.driver, 3).until(
            ec.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys("datoToda123!@#")

        time.sleep(5)
        login_button = WebDriverWait(self.driver, 3).until(
            ec.element_to_be_clickable((By.ID, "login-btn"))
        )
        login_button.click()
        status_code = self.driver.execute_script(
            """
        var entries = window.performance.getEntries();
        if (entries.length > 0 && entries[0].response) {
            return entries[0].response.status;
        } else {
            return null;
        }
        """
        )
        if status_code == 200:
            print(f'ავტორიზაცია განხორციელდა წარმატებით, სტატუსია: {status_code}')
        else:
            print(f'მომხმარებელმა ვერ გაიარა ავტორიზაცია, სტატუსია: {status_code}')
        time.sleep(3)

    def test_04_only_pass(self):
        self.driver.find_element(By.TAG_NAME, 'html').click()
        i = 5
        while i > 0:
            send_keys('{DOWN}')
            i -= 1
        time.sleep(2)

        elemento_to_triple_click = self.driver.find_element(By.ID, "username")

        actions = ActionChains(self.driver)
        actions.click(elemento_to_triple_click).click(elemento_to_triple_click).click(
            elemento_to_triple_click).perform()
        time.sleep(1.5)
        send_keys('{DELETE}')
        time.sleep(1.5)
        elemento_to_triple_click = self.driver.find_element(By.ID, "password")

        actions = ActionChains(self.driver)
        actions.click(elemento_to_triple_click).click(elemento_to_triple_click).click(
            elemento_to_triple_click).perform()
        time.sleep(1.5)
        send_keys('{DELETE}')

        password_field = WebDriverWait(self.driver, 3).until(
            ec.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys("MXOLODPAROLI")
        print("Username ცარიელია, უნდა შეივსოს სავალდებულოდ")
        time.sleep(3)

    def test_05_correct_user_and_pass(self):
        elemento_to_triple_click = self.driver.find_element(By.ID, "username")

        actions = ActionChains(self.driver)
        actions.click(elemento_to_triple_click).click(elemento_to_triple_click).click(
            elemento_to_triple_click).perform()
        time.sleep(1.5)
        send_keys('{DELETE}')
        time.sleep(1.5)

        elemento_to_triple_click = self.driver.find_element(By.ID, "password")

        actions = ActionChains(self.driver)
        actions.click(elemento_to_triple_click).click(elemento_to_triple_click).click(
            elemento_to_triple_click).perform()
        time.sleep(1.5)
        send_keys('{DELETE}')

        username_field = WebDriverWait(self.driver, 3).until(
            ec.presence_of_element_located((By.ID, "username"))
        )
        username_field.send_keys("testOnline")
        time.sleep(5)
        password_field = WebDriverWait(self.driver, 3).until(
            ec.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys("Zvikilo13!")
        time.sleep(4)

        login_button = WebDriverWait(self.driver, 3).until(
            ec.element_to_be_clickable((By.ID, "login-btn"))
        )
        login_button.click()
        # OTP LOGIC
        time.sleep(3)
        self.driver.find_element(By.ID, "otp-1").send_keys("0")
        self.driver.find_element(By.ID, "otp-2").send_keys("0")
        self.driver.find_element(By.ID, "otp-3").send_keys("0")
        self.driver.find_element(By.ID, "otp-4").send_keys("0")
        time.sleep(2)

        otp_button = WebDriverWait(self.driver, 3).until(
            ec.element_to_be_clickable((By.ID, "login-btn"))
        )
        otp_button.click()
        time.sleep(3)


# import urllib.request
# import urllib.request
# import urllib.error
#
# try:
#     with urllib.request.urlopen('http://10.117.27.38:8090/') as f:
#         print(f.read())
#         print(f.status)
#         print(f.getheader("content-length"))
# except urllib.error.URLError as e:
#     print(e.reason)
