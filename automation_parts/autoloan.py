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
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_01_login(self):
        self.driver.get("http://dev.crystalone.ge/")
        self.driver.find_element(By.ID, 'details-button').click()
        self.driver.find_element(By.ID, 'proceed-link').click()
        time.sleep(5)
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
        # self.driver.find_element(By.XPATH, "/html/body/div[2]/header/nav/ul/li[2]/span/a/div").click()
        # self.driver.find_element(By.ID, "1").click()
        self.driver.get("https://dev.crystalone.ge/autoLoan")

    def test_03_consent_to_data(self):
        time.sleep(3)
        x = 15
        while x > 0:
            send_keys('{DOWN}')
            x -= 1
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/section/div/label/span[1]/input").click()

    def test_04_agree_button(self):
        self.driver.find_element(By.ID, "confirm-btn").click()
        time.sleep(2)

    def test_05_autoloan_application_section1(self):
        self.driver.find_element(By.ID, "amount").send_keys(random.randint(10000, 99999))
        time.sleep(1)
        autoduration = self.driver.find_element(By.ID, "duration")
        autoduration.click()
        autoduration.send_keys(Keys.ARROW_DOWN)
        autoduration.send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.ID, "pmt").send_keys(random.randint(1000, 9999))
        time.sleep(1)
        autopayment = self.driver.find_element(By.ID, "payment_day")
        autopayment.click()
        autopayment.send_keys("5")
        autopayment.send_keys(Keys.ENTER)
        time.sleep(1)
        autobranch = self.driver.find_element(By.ID, "branch")
        autobranch.click()
        autobranch.send_keys("5")
        autobranch.send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "შეძენა").click()

        # scrool
        self.driver.find_element(By.TAG_NAME, 'html').click()
        x = 10
        while x > 0:
            send_keys('{DOWN}')
            x -= 1
        time.sleep(2)

    def test_05_autoloan_application_section2(self):
        autocarbrand = self.driver.find_element(By.ID, "car_brand_id")
        autocarbrand.click()
        autocarbrand.send_keys(Keys.ENTER)
        time.sleep(1)
        autocarmodel = self.driver.find_element(By.ID, "car_model")
        autocarmodel.send_keys("ACHIKO")
        time.sleep(1)
        autocaryear = self.driver.find_element(By.ID, "car_year")
        autocaryear.click()
        autocaryear.send_keys(Keys.ENTER)
        time.sleep(1)
        autocarsteering = self.driver.find_element(By.ID, "car_steering_type_id")
        autocarsteering.click()
        autocarsteering.send_keys(Keys.ENTER)
        time.sleep(1)
        autocarfuel = self.driver.find_element(By.ID, "car_fuel_type_id")
        autocarfuel.click()
        autocarfuel.send_keys(Keys.ENTER)
        time.sleep(1)
        autolink = self.driver.find_element(By.ID, "car_url")
        autolink.send_keys("https://www.google.com/")
        time.sleep(1)

    def test_06_autoloan_images(self):
        firstimage = self.driver.find_element(By.XPATH,
                                              "/html/body/div[2]/div/div/section/form/section/div/div["
                                              "4]/div/div/div/div/div/div/div[1]/span/div/span/div")
        firstimage.click()
        time.sleep(2)
        pyautogui.typewrite("C:\\Users\\b"
                            ".bitarashvili"
                            "\\Desktop"
                            "\\default.jpg")
        pyautogui.press("enter")

        secondimage = self.driver.find_element(By.XPATH,
                                               "/html/body/div[2]/div/div/section/form/section/div/div["
                                               "4]/div/div/div/div/div/div/div[2]/span/div/span/div")
        secondimage.click()
        time.sleep(2)
        pyautogui.typewrite("C:\\Users\\b"
                            ".bitarashvili"
                            "\\Desktop"
                            "\\p.jpg")
        pyautogui.press("enter")

    def test_07_autoloan_submit_button(self):
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/section/form/section/div/div["
                                           "5]/div/div/div/div/button").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "modalOK").click()
