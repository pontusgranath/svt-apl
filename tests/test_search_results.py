import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Title(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        
    # What the test does
    def test_name(self):
        driver = self.driver
        driver.get("http://localhost:8000")        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()