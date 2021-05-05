import unittest
from selenium import webdriver

class Title(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # Checks if the site title is correct
    def test_title_text(self):
        driver = self.driver
        driver.get("http://localhost:8000")

        self.assertIn("Searchbar", driver.title)

    # Checks if the text on the page header if correct
    def test_header_text(self):
        driver = self.driver
        driver.get("http://localhost:8000")

        titleText = driver.find_element_by_id('title').text
        self.assertIn('SVT-APL Searchbar for statistical analysis stuff', titleText)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()