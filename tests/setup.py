import os
from selenium import webdriver

# Locates the parent directory of tests
parentPath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

# Creates a variable "options" with the Options() class attributes
options = webdriver.ChromeOptions()

# Adds the no-sandbox as an argument
options.add_argument("no-sandbox")
# Adds headless as an argument
options.add_argument("headless")

driver = webdriver.Chrome(options=options)

# Where we want to go from the parent directory => index
desiredPath = "\\Quest-Tracker\\public\\home.html"

# Loads in the website
driver.get("http://localhost:8000/")