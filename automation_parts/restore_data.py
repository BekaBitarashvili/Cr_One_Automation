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

    def test_04_fill_inputs_incorrect_data(self):
        personal_num = self.driver.find_elements(By.XPATH, "/html/body/div/div/div/section/form/div/div["
                                                           "1]/div/div/div/div/span/input")
        personal_num[0].send_keys("11111111111")
        mob_num = self.driver.find_elements(By.XPATH, "/html/body/div/div/div/section/form/div/div["
                                                      "2]/div/div/div/div/span/input")
        mob_num[0].send_keys("555555555")
        assert self.driver.find_element(By.ID, "restoreBtn").is_enabled() == True, "ღილაკი არ გააქტიურებულა!"
        restoring_button = self.driver.find_element(By.ID, "restoreBtn")
        restoring_button.click()
        assert (self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/span/div/div/div").get_attribute(
            "innerText") == "The specified phone number does not match the number specified in the system." or
                "მითითებული ტელეფონის ნომერი არ ემთხვევა სისტემაში მითითებულ ნომერს.")

    def test_05_fill_inputs_correct_personal(self):
        pass

    def test_06_fill_inputs_correct_mobile(self):
        pass

    def test_07_fill_inputs_correct_data(self):
        pass
