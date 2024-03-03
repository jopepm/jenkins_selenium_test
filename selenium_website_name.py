from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless") 
driver = webdriver.Chrome(options=chrome_options)
driver.get('./example.html')

title = driver.title
print("Title of the website:", title)

driver.quit()
