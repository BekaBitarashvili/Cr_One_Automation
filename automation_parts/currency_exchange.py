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


class TestCurrency(unittest.TestCase):
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

    def test_01_login(self):
        self.driver.get("https://dev.crystalone.ge/")
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
        otp_button = WebDriverWait(self.driver, 3).until(
            ec.element_to_be_clickable((By.ID, "requestCodeAgain"))
        )
        otp_button.click()

    def test_02_currency(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/ul/li[4]/span/a").click()
        time.sleep(8)
        self.driver.find_element(By.TAG_NAME, 'html').click()
        i = 13
        while i > 0:
            send_keys('{DOWN}')
            i -= 1
        time.sleep(2)
        x = 13
        while x > 0:
            send_keys('{UP}')
            x -= 1
        time.sleep(2)

    def test_03_gel_to_usd(self):
        exch1_input = self.driver.find_element(By.ID, "InputBuyField")
        exch1_input.click()
        exch1_input.send_keys("100")
        time.sleep(5)
        self.driver.find_element(By.ID, "reversBtn").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "reversBtn").click()
        time.sleep(3)

    def test_04_eur_to_usd(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/section/div[1]/form/div/div[2]/div["
                                           "1]/div/div/div/div/div/div/div/div/div/div/div").click()
        time.sleep(3)
        for _ in range(2):
            send_keys('{UP}')
        time.sleep(2)
        send_keys('{ENTER}')
        time.sleep(5)
        self.driver.find_element(By.ID, "reversBtn").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "reversBtn").click()
        time.sleep(3)

    def test_05_different_value(self):
        exch2_input = self.driver.find_element(By.ID, "InputBuyField")
        for _ in range(3):
            exch2_input.send_keys(Keys.BACKSPACE)
        time.sleep(3)
        exch2_input.send_keys("5000")
        time.sleep(5)
        self.driver.find_element(By.ID, "reversBtn").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "reversBtn").click()
        time.sleep(3)