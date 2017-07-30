# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class Browser():

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
        self.driver.implicitly_wait(10)

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

    def search(self, search):
        """
        serch for something on the page
        """
        self.driver.find_element_by_class_name('room5-icons-search').click()
        searchField = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'search-input'))
        )
        searchField.send_keys(search)
        self.driver.implicitly_wait(10)

    def search_result(self):
        result = 'div.post-title > a > h3.mt-8.montserrat-regular'
        searchResult = []

        searchResult = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, result))
        )
        assert "Brazil" in searchResult[0].text

    def select_country_page(self, country):
        select = Select(self.find_by_id('select-country'))
        select.select_by_visible_text(country)
        assert u'Room5: encontre inspiração para a sua próxima estadia em hotel no trivago.com.br' in self.driver.title

    def validate_contry_page(self):
        assert 'http://room5.trivago.com.br/' in self.driver.current_url

    def menu_open(self):
        menu_btn = self.find_by_class_name('nav-icon')
        menu_btn.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.single-menu.montserrat-regular.open'))
        )

    def menu_navigation(self):
        family_option = self.driver.find_element_by_xpath('//a[text()="Family"]')
        family_option.click()
        self.driver.implicitly_wait(10)

    def validate_family_page(self):
        self.driver.find_element_by_xpath('//h1[text()="Family"]')
        assert 'http://room5.trivago.com/theme/family/' in self.driver.current_url
        assert u'Family' in self.driver.title

    def inspire_me_subscription(self, email):
        self.find_by_css_selector('.etn_box.etn_light')

        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'etn_email'))
        )

        email_field.clear()
        email_field.send_keys(email)

        inpire_me_btn = self.find_by_class_name('etn__submit')
        inpire_me_btn.click()

    def validate_email_subscription(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.etn_box.etn_dark'))
        )
        self.driver.find_element_by_xpath('//div/p[text()="You are now checked-in!"]')
