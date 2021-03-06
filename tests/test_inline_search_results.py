import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InlineSearchResults(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    # Checks if the results in inline-search is correct
    def test_correct_inline_search_results(self):
        driver = self.driver = webdriver.Chrome()
        driver.get("http://localhost:8000")

        def CompareResults(title, amount, expectedResults):
            searchField = driver.find_element_by_name('search-title')
            searchField.clear()
            searchAmountField = driver.find_element_by_name('title-amount')
            searchAmountField.clear()
            
            searchField.send_keys(title)
            searchField.send_keys(Keys.RETURN)

            inlineButtons = driver.find_elements_by_class_name('plus-button')
            inlineButtons[amount].click()
        
            inlineList = driver.find_elements_by_xpath('//span[@class="inline_distance"]/parent::li')
            inlineSearchResults = [element.text for element in inlineList]
            inlineSearchResults = [i.split(' - ', 1)[0] for i in inlineSearchResults]

            self.assertListEqual(expectedResults, inlineSearchResults)

        CompareResults('Klipp/simc', 0, ['Bolibompa: Drakens trädgård', 'Kalifat', 'Skidskytte: VM', 'Melodifestivalen 2020: Deltävling 3', 'Svenska nyheter'])
        CompareResults('Klipp/simc', 1, ['Kalifat', 'Melodifestivalen 2020: Deltävling 3', 'Falkenberg forever', 'Svenska nyheter', 'Stjärnorna på slottet'])
        CompareResults('Bolibompa: Drakens trädgård', 4, ['Kalifat', 'Pippi Långstrump', 'Skidskytte: VM', 'Falkenberg forever', 'Svenska nyheter'])

    # Tests if distance measurements are correct in inline-search results
    def test_correct_inline_distance_results(self):
        driver = self.driver
        driver.get("http://localhost:8000")

        def compareDistance(title, amount, expectedResults):
            searchField = driver.find_element_by_name('search-title')
            searchField.clear()
            searchAmountField = driver.find_element_by_name('title-amount')
            searchAmountField.clear()
            
            searchField.send_keys(title)
            searchField.send_keys(Keys.RETURN)

            inlineButtons = driver.find_elements_by_class_name('plus-button')
            inlineButtons[amount].click()

            searchResults = [element.text for element in driver.find_elements_by_class_name('inline_distance')]

            self.assertListEqual(expectedResults, searchResults)

        compareDistance('Klipp/simc', 0, ['0.13', '0.14', '0.14', '0.14', '0.15'])
        compareDistance('Klipp/simc', 1, ['0.12', '0.14', '0.15', '0.15', '0.15'])
        compareDistance('Greta Gris', 4, ['0.15', '0.17', '0.19', '0.19', '0.19'])
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()