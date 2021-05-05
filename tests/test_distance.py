import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Distance(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        
    # Tests so the text on the toggle distance button properly changes on click
    def test_distance_button_text(self):
        driver = self.driver
        driver.get("http://localhost:8000")

        searchField = driver.find_element_by_name('search-title')
        searchField.send_keys("Klipp/simc")
        searchField.send_keys(Keys.RETURN)

        distanceButton = driver.find_element_by_id('distance-button')

        self.assertIn("Display distance", distanceButton.text)
        print("First assertion finished!")

        distanceButton.click()

        self.assertIn("Hide distance", distanceButton.text)
        print("Second assertion finished!")

        distanceButton.click()

        self.assertIn("Display distance", distanceButton.text)
        print("Third assertion finished!")

    def test_distance_button_toggle_distance(self):
        driver = self.driver
        driver.get("http://localhost:8000")

        searchField = driver.find_element_by_name('search-title')
        searchField.send_keys("Klipp/simc")
        searchField.send_keys(Keys.RETURN)

        distanceButton = driver.find_element_by_id('distance-button')
        distance = driver.find_elements_by_class_name('distance-measurement')
        # Fails test if list is empty
        self.assertIsNot(0, len(distance))
        
        # Checks if all elements are hidden
        index = 0
        for item in distance:
            visibility = item.value_of_css_property("visibility")
            self.assertEqual(visibility, "hidden")
            index += 1
            print("Item", index, "is hidden!")

        distanceButton.click()

        # Checks if all elements are visible after click
        index = 0
        for item in distance:
            visibility = item.value_of_css_property("visibility")
            self.assertEqual(visibility, "visible")
            index += 1
            print("Item", index, "is visible!")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()