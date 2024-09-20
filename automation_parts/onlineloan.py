import json
import unittest
import time
import random

import pyautogui
from selenium.webdriver.support.ui import Select
from pywinauto.keyboard import send_keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec, wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


class TestWebsite(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_experimental_option("detach", True)

        # chromedriver_path = "C:/Users/b.bitarashvili/Downloads/chromedriver_win64/chromedriver.exe"
        chromedriver_path = "C:/Users/b.bitarashvili/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
        service = Service(chromedriver_path)
        cls.driver = webdriver.Chrome(service=service, options=options)

        # cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_01_login(self):
        self.driver.get("http://dev.crystalone.ge/")
        self.driver.find_element(By.ID, 'details-button').click()
        self.driver.find_element(By.ID, 'proceed-link').click()
        time.sleep(3)
        self.driver.find_element(By.TAG_NAME, 'html').click()
        i = 5
        while i > 0:
            send_keys('{DOWN}')
            i -= 1
        time.sleep(2)

        self.driver.find_element(By.ID, "username").send_keys("devtest3")
        self.driver.find_element(By.ID, "password").send_keys("QWEasd123")
        self.driver.find_element(By.ID, "login-btn").click()
        time.sleep(4)
        self.driver.find_element(By.ID, "otp-1").send_keys("0")
        self.driver.find_element(By.ID, "otp-2").send_keys("0")
        self.driver.find_element(By.ID, "otp-3").send_keys("0")
        self.driver.find_element(By.ID, "otp-4").send_keys("0")
        self.driver.find_element(By.ID, "requestCodeAgain").click()
        time.sleep(2)

    def test_02_autoloan_button(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/header/nav/ul/li[2]/span/a").click()
        self.driver.find_element(By.ID, "2").click()

    def test_03_request_loan(self):
        loan_amount = self.driver.find_element(By.ID, "amount")
        loan_amount.send_keys(random.randint(9999, 99999))
        time.sleep(1.5)
        loan_duration = self.driver.find_element(By.ID, "duration")
        loan_duration.click()
        loan_duration.send_keys(random.randint(12, 24))
        loan_duration.send_keys(Keys.ENTER)
        time.sleep(1.5)
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()
        time.sleep(3)

    def test_04_consent_to_data(self):
        time.sleep(3)
        x = 15
        while x > 0:
            send_keys('{DOWN}')
            x -= 1
        time.sleep(2)
        self.driver.find_element(By.ID, "isChecked").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "isChecked2").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "isChecked3").click()

    def test_05_agree_button(self):
        self.driver.find_element(By.ID, "confirm-btn").click()
        time.sleep(2)