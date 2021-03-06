import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PlusButton(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()


    # Tests if plus-button changes value before and after click
    def test_plus_button_correct_symbol(self):
        driver = self.driver
        driver.get("http://localhost:8000")

        searchField = driver.find_element_by_name('search-title')
        searchField.clear()
        searchAmountField = driver.find_element_by_name('title-amount')
        searchAmountField.clear()
        
        searchField.send_keys('Klipp/simc')
        searchField.send_keys(Keys.RETURN)

        plusButton = driver.find_element_by_class_name('plus-button')
        valueAttribute = plusButton.get_attribute('value')

        self.assertEqual('+', valueAttribute)

        plusButton.click()

        plusButton = driver.find_element_by_class_name('plus-button')
        valueAttribute = plusButton.get_attribute('value')
        self.assertEqual('>', valueAttribute)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()