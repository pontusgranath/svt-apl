import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SearchResults(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        
    # Tests so the default amount of titles is correct
    def test_default_amount_of_titles(self):
        driver = self.driver
        driver.get("http://localhost:8000")

        searchField = driver.find_element_by_name('search-title')
        searchField.send_keys('Klipp/simc')

        searchField.send_keys(Keys.RETURN)

        titles = driver.find_elements_by_class_name('list-title')

        self.assertEqual(5, len(titles))

    # Tests so the correct amount of titles is displayed when amount search field is used
    def test_correct_amount_of_titles(self):
        driver = self.driver
        driver.get("http://localhost:8000")

        def checkAmountOfTitles(amount, title):
            searchField = driver.find_element_by_name('search-title')
            searchAmountField = driver.find_element_by_name('title-amount')

            searchField.send_keys(title)
            searchAmountField.send_keys(amount)

            searchAmountField.send_keys(Keys.RETURN)

            titles = driver.find_elements_by_class_name('list-title')

            self.assertEqual(int(amount), len(titles))

        checkAmountOfTitles("3" ,"Klipp/simc")
        checkAmountOfTitles("99" ,"Klipp/simc")
        checkAmountOfTitles("99" ,"Agenda")
        checkAmountOfTitles("1" ,"Agenda")
        checkAmountOfTitles("0" ,"World on fire")
        checkAmountOfTitles("68" ,"DNA")


    # Tests if the search results are correct
    def test_correct_search_results(self):
        driver = self.driver
        driver.get("http://localhost:8000")

        def compareResults(title, expectedResults):
            searchField = driver.find_element_by_name('search-title')
            searchField.send_keys(title)
            searchField.send_keys(Keys.RETURN)

            searchResults = [element.text for element in driver.find_elements_by_class_name("list-title")]

            self.assertEqual(expectedResults, searchResults)

        compareResults("Klipp/simc", ['Come home', 'Folkhälsomyndigheten om covid-19', 'Bolibompa: Drakens trädgård', 'Skidskytte: VM', 'Melodifestivalen 2020: Deltävling 3'])
        compareResults("Bang", ['Eagles', 'The Split', 'Come home', 'World on fire', 'Skidskytte: VM'])
        compareResults("Leif och Billy", ['Folkhälsomyndigheten om covid-19', 'Kalifat', 'Pippi Långstrump', 'Melodifestivalen 2020: Deltävling 3', 'På spåret'])

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()