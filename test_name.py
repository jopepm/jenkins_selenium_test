from selenium import webdriver

driver = webdriver.Chrome('path_to_chromedriver')
driver.get('https://example.com')

title = driver.title
print("Title of the website:", title)

driver.quit()
