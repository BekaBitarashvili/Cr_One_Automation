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


class TestProducts(unittest.TestCase):
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

    def test_02_loans(self):
        time.sleep(3)
        self.driver.get("http://10.117.27.38:8090/loans")
        time.sleep(5)
        i = 5
        while i > 0:
            send_keys('{DOWN}')
            i -= 1
        time.sleep(2)
        loan_button = self.driver.find_element(By.CSS_SELECTOR, "body > div > div > div > section > div.my-\["
                                                                "12px\].bg-white.lg\:bg-gray.dark\:bg-gray\/\["
                                                                "\.06\].\[\&\>\*\]\:text-black.\["
                                                                "\&\>\*\]\:dark\:text-white.rounded-md.lg\:rounded-xl"
                                                                ".text-left.transition.ease-in-out.delay-150.shadow"
                                                                "-10.cursor-pointer.transition-transform > div")
        loan_button.click()
        time.sleep(2)
        x = 7
        while x > 0:
            send_keys('{DOWN}')
            x -= 1
        time.sleep(2)

    def test_03_agreement_buttons(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/section/div[2]/div[2]/div[3]/button[1]").click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/section/div[2]/div[2]/div[3]/button[2]").click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/section/div[2]/div[2]/div[3]/button[3]").click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])

    def test_04_change_loan_name(self):
        x = 7
        while x > 0:
            send_keys('{UP}')
            x -= 1
        time.sleep(2)

        self.driver.find_element(By.XPATH, "/html/body/div/div/div/section/div[2]/div[1]/div[1]/div[2]/div").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "nameOfTheLoan").send_keys("შეცვლილი სახელი")
        time.sleep(2)
        self.driver.find_element(By.ID, "modalOK").click()
        time.sleep(2)