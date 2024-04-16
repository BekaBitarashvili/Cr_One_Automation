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


class TestRestore(unittest.TestCase):
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

    def test_01_restore_data_button(self):
        self.driver.get("http://10.117.27.38:8090")
        time.sleep(3)
        self.driver.find_element(By.TAG_NAME, 'html').click()
        i = 5
        while i > 0:
            send_keys('{DOWN}')
            i -= 1
        time.sleep(2)

        restore_click = WebDriverWait(self.driver, 3).until(
            ec.presence_of_element_located((By.XPATH, "/html/body/div/div/div/section/div[2]/form/div/a")))
        restore_click.click()
        assert self.driver.find_element(By.XPATH, "/html/body/div/div/div/section/form/h1").get_attribute(
            "innerText") == "Data Recovery" or "მონაცემების აღდგენა"

    def test_02_check_button(self):
        restoring_button = self.driver.find_element(By.ID, "restoreBtn")
        assert restoring_button.is_enabled() == False, "ღილაკი გაააქტიურებულია!"

    def test_03_check_inputs(self):
        inputs = self.driver.find_elements(By.TAG_NAME, "input")
        for inp in inputs:
            assert inp.get_attribute("value") == "", "ველები არ არის ცარიელი!"

    def test_04_fill_inputs_correct_data(self):
        x = 6
        while x > 0:
            send_keys('{DOWN}')
            x -= 1
        personal_num = self.driver.find_elements(By.ID, "personal_id")
        personal_num[0].send_keys("18001021014")
        mob_num = self.driver.find_elements(By.ID, "phone")
        mob_num[0].send_keys("577121157")
        assert self.driver.find_element(By.ID, "restoreBtn").is_enabled() == True, "ღილაკი არ გააქტიურებულა!"
        restoring_button = self.driver.find_element(By.ID, "restoreBtn")
        restoring_button.click()
        time.sleep(2)

    def test_05_type_6digit_code(self):
        self.driver.find_element(By.TAG_NAME, "body").click()
        x = 6
        while x > 0:
            send_keys('{DOWN}')
            x -= 1
        time.sleep(3)
        self.driver.find_element(By.ID, "otp-1").send_keys("0")
        self.driver.find_element(By.ID, "otp-2").send_keys("0")
        self.driver.find_element(By.ID, "otp-3").send_keys("0")
        self.driver.find_element(By.ID, "otp-4").send_keys("0")
        self.driver.find_element(By.ID, "otp-5").send_keys("0")
        self.driver.find_element(By.ID, "otp-6").send_keys("0")
        time.sleep(3)
        request_code = self.driver.find_element(By.ID, "requestCodeAgain")
        request_code.click()
        time.sleep(3)

    def test_06_new_password(self):
        self.driver.find_element(By.TAG_NAME, "body").click()
        x = 4
        while x > 0:
            send_keys('{UP}')
            x -= 1
        first_pass = self.driver.find_element(By.ID, "newPassword")
        first_pass.send_keys("123123123G")
        time.sleep(2)
        second_pass = self.driver.find_element(By.ID, "repeatPassword")
        second_pass.send_keys("123123123G")
        time.sleep(4)
