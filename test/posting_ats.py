import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username").send_keys("jaker")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("maverick1a")
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/admin")
        assert "Logged In"
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr/td[1]/a").click()
        time.sleep(2)
        driver.get("http://127.0.0.1:8000/admin/blog/post/add/")
        driver.find_element_by_id("id_author").send_keys("jaker")
        time.sleep(4)
        driver.find_element_by_id("id_title").send_keys("admin post test")
        driver.find_element_by_id("id_text").send_keys("This is only a test.")
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[5]/div/p/span[1]/a[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[5]/div/p/span[2]/a[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(4)
        # admin test complete, moving on to normal post
        driver.get("http://127.0.0.1:8000/")
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/a/span").click()
        time.sleep(4)
        driver.find_element_by_id("id_title").send_keys("user post test")
        driver.find_element_by_id("id_text").send_keys("This is also only a test.")
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
        time.sleep(4)
        driver.get("http://127.0.0.1:8000/")
        time.sleep(5)
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
