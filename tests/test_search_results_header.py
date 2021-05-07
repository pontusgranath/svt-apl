import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SearchResultsHeader(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    # Checks if "Search results for: " text is correct  
    def test_search_results_header_text(self):
        driver = self.driver
        driver.get("http://localhost:8000")

        searchField = driver.find_element_by_name('search-title')
        searchField.clear()
        searchAmountField = driver.find_element_by_name('title-amount')
        searchAmountField.clear()

        searchField.send_keys("Klipp/simc")
        searchField.send_keys(Keys.RETURN)

        searchHeaderText = driver.find_element_by_id('search-results-text').text
        
        self.assertIn("Search results for: ", searchHeaderText)
        
    # Tests multiple times if the header result text is correct
    def test_search_results_header_result_text(self):
        driver = self.driver
        driver.get("http://localhost:8000")

        def assertHeaderText(title):
            searchField = driver.find_element_by_name('search-title')
            searchField.clear()
            searchAmountField = driver.find_element_by_name('title-amount')
            searchAmountField.clear()
            
            searchField.send_keys(title)
            searchField.send_keys(Keys.RETURN)

            searchHeaderResultText = driver.find_element_by_xpath('//h2[@id="search-results-text"]/span').text

            self.assertIn(title, searchHeaderResultText)

            print(title, "found!")

        assertHeaderText("Agenda")
        assertHeaderText("Kulturnyheterna")
        assertHeaderText("Klipp/simc")
        assertHeaderText("World on fire")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()