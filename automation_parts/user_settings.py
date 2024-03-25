import json
import unittest
import time
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
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


class TestSettings(unittest.TestCase):
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
        self.driver.get("http://10.117.27.38:8090")
        time.sleep(3)
        self.driver.find_element(By.TAG_NAME, 'html').click()
        i = 5
        while i > 0:
            send_keys('{DOWN}')
            i -= 1
        time.sleep(2)

        self.driver.find_element(By.ID, "username").send_keys("testOnline")
        self.driver.find_element(By.ID, "password").send_keys("Zvikilo13!")
        self.driver.find_element(By.ID, "login-btn").click()
        time.sleep(4)
        self.driver.find_element(By.ID, "otp-1").send_keys("1")
        self.driver.find_element(By.ID, "otp-2").send_keys("1")
        self.driver.find_element(By.ID, "otp-3").send_keys("1")
        self.driver.find_element(By.ID, "otp-4").send_keys("1")
        time.sleep(2)

    def test_02_settings(self):
        time.sleep(2)
        self.driver.find_element(By.ID, "avatar-menu-btn").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "setting").click()
        time.sleep(2)

    def test_03_my_profile_section(self):
        self.driver.find_element(By.TAG_NAME, 'html').click()
        i = 12
        while i > 0:
            send_keys('{DOWN}')
            i -= 1
        time.sleep(2)
        z = 0
        while z < 12:
            send_keys('{UP}')
            z += 1
        time.sleep(2)

    def test_04_password_section(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/section/div[2]/div[1]/div[1]/div/div[2]").click()
        time.sleep(2)
        # self.driver.find_element(By.TAG_NAME, 'html').click()
        i = 12
        while i > 0:
            send_keys('{DOWN}')
            i -= 1
        time.sleep(2)
        z = 0
        while z < 12:
            send_keys('{UP}')
            z += 1
        time.sleep(2)

    def test_05_history_section(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/section/div[2]/div[1]/div[1]/div/div[3]").click()
        time.sleep(2)
        self.driver.find_element(By.TAG_NAME, 'html').click()
        i = 11
        while i > 0:
            send_keys('{DOWN}')
            i -= 1
        time.sleep(2)

        z = 0
        while z < 15:
            send_keys('{UP}')
            z += 1
        time.sleep(2)

    def test_06_change_photo(self):
        time.sleep(3)
        upload_button = self.driver.find_element(By.XPATH,
                                                 "/html/body/div/div/div/section/div[1]/span/div[1]/span/button")
        upload_button.click()

        time.sleep(2)

        pyautogui.typewrite("Desktop\\default.jpg")
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(2)

        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]").click()
        time.sleep(5)

    def test_07_logout(self):
        self.driver.find_element(By.ID, "avatar-menu-btn").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "log-out").click()
        time.sleep(2)
