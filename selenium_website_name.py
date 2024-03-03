import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


script_dir = os.path.dirname(os.path.abspath(__file__))
html_file_path = os.path.join(script_dir, 'example.html')

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options = options)
print(html_file_path)
driver.get(html_file_path)

title = driver.title
print("Title of the website:", title)

driver.quit()
