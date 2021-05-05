import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class SearchResultsHeader(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_correct_inline_search_results(self):
        driver = self.driver = webdriver.Chrome()
        driver.get("http://localhost:8000")

        searchField = driver.find_element_by_name('search-title')
        searchField.send_keys('Klipp/simc')
        searchField.send_keys(Keys.RETURN)

        inlineButton = driver.find_element_by_class_name('plus-button')
        inlineButton.click()

        time.sleep(2)
        

        x = driver.find_element_by_xpath('//span[@class="inline_distance"]/parent::li')
        print('Element Found')



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()