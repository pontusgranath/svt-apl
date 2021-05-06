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


    # Tests if the text in distance-button changes before and after click
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

    
    # Tests if the correct distance-measurements are being displayed
    def test_correct_distance_results(self):
        driver = self.driver
        driver.get("http://localhost:8000")

        def compareDistance(title, expectedResults):
            searchField = driver.find_element_by_name('search-title')
            searchField.send_keys(title)
            searchField.send_keys(Keys.RETURN)

            distanceButton = driver.find_element_by_id('distance-button')
            distanceButton.click()

            searchResults = [element.text for element in driver.find_elements_by_class_name("distance-measurement")]
            searchResults = [i.split('- ', 1)[1] for i in searchResults]

            self.assertListEqual(expectedResults, searchResults)

        compareDistance('Klipp/simc', ['0.16', '0.2', '0.21', '0.22', '0.22'])
        compareDistance('Bang', ['0.25', '0.27', '0.27', '0.28', '0.29'])
        compareDistance('Leif och Billy', ['0.15', '0.17', '0.17', '0.19', '0.19'])

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()