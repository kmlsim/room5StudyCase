from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Browser(object):

    base_url = 'http://room5.trivago.com'
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    #assert "Room5: hotel inspiration from trivago.com" in driver.title

    def close(self):
        """
        close the webdriver instance
        """
        self.driver.quit()

    def visit(self, location=''):
        """
        navigate webdriver to different pages
        """
        url = self.base_url + location
        self.driver.get(url)

    def find_by_id(self, selector):
        """
        find a page element in the DOM
        """
        return self.driver.find_element_by_id(selector)

    def find_by_class_name(self, selector):
        """
        find a page element in the DOM
        """
        return self.driver.find_element_by_class_name(selector)

    def find_by_css_selector(self, selector):
        """
        find a page element in the DOM
        """
        return self.driver.find_element_by_css_selector(selector)


