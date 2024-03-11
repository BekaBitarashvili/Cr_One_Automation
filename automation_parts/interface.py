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

    def test_01_crystal_logo(self):
        self.driver.get("http://10.117.27.38:8090")
        time.sleep(2)
        self.driver.find_element(By.TAG_NAME, "html").click()

        i = 1
        while i > 0:
            send_keys('{DOWN}')
            i -= 1
        time.sleep(2)

        username_field = WebDriverWait(self.driver, 3).until(
            ec.presence_of_element_located((By.ID, "username"))
        )
        username_field.send_keys("vtestavtLOGOS")
        password_field = WebDriverWait(self.driver, 3).until(
            ec.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys("CLICKIlogoze")
        show_password = WebDriverWait(self.driver, 3).until(
            ec.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/section/div[2]/form/div/div[2]/div/div/div["
                                                  "1]/div/span/span[2]"))
        )
        show_password.click()
        time.sleep(2)
        crystal_logo = self.driver.find_element(By.XPATH, "/html/body/div/header/div/div[2]/a/div/img")
        crystal_logo.click()
        check_username = self.driver.find_element(By.ID, "username")
        assert check_username.get_attribute("value") == "", "სახელის ველი არ გასუფთავდა!"
        check_password = self.driver.find_element(By.ID, "password")
        assert check_password.get_attribute("value") == "", "პაროლის ველი არ გასუფთავდა!"
        time.sleep(3)

    def test_02_dark_mode(self):
        username_field = WebDriverWait(self.driver, 3).until(
            ec.presence_of_element_located((By.ID, "username"))
        )
        username_field.send_keys("DARKMODE")
        password_field = WebDriverWait(self.driver, 3).until(
            ec.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys("rchebaSHEVSEBULI")
        show_password = WebDriverWait(self.driver, 3).until(
            ec.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/section/div[2]/form/div/div[2]/div/div/div["
                                                  "1]/div/span/span[2]"))
        )
        show_password.click()

        mode_change = self.driver.find_element(By.XPATH, "/html/body/div/header/div/div[3]/button")
        mode_change.click()
        time.sleep(3)
        mode_change.click()
        time.sleep(3)
        assert self.driver.find_element(By.ID, "username").get_attribute("value") == "DARKMODE", "ტექსტი წაიშალა!"
        assert self.driver.find_element(By.ID, "password").get_attribute("value") == "rchebaSHEVSEBULI", ("ტექსტი "
                                                                                                          "წაიშალა!")

    def test_03_about(self):
        about = self.driver.find_element(By.XPATH, "/html/body/div/footer/div/div[1]/nav/a[1]")
        about.click()
        time.sleep(3)
        i = 10
        while i > 0:
            send_keys('{DOWN}')
            i -= 1
        time.sleep(2)
        x = 10
        while x > 0:
            send_keys('{UP}')
            x -= 1
        time.sleep(2)
        self.driver.back()
        z = 11
        while z > 0:
            send_keys('{UP}')
            z -= 1

    def test_04_address(self):
        address = self.driver.find_element(By.XPATH, "/html/body/div/footer/div/div[1]/nav/a[2]")
        address.click()
        time.sleep(3)
        i = 10
        while i > 0:
            send_keys('{DOWN}')
            i -= 1
        time.sleep(2)
        x = 10
        while x > 0:
            send_keys('{UP}')
            x -= 1
        time.sleep(2)
        self.driver.back()
        z = 11
        while z > 0:
            send_keys('{UP}')
            z -= 1

    def test_05_faq(self):
        faq = self.driver.find_element(By.XPATH, "/html/body/div/footer/div/div[1]/nav/a[3]")
        faq.click()
        time.sleep(3)
        i = 10
        while i > 0:
            send_keys('{DOWN}')
            i -= 1
        time.sleep(2)
        x = 10
        while x > 0:
            send_keys('{UP}')
            x -= 1
        time.sleep(2)
        self.driver.back()
        z = 11
        while z > 0:
            send_keys('{UP}')
            z -= 1

    def test_06_facebook(self):
        facebook = self.driver.find_element(By.XPATH, "/html/body/div/footer/div/div[2]/div[1]/a[1]")
        facebook.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def test_07_youtube(self):
        youtube = self.driver.find_element(By.XPATH, "/html/body/div/footer/div/div[2]/div[1]/a[2]")
        youtube.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def test_08_linkedin(self):
        linkedin = self.driver.find_element(By.XPATH, "/html/body/div/footer/div/div[2]/div[1]/a[3]")
        linkedin.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.quit()