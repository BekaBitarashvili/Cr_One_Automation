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

        self.driver.find_element(By.ID, "username").send_keys("testSaxeli13")
        self.driver.find_element(By.ID, "password").send_keys("Zvikilo13!")
        self.driver.find_element(By.ID, "login-btn").click()
        time.sleep(4)
        self.driver.find_element(By.ID, "otp-1").send_keys("1")
        self.driver.find_element(By.ID, "otp-2").send_keys("1")
        self.driver.find_element(By.ID, "otp-3").send_keys("1")
        self.driver.find_element(By.ID, "otp-4").send_keys("1")
        time.sleep(2)

    def test_02_statements_page(self):
        self.driver.find_element(By.XPATH, "/html/body/div/header/nav/ul/li[3]/span/a").click()
        time.sleep(10)

    def test_03_check_status(self):
        check_status = self.driver.find_element(By.XPATH, "/html/body/div/div/div/section/div[1]/div[1]/div[4]/h4")
        assert check_status.text == "Confirmed", f"Expected: Confirmed, but got: {check_status.text}"
        print(f"{check_status.text} is correct")
        time.sleep(2)

    def test_04_check_date(self):
        sched_date = self.driver.find_element(By.XPATH, "/html/body/div/div/div/section/div[1]/div["
                                                        "2]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]")
        actual_date = self.driver.find_element(By.XPATH, "//html/body/div/div/div/section/div[1]/div[1]/div[5]/h4")
        assert sched_date.text == actual_date.text
        print(f"{sched_date.text} {actual_date.text} is correct")

    def test_05_schedule_pagination(self):
        pag_button = self.driver.find_element(By.XPATH,
                                              "/html/body/div/div/div/section/div[1]/div[2]/div/div/div/ul/li["
                                              "5]/button")
        if pag_button.is_enabled():
            for _ in range(3):
                pag_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div/section/div[1]/div["
                                                                "2]/div/div/div/ul/li[""5]/button")
                pag_button.click()
                time.sleep(3)
