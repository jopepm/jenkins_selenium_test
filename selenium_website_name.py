from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options = options)
driver.get('./example.html')

title = driver.title
print("Title of the website:", title)

driver.quit()
